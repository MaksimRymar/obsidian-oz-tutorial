---
title: How I run a 9-wave AI investment briefing every morning in 90 seconds (full
  architecture)
date: '2026-05-13'
source: https://dev.to/tellmefrankie/how-i-run-a-9-wave-ai-investment-briefing-every-morning-in-90-seconds-full-architecture-3c51
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-06-summarize-1000-documents-with-python-for-under-1-pay-per-use-ai-api]]'
- '[[2026-03-25-i-automated-my-entire-morning-routine-with-5-python-scripts-heres-the-code]]'
- '[[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]'
- '[[2026-03-23-i-ran-56-experiments-to-find-the-best-way-to-make-ai-watch-videos]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
status: unread
---

> **TL;DR:** The problem with morning research Before market open, I used to spend 45–60 minutes reading news, checking charts, reviewing positions. Most of it was noise. I was making decisions based on whatever I happened to read la…

## What’s new and why it matters
The problem with morning research Before market open, I used to spend 45–60 minutes reading news, checking charts, reviewing positions. Most of it was noise. I was making decisions based on whatever I happened to read last, not a systematic view. Now I run a 9-wave Claude Code pipeline that takes 90 seconds and covers everything. Here's the full architecture. The 9-wave pipeline Each "wave" is a separate Claude API call with a specific role. Running them sequentially means each wave can reference the previous ones. Wave 1: Macro Context Inputs: S&P 500, Nasdaq, VIX, 10Y yield, DXY, oil, recent…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tellmefrankie/how-i-run-a-9-wave-ai-investment-briefing-every-morning-in-90-seconds-full-architecture-3c51

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-06-summarize-1000-documents-with-python-for-under-1-pay-per-use-ai-api]]
- [[2026-03-25-i-automated-my-entire-morning-routine-with-5-python-scripts-heres-the-code]]
- [[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]
- [[2026-03-23-i-ran-56-experiments-to-find-the-best-way-to-make-ai-watch-videos]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
