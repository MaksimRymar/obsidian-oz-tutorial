from __future__ import annotations

from datetime import datetime, timezone

import feedparser

from ..models import DiscoveredItem


def _published(entry: dict) -> datetime | None:
    # feedparser provides published_parsed/updated_parsed
    for k in ("published_parsed", "updated_parsed"):
        if entry.get(k):
            st = entry[k]
            try:
                return datetime(*st[:6], tzinfo=timezone.utc)
            except Exception:
                pass
    return None


def fetch_feed(name: str, url: str, limit: int = 50) -> list[DiscoveredItem]:
    fp = feedparser.parse(url)
    items: list[DiscoveredItem] = []
    for e in (fp.entries or [])[:limit]:
        link = e.get("link")
        title = e.get("title") or "(untitled)"
        if not link:
            continue
        item_id = e.get("id") or link
        summary = e.get("summary") or e.get("description")
        items.append(
            DiscoveredItem(
                id=f"rss:{name}:{item_id}",
                title=title,
                url=link,
                source=name,
                published_at=_published(e),
                summary=summary,
                extra={},
            )
        )
    return items
