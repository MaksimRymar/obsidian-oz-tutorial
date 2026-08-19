---
title: 'A referee for lip-sync: scoring whether audio and video match with two embedding
  towers'
date: '2026-08-19'
source: https://dev.to/wladradchenko/a-referee-for-lip-sync-scoring-whether-audio-and-video-match-with-two-embedding-towers-49mc
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-01-data-engineering-manager-interview-prep-people-roadmaps-platform-vs-product-trade-offs]]'
- '[[2026-07-27-how-to-build-a-hiring-intent-score-that-doesnt-lie-to-you]]'
- '[[2026-07-19-your-llm-cant-actually-watch-video-heres-the-smallest-fix-mit]]'
- '[[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** You have a talking-head video. The audio and the lips are close, but not exact. Maybe the sound runs three frames ahead. Maybe two people are on screen and you need to know which mouth the voice belongs to. How do you me…

## What’s new and why it matters
You have a talking-head video. The audio and the lips are close, but not exact. Maybe the sound runs three frames ahead. Maybe two people are on screen and you need to know which mouth the voice belongs to. How do you measure that automatically, without a human watching every clip? That is the problem SyncNet solves, and the open-source Wunjo Make repo ships two versions of it. I want to walk through the actual code: how the network is built, how audio turns into the thing the network eats, and how the codebase turns the network's output into a usable offset and a confidence number. Plain vers…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wladradchenko/a-referee-for-lip-sync-scoring-whether-audio-and-video-match-with-two-embedding-towers-49mc

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-01-data-engineering-manager-interview-prep-people-roadmaps-platform-vs-product-trade-offs]]
- [[2026-07-27-how-to-build-a-hiring-intent-score-that-doesnt-lie-to-you]]
- [[2026-07-19-your-llm-cant-actually-watch-video-heres-the-smallest-fix-mit]]
- [[2026-06-20-i-built-a-machine-verifiable-contract-system-for-python-code-heres-how-it-works]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
