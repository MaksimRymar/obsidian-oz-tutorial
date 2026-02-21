from __future__ import annotations

from datetime import datetime, timezone

import requests
from bs4 import BeautifulSoup

from ..models import DiscoveredItem


def fetch_trending(language: str, limit: int = 30) -> list[DiscoveredItem]:
    url = f"https://github.com/trending/{language}?since=daily"
    html = requests.get(url, timeout=30, headers={"User-Agent": "obsidian-analyst-vault-agent"}).text
    soup = BeautifulSoup(html, "html.parser")

    items: list[DiscoveredItem] = []
    for article in soup.select("article.Box-row")[:limit]:
        a = article.select_one("h2 a")
        if not a:
            continue
        repo = " ".join(a.get_text(" ").split())
        repo = repo.replace(" / ", "/")
        href = a.get("href")
        if not href:
            continue
        full_url = f"https://github.com{href.strip()}"

        desc_el = article.select_one("p")
        desc = desc_el.get_text(" ").strip() if desc_el else ""

        items.append(
            DiscoveredItem(
                id=f"ghtrending:{language}:{repo}",
                title=f"{repo} (trending)",
                url=full_url,
                source=f"GitHub Trending ({language})",
                published_at=datetime.now(timezone.utc),
                summary=desc,
                extra={"repo": repo, "language": language},
            )
        )

    return items


def keyword_filter(items: list[DiscoveredItem], keywords_any: list[str]) -> list[DiscoveredItem]:
    if not keywords_any:
        return items
    kws = [k.lower() for k in keywords_any]
    out: list[DiscoveredItem] = []
    for it in items:
        hay = (it.title + " " + (it.summary or "")).lower()
        if any(k in hay for k in kws):
            out.append(it)
    return out
