from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from .text import normalize_ws, tokens


FRONTMATTER_TEMPLATE_KEYS = [
    "title",
    "date",
    "source",
    "domain",
    "relevance",
    "tags",
    "related",
    "status",
]


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def slugify(title: str) -> str:
    s = normalize_ws(title).lower()
    s = re.sub(r"[^a-z0-9\-\s]", "", s)
    s = re.sub(r"\s+", "-", s).strip("-")
    return s[:120] or "note"


@dataclass
class ParsedNote:
    path: Path
    frontmatter: dict[str, Any]
    body: str


_frontmatter_re = re.compile(r"\A---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def parse_note(path: Path) -> ParsedNote:
    txt = path.read_text(encoding="utf-8")
    m = _frontmatter_re.match(txt)
    if not m:
        return ParsedNote(path=path, frontmatter={}, body=txt)
    fm_raw = m.group(1)
    fm = yaml.safe_load(fm_raw) or {}
    body = txt[m.end() :]
    return ParsedNote(path=path, frontmatter=fm, body=body)


def render_note(frontmatter: dict[str, Any], body: str) -> str:
    # Ensure required keys exist
    fm = dict(frontmatter)
    for k in FRONTMATTER_TEMPLATE_KEYS:
        if k not in fm:
            fm[k] = [] if k in ("tags", "related") else ""
    if not fm.get("date"):
        fm["date"] = _utc_now_iso()
    if not fm.get("status"):
        fm["status"] = "unread"

    fm_txt = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    return f"---\n{fm_txt}\n---\n\n{body.strip()}\n"


def ensure_dirs(vault_dir: Path) -> None:
    (vault_dir / "Analyst-Skills" / "Python").mkdir(parents=True, exist_ok=True)
    (vault_dir / "Analyst-Skills" / "SQL").mkdir(parents=True, exist_ok=True)
    (vault_dir / "Analyst-Skills" / "AI-Tools").mkdir(parents=True, exist_ok=True)
    (vault_dir / "Analyst-Skills" / "Zendesk").mkdir(parents=True, exist_ok=True)
    (vault_dir / "Analyst-Skills" / "Tableau").mkdir(parents=True, exist_ok=True)
    (vault_dir / "Analyst-Skills" / "Presentations").mkdir(parents=True, exist_ok=True)
    (vault_dir / "Analyst-Skills" / "Productivity").mkdir(parents=True, exist_ok=True)
    (vault_dir / "Inbox").mkdir(parents=True, exist_ok=True)
    (vault_dir / "Weekly-Digests").mkdir(parents=True, exist_ok=True)


def domain_folder(vault_dir: Path, domain: str) -> Path:
    return vault_dir / "Analyst-Skills" / domain


def write_note_if_missing(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def list_all_notes(vault_dir: Path) -> list[Path]:
    return [p for p in vault_dir.rglob("*.md") if p.is_file()]


def find_related_notes(
    vault_dir: Path,
    title: str,
    body: str,
    max_related: int = 6,
) -> list[str]:
    target = tokens(title + " " + body)
    if not target:
        return []

    scored: list[tuple[int, str]] = []
    for p in list_all_notes(vault_dir):
        # Skip weekly digests; they tend to be very broad
        if "Weekly-Digests" in p.parts:
            continue
        try:
            parsed = parse_note(p)
        except Exception:
            continue
        other_title = str(parsed.frontmatter.get("title") or p.stem)
        other_tks = tokens(other_title + " " + parsed.body)
        overlap = len(target.intersection(other_tks))
        if overlap <= 3:
            continue
        # Obsidian wikilink uses basename without extension
        scored.append((overlap, p.stem))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [stem for _, stem in scored[:max_related]]
