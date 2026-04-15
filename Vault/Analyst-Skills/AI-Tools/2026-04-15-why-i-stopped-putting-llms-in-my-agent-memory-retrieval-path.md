---
title: Why I stopped putting LLMs in my agent memory retrieval path
date: '2026-04-15'
source: https://dev.to/aarjay_singh_0f76e7ca03bf/why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path-4bia
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]'
status: unread
---

> **TL;DR:** Every agent pipeline I've touched in the last eighteen months reinvents memory, and most of them do it badly. Planner decisions never reach the executor. Giant prompts get passed between agents as "context." Tokens burn…

## What’s new and why it matters
Every agent pipeline I've touched in the last eighteen months reinvents memory, and most of them do it badly. Planner decisions never reach the executor. Giant prompts get passed between agents as "context." Tokens burn on stale data. An LLM call sits in the retrieval path, so the same query returns different ranked results on different runs — which makes the system impossible to reason about and impossible to unit-test. The fix, once I'd seen it happen enough times, is boring: treat memory as infrastructure , not as prompt engineering. That's what Memwright is. The problem with LLM-in-the-loo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aarjay_singh_0f76e7ca03bf/why-i-stopped-putting-llms-in-my-agent-memory-retrieval-path-4bia

## Related notes
- [[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]
