from __future__ import annotations

import re


_word_re = re.compile(r"[a-z0-9][a-z0-9\-\._/]+", re.IGNORECASE)


def normalize_ws(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def tokens(s: str) -> set[str]:
    return {t.lower() for t in _word_re.findall(s or "")}
