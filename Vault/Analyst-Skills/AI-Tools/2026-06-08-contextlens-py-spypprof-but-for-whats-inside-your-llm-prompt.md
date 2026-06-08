---
title: ContextLens — py-spy/pprof but for what's inside your LLM prompt
date: '2026-06-08'
source: https://dev.to/harshal_sant_be921c5039f2/contextlens-py-spypprof-but-for-whats-inside-your-llm-prompt-59l7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]'
- '[[2026-05-08-i-built-an-ai-agent-that-does-osint-investigations-from-your-terminal]]'
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
- '[[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
status: unread
---

> **TL;DR:** In multi-turn agent loops, the full context re-sends on every API call. A tool result added at turn 3 gets billed again at turns 4, 5, 6, 7... forever. Most of it is never read again. Standard observability tools tell yo…

## What’s new and why it matters
In multi-turn agent loops, the full context re-sends on every API call. A tool result added at turn 3 gets billed again at turns 4, 5, 6, 7... forever. Most of it is never read again. Standard observability tools tell you the total token count. They never tell you what's in there or how much of it is waste . That's what ContextLens fixes. What it does ContextLens is a diagnostic profiler for LLM agent context windows. It: Decomposes the context window into regions: system prompt, tool schemas, tool results, retrieved chunks, user messages, assistant messages Tracks which blocks get re-billed a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/harshal_sant_be921c5039f2/contextlens-py-spypprof-but-for-whats-inside-your-llm-prompt-59l7

## Related notes
- [[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]
- [[2026-05-08-i-built-an-ai-agent-that-does-osint-investigations-from-your-terminal]]
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
- [[2026-04-15-why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
