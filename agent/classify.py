from __future__ import annotations

from dataclasses import dataclass

from .models import DiscoveredItem
from .text import tokens


@dataclass(frozen=True)
class Classified:
    domain: str
    tags: list[str]


def _domain_allowed(domain: str, hay_lower: str) -> bool:
    # Prevent overly-generic matches from dumping content into sensitive domains.
    if domain == "Zendesk":
        return "zendesk" in hay_lower

    if domain == "Customer-Support-Analytics":
        markers = [
            "support analytics",
            "customer support analytics",
            "ticket analytics",
            "zendesk explore",
            "csat",
            "nps",
            "fcr",
            "first response",
            "first reply",
            "time to resolution",
            "deflection",
            "contact reason",
        ]
        return any(m in hay_lower for m in markers)

    return True


def classify_item(item: DiscoveredItem, domain_keywords: dict[str, list[str]], tag_keywords: dict[str, list[str]]) -> Classified:
    hay = " ".join(
        [
            item.title or "",
            item.summary or "",
            item.url or "",
            " ".join(f"{k}:{v}" for k, v in (item.extra or {}).items()),
        ]
    )
    hay_lower = hay.lower()
    tks = tokens(hay)

    # Domain scoring
    scores: list[tuple[int, str]] = []
    for domain, kws in domain_keywords.items():
        score = 0
        for kw in kws:
            kwl = kw.lower()
            if kwl in hay_lower:
                score += 2
            if kwl in tks:
                score += 3
        scores.append((score, domain))

    scores.sort(reverse=True, key=lambda x: x[0])

    best_domain = "Productivity"
    for score, domain in scores:
        if score <= 0:
            break
        if _domain_allowed(domain, hay_lower):
            best_domain = domain
            break

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
        "Customer-Support-Analytics": "support-analytics",
        "Tableau": "tableau",
        "Presentations": "presentations",
        "Productivity": "productivity",
    }
    dt = domain_tag_map.get(best_domain)
    if dt:
        tags.add(dt)

    return Classified(domain=best_domain, tags=sorted(tags))
