---
title: 'Building a Stock Advisor on a Coral Dev Board: From Edge TPU Bugs to Working
  TPU Inference'
date: '2026-05-13'
source: https://dev.to/charbull/building-a-stock-advisor-on-a-coral-dev-board-from-edge-tpu-bugs-to-working-tpu-inference-156
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]'
- '[[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]'
- '[[2026-04-17-postgresql-vs-mysql-which-is-better-for-your-application]]'
- '[[2026-03-05-building-an-ai-prediction-api-with-fastapi-lessons-from-an-open-source-project]]'
- '[[2026-04-14-stock-recommendation-system-using-anthropic-mcp-and-python]]'
status: unread
---

> **TL;DR:** A few months ago I set out to answer a simple question: can I build a scientific framework for deciding when to sell my Google RSUs instead of making decisions based on gut feeling? The answer turned out to be "sort of,…

## What’s new and why it matters
A few months ago I set out to answer a simple question: can I build a scientific framework for deciding when to sell my Google RSUs instead of making decisions based on gut feeling? The answer turned out to be "sort of, but the process taught me far more than the answer did." This post covers the full arc — hardware choices, architecture decisions, the bugs that kept predictions stuck at 0.00%, and finally a working system running at 2.5ms on the Edge TPU. I also added a second model — a direction classifier that predicts whether price will go up or down — to complement the original price regr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/charbull/building-a-stock-advisor-on-a-coral-dev-board-from-edge-tpu-bugs-to-working-tpu-inference-156

## Related notes
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]
- [[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]
- [[2026-04-17-postgresql-vs-mysql-which-is-better-for-your-application]]
- [[2026-03-05-building-an-ai-prediction-api-with-fastapi-lessons-from-an-open-source-project]]
- [[2026-04-14-stock-recommendation-system-using-anthropic-mcp-and-python]]
