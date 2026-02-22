from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class LLMResult:
    summary: str
    how_to_apply: str
    relevance: str  # 🔴 / 🟡 / 🟢


def enabled() -> bool:
    return bool(os.getenv("OPENAI_API_KEY"))


def summarize(title: str, source: str, url: str, raw_text: str, domain: str) -> LLMResult:
    """Best-effort LLM summary.

    If OpenAI is unavailable, returns a deterministic heuristic summary.
    """

    if not enabled():
        # Heuristic fallback: use whatever content we have (RSS excerpt, etc.)
        try:
            from bs4 import BeautifulSoup

            plain = BeautifulSoup(raw_text or "", "html.parser").get_text(" ", strip=True)
        except Exception:
            plain = (raw_text or "").strip()

        plain = " ".join((plain or "").split())
        if plain:
            summary = plain[:600].rstrip() + ("…" if len(plain) > 600 else "")
        else:
            summary = f"{title}."

        how = "- Extract 1 actionable tactic from this post and try it on a real dataset this week.\n"
        if domain in ("Python", "AI-Tools"):
            how += "- Reproduce the example in a notebook; then refactor into a reusable function.\n"
        if domain in ("SQL",):
            how += "- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.\n"
        how += "- Add a short note: what changed in your workflow?"

        # Conservative default
        relevance = "🟡"
        if any(k in (title.lower() + " " + plain.lower()) for k in ["release", "released", "breaking", "deprec", "security", "new feature"]):
            relevance = "🔴"

        return LLMResult(summary=summary, how_to_apply=how, relevance=relevance)

    # Lazy import so local runs work without the dependency configured in all envs.
    from openai import OpenAI

    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
    client = OpenAI()

    prompt = f"""
You are curating a knowledge base for a working data/business analyst.

Create:
1) A concise summary (2-5 sentences) of what is new and why it matters.
2) A practical 'How to apply' section with steps and/or code snippets.
3) A relevance rating: 🔴 must-know / 🟡 good-to-know / 🟢 nice-to-have.

Domain: {domain}
Source: {source}
Title: {title}
URL: {url}

Content (may be partial):
{raw_text}
""".strip()

    resp = client.responses.create(
        model=model,
        input=prompt,
        temperature=0.2,
    )
    txt = (resp.output_text or "").strip()

    # Very simple parsing; keep the agent resilient.
    summary = ""
    how = ""
    relevance = "🟡"

    lines = [l.rstrip() for l in txt.splitlines() if l.strip()]
    section = None
    for l in lines:
        low = l.lower()
        if low.startswith("summary"):
            section = "summary"
            continue
        if low.startswith("how"):
            section = "how"
            continue
        if "relevance" in low and ("🔴" in l or "🟡" in l or "🟢" in l):
            if "🔴" in l:
                relevance = "🔴"
            elif "🟢" in l:
                relevance = "🟢"
            else:
                relevance = "🟡"
            continue

        if section == "summary":
            summary += (l + " ")
        elif section == "how":
            how += (l + "\n")

    summary = summary.strip() or txt[:4000]
    how = how.strip() or "- Apply one technique from the post in a small sandbox project."

    # If the model didn't provide relevance, infer a default.
    if "🔴" in txt:
        relevance = "🔴"
    elif "🟢" in txt:
        relevance = "🟢"

    return LLMResult(summary=summary, how_to_apply=how, relevance=relevance)
