---
title: You cannot predict what an LLM call will cost before you make it
date: '2026-08-10'
source: https://dev.to/focxle/you-cannot-predict-what-an-llm-call-will-cost-before-you-make-it-8e9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]'
- '[[2026-08-08-i-built-an-async-wrapper-for-openaianthropic-sdks-because-i-didnt-want-a-proxy-in-my-request-path]]'
status: unread
---

> **TL;DR:** I spent a week building spending caps for AI agents on an assumption that turned out to be wrong, and the way it was wrong is more interesting than the feature. The assumption is the obvious one. Before making a model ca…

## What’s new and why it matters
I spent a week building spending caps for AI agents on an assumption that turned out to be wrong, and the way it was wrong is more interesting than the feature. The assumption is the obvious one. Before making a model call, estimate what it will cost. If that estimate breaks the budget, refuse the call. Every budget system works this way: check, then spend. Then I measured the estimate against real calls, and it does not work. Not "needs tuning". Does not work, and cannot be made to. The measurement 12 calls recorded through OpenRouter against openai/gpt-oss-20b:free , 9 of which had a compara…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/focxle/you-cannot-predict-what-an-llm-call-will-cost-before-you-make-it-8e9

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]
- [[2026-08-08-i-built-an-async-wrapper-for-openaianthropic-sdks-because-i-didnt-want-a-proxy-in-my-request-path]]
