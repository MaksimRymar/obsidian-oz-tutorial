from __future__ import annotations

from .rss import fetch_feed
from ..models import DiscoveredItem


def fetch_tag(tag: str, limit: int = 30) -> list[DiscoveredItem]:
    # Medium supports RSS for tags
    url = f"https://medium.com/feed/tag/{tag}"
    items = fetch_feed(name=f"Medium #{tag}", url=url, limit=limit)
    out: list[DiscoveredItem] = []
    for it in items:
        out.append(
            DiscoveredItem(
                id=f"medium:{tag}:{it.id}",
                title=it.title,
                url=it.url,
                source=it.source,
                published_at=it.published_at,
                summary=it.summary,
                extra=it.extra,
            )
        )
    return out
