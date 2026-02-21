from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .classify import classify_item
from .models import DiscoveredItem
from .vault import find_related_notes, parse_note, render_note


def _iso_today() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def enrich_inbox(
    vault_dir: Path,
    inbox_dir: Path,
    domain_keywords: dict[str, list[str]],
    tag_keywords: dict[str, list[str]],
) -> list[Path]:
    """Mutates inbox notes in place.

    Returns list of modified note paths.
    """

    modified: list[Path] = []
    if not inbox_dir.exists():
        return modified

    for p in sorted(inbox_dir.glob("*.md")):
        parsed = parse_note(p)
        fm = dict(parsed.frontmatter)
        body = parsed.body or ""

        # Infer title
        if not fm.get("title"):
            fm["title"] = p.stem

        # Infer date
        if not fm.get("date"):
            fm["date"] = _iso_today()

        # Classification from the note text
        as_item = DiscoveredItem(
            id=f"inbox:{p.name}",
            title=str(fm.get("title") or p.stem),
            url="",
            source="Inbox",
            published_at=None,
            summary=body[:2000],
            extra={},
        )
        classified = classify_item(as_item, domain_keywords, tag_keywords)

        if not fm.get("domain"):
            fm["domain"] = classified.domain

        # Tags: normalize to '#tag'
        tags: set[str] = set()
        existing = fm.get("tags") or []
        if isinstance(existing, str):
            existing = [existing]
        for t in existing:
            t = str(t).strip()
            if not t:
                continue
            tags.add(t if t.startswith("#") else f"#{t}")
        for t in classified.tags:
            tags.add(f"#{t}")
        fm["tags"] = sorted(tags)

        if not fm.get("status"):
            fm["status"] = "unread"

        # Related
        related = find_related_notes(vault_dir, str(fm.get("title") or ""), body)
        fm["related"] = [f"[[{x}]]" for x in related]

        # Suggest folder (but do not move automatically)
        suggest_line = f"Suggested folder: `Analyst-Skills/{fm.get('domain')}/`\n"
        if "Suggested folder:" not in body and fm.get("domain"):
            body = suggest_line + "\n" + body.lstrip()

        new_txt = render_note(fm, body)
        if new_txt != p.read_text(encoding="utf-8"):
            p.write_text(new_txt, encoding="utf-8")
            modified.append(p)

    return modified
