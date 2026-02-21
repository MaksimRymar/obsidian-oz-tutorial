from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class DiscoveredItem:
    id: str
    title: str
    url: str
    source: str
    published_at: datetime | None = None
    summary: str | None = None
    extra: dict[str, str] = field(default_factory=dict)
