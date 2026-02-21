from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class AgentState:
    seen_ids: set[str] = field(default_factory=set)
    pypi_versions: dict[str, str] = field(default_factory=dict)
    weekly_digest_weeks: set[str] = field(default_factory=set)

    @classmethod
    def load(cls, path: Path) -> "AgentState":
        if not path.exists():
            return cls()
        raw = json.loads(path.read_text(encoding="utf-8"))
        return cls(
            seen_ids=set(raw.get("seen_ids", [])),
            pypi_versions=dict(raw.get("pypi_versions", {})),
            weekly_digest_weeks=set(raw.get("weekly_digest_weeks", [])),
        )

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload: dict[str, Any] = {
            "seen_ids": sorted(self.seen_ids),
            "pypi_versions": self.pypi_versions,
            "weekly_digest_weeks": sorted(self.weekly_digest_weeks),
        }
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
