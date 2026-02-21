from __future__ import annotations

from dataclasses import dataclass

from .models import DiscoveredItem
from .text import tokens


@dataclass(frozen=True)
class Classified:
    domain: str
    tags: list[str]


def classify_item(item: DiscoveredItem, domain_keywords: dict[str, list[str]], tag_keywords: dict[str, list[str]]) -> Classified:
    hay = " ".join(
        [
            item.title or "",
            item.summary or "",
            item.url or "",
            " ".join(f"{k}:{v}" for k, v in (item.extra or {}).items()),
        ]
    )
    tks = tokens(hay)

    # Domain scoring
    best_domain = "Productivity"
    best_score = 0
    for domain, kws in domain_keywords.items():
        score = 0
        for kw in kws:
            if kw.lower() in hay.lower():
                score += 2
            if kw.lower() in tks:
                score += 3
        if score > best_score:
            best_score = score
            best_domain = domain

    # Tags
    tags: set[str] = set()
    for tag, kws in tag_keywords.items():
        for kw in kws:
            if kw.lower() in hay.lower() or kw.lower() in tks:
                tags.add(tag)
                break

    # Always include domain tag
    domain_tag_map = {
        "Python": "python",
        "SQL": "sql",
        "AI-Tools": "ai",
        "Zendesk": "zendesk",
        "Tableau": "tableau",
        "Presentations": "presentations",
        "Productivity": "productivity",
    }
    dt = domain_tag_map.get(best_domain)
    if dt:
        tags.add(dt)

    return Classified(domain=best_domain, tags=sorted(tags))
