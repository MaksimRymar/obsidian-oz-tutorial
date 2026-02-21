from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

from .vault import parse_note, render_note


@dataclass(frozen=True)
class DigestEntry:
    title: str
    path_stem: str
    domain: str
    relevance: str
    date: str


def _week_key(dt: datetime) -> str:
    iso_year, iso_week, _ = dt.isocalendar()
    return f"{iso_year}-W{iso_week:02d}"


def _relevance_score(r: str) -> int:
    if "🔴" in (r or ""):
        return 3
    if "🟡" in (r or ""):
        return 2
    if "🟢" in (r or ""):
        return 1
    return 0


def gather_last_week_notes(vault_dir: Path, now: datetime) -> list[DigestEntry]:
    cutoff = now - timedelta(days=7)
    out: list[DigestEntry] = []
    for p in vault_dir.rglob("*.md"):
        if not p.is_file():
            continue
        if "Weekly-Digests" in p.parts:
            continue
        parsed = parse_note(p)
        fm = parsed.frontmatter
        d = str(fm.get("date") or "")
        try:
            dt = datetime.fromisoformat(d)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
        except Exception:
            # If can't parse, skip
            continue
        if dt < cutoff:
            continue

        out.append(
            DigestEntry(
                title=str(fm.get("title") or p.stem),
                path_stem=p.stem,
                domain=str(fm.get("domain") or ""),
                relevance=str(fm.get("relevance") or ""),
                date=d,
            )
        )
    return out


def write_weekly_digest(vault_dir: Path, weekly_digest_dir: Path, now: datetime) -> Path:
    weekly_digest_dir.mkdir(parents=True, exist_ok=True)
    week_key = _week_key(now)

    notes = gather_last_week_notes(vault_dir, now)
    notes.sort(key=lambda n: (_relevance_score(n.relevance), n.date), reverse=True)

    top10 = notes[:10]

    # Tools/libs: heuristic: if title contains a version or 'released'
    tools = [n for n in notes if "released" in n.title.lower() or "version" in n.title.lower()]
    tools = tools[:10]

    # Trending skills: most common domains + tags
    domain_counts = Counter([n.domain for n in notes if n.domain])

    # Weekend suggestion: first 🔴 otherwise first 🟡
    weekend = next((n for n in notes if "🔴" in n.relevance), None) or (notes[0] if notes else None)

    fm = {
        "title": f"Weekly Digest {week_key}",
        "date": now.strftime("%Y-%m-%d"),
        "source": "Vault Digest",
        "domain": "Weekly-Digest",
        "relevance": "🟡",
        "tags": ["#digest"],
        "related": [],
        "status": "unread",
    }

    def wl(stem: str) -> str:
        return f"[[{stem}]]"

    body_lines: list[str] = []
    body_lines.append("## Top 10 updates")
    if not top10:
        body_lines.append("- (No notes found in the last 7 days.)")
    else:
        for n in top10:
            body_lines.append(f"- {n.relevance} {wl(n.path_stem)} — {n.title} ({n.domain})")

    body_lines.append("\n## New libraries or tools worth trying")
    if not tools:
        body_lines.append("- (No obvious library/tool releases detected.)")
    else:
        for n in tools:
            body_lines.append(f"- {wl(n.path_stem)} — {n.title}")

    body_lines.append("\n## Skills trending up this week")
    if not domain_counts:
        body_lines.append("- (Not enough data yet.)")
    else:
        for dom, cnt in domain_counts.most_common(6):
            body_lines.append(f"- {dom}: {cnt} notes")

    body_lines.append("\n## Weekend learning suggestion")
    if not weekend:
        body_lines.append("Pick one recent note and spend 60–90 minutes reproducing the example end-to-end.")
    else:
        body_lines.append(f"Focus on {wl(weekend.path_stem)} — {weekend.title}.")
        body_lines.append("Suggested approach:")
        body_lines.append("- Recreate the key example in a notebook or SQL scratchpad")
        body_lines.append("- Adapt it to one real dataset you use at work")
        body_lines.append("- Write a short 'what changed in my workflow' summary")

    digest_path = weekly_digest_dir / f"{week_key}-weekly-digest.md"
    digest_path.write_text(render_note(fm, "\n".join(body_lines)), encoding="utf-8")
    return digest_path
