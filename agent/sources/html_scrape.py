from __future__ import annotations

from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

from ..models import DiscoveredItem


def fetch_recent_links(name: str, url: str, limit: int = 25) -> list[DiscoveredItem]:
    html = requests.get(url, timeout=30, headers={"User-Agent": "obsidian-analyst-vault-agent"}).text
    soup = BeautifulSoup(html, "html.parser")

    # Heuristic: collect distinct article-ish links.
    seen: set[str] = set()
    items: list[DiscoveredItem] = []
    for a in soup.select("a[href]"):
        href = a.get("href")
        if not href:
            continue
        if href.startswith("#"):
            continue
        text = a.get_text(" ").strip()
        if not text or len(text) < 12:
            continue
        # Normalize to absolute-ish
        if href.startswith("/"):
            full = url.rstrip("/") + href
        elif href.startswith("http"):
            full = href
        else:
            continue

        if full in seen:
            continue
        seen.add(full)

        items.append(
            DiscoveredItem(
                id=f"html:{name}:{full}",
                title=text,
                url=full,
                source=name,
                published_at=datetime.now(timezone.utc),
                summary=None,
                extra={},
            )
        )
        if len(items) >= limit:
            break

    return items
