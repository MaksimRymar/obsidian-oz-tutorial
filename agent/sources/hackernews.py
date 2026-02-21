from __future__ import annotations

from datetime import datetime, timezone

import requests

from ..models import DiscoveredItem


def _dt(ts: int | None) -> datetime | None:
    if not ts:
        return None
    return datetime.fromtimestamp(ts, tz=timezone.utc)


def fetch_top(limit: int = 40) -> list[DiscoveredItem]:
    # Algolia supports front_page tag (current HN front page)
    url = "https://hn.algolia.com/api/v1/search?tags=front_page"
    data = requests.get(url, timeout=30).json()
    hits = (data.get("hits") or [])[:limit]
    items: list[DiscoveredItem] = []
    for h in hits:
        hn_id = str(h.get("objectID"))
        title = h.get("title") or h.get("story_title") or "(untitled)"
        link = h.get("url") or h.get("story_url") or f"https://news.ycombinator.com/item?id={hn_id}"
        items.append(
            DiscoveredItem(
                id=f"hn:top:{hn_id}",
                title=title,
                url=link,
                source="HackerNews (top)",
                published_at=_dt(h.get("created_at_i")),
                summary=h.get("_highlightResult", {}).get("title", {}).get("value"),
                extra={"hn_id": hn_id},
            )
        )
    return items


def fetch_new(limit: int = 40) -> list[DiscoveredItem]:
    # Newest stories
    url = "https://hn.algolia.com/api/v1/search_by_date?tags=story"
    data = requests.get(url, timeout=30).json()
    hits = (data.get("hits") or [])[:limit]
    items: list[DiscoveredItem] = []
    for h in hits:
        hn_id = str(h.get("objectID"))
        title = h.get("title") or "(untitled)"
        link = h.get("url") or f"https://news.ycombinator.com/item?id={hn_id}"
        items.append(
            DiscoveredItem(
                id=f"hn:new:{hn_id}",
                title=title,
                url=link,
                source="HackerNews (new)",
                published_at=_dt(h.get("created_at_i")),
                summary=None,
                extra={"hn_id": hn_id},
            )
        )
    return items
