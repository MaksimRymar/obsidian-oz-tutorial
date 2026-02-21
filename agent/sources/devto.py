from __future__ import annotations

from .rss import fetch_feed
from ..models import DiscoveredItem


def fetch_tag(tag: str, limit: int = 30) -> list[DiscoveredItem]:
    # Dev.to supports RSS per tag
    url = f"https://dev.to/feed/tag/{tag}"
    items = fetch_feed(name=f"Dev.to #{tag}", url=url, limit=limit)
    # prefix IDs
    out: list[DiscoveredItem] = []
    for it in items:
        out.append(
            DiscoveredItem(
                id=f"devto:{tag}:{it.id}",
                title=it.title,
                url=it.url,
                source=it.source,
                published_at=it.published_at,
                summary=it.summary,
                extra=it.extra,
            )
        )
    return out
