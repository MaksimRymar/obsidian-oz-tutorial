---
title: I built a tiny tool to catch the metric trap from my last post
date: '2026-06-08'
source: https://dev.to/elvisyao007/i-built-a-tiny-tool-to-catch-the-metric-trap-from-my-last-post-55ed
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#tool'
related:
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]'
- '[[2026-05-16-singidbot-telegram-id-retrieval-bot-for-openclaw-topic-configuration]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
status: unread
---

> **TL;DR:** In my last post I found that 33/100 "grounded-but-wrong" answers in my RAG eval were a measurement artifact — not real failures. The culprit: proportion recall with a relevant-doc-count denominator silently breaks on mul…

## What’s new and why it matters
In my last post I found that 33/100 "grounded-but-wrong" answers in my RAG eval were a measurement artifact — not real failures. The culprit: proportion recall with a relevant-doc-count denominator silently breaks on multi-answer datasets when k is small. So I packaged the diagnostic into a standalone tool: eval-sanity . pip install eval-sanity It takes the retrieved and relevant doc IDs you already have and tells you whether your recall metric is structurally capable of saying what you think it says — before you trust the number on your dashboard. What it checks: oracle ceiling : the best any…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/elvisyao007/i-built-a-tiny-tool-to-catch-the-metric-trap-from-my-last-post-55ed

## Related notes
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]
- [[2026-05-16-singidbot-telegram-id-retrieval-bot-for-openclaw-topic-configuration]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
