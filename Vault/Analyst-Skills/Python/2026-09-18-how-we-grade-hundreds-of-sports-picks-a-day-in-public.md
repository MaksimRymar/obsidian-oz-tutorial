---
title: How we grade hundreds of sports picks a day in public
date: '2026-09-18'
source: https://dev.to/eddie_glush_60e960e585bf8/how-we-grade-hundreds-of-sports-picks-a-day-in-public-3866
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tableau'
- '#tool'
related:
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
status: unread
---

> **TL;DR:** Most sports prediction sites will tell you how good they are. Very few will show you the losses. We decided early that our record would be a public page rather than a marketing claim, and that decision ended up shaping t…

## What’s new and why it matters
Most sports prediction sites will tell you how good they are. Very few will show you the losses. We decided early that our record would be a public page rather than a marketing claim, and that decision ended up shaping the whole pipeline. This is a write-up of how the grading works, what it costs, and what we learned when we pointed the same machinery at the betting market itself. The shape of the pipeline There are four stages, and each one is a table you can query. 1. Publish before the game. A pick only counts if it exists before the event starts. Models run on a schedule, write their selec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/eddie_glush_60e960e585bf8/how-we-grade-hundreds-of-sports-picks-a-day-in-public-3866

## Related notes
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-30-when-to-index-a-table-a-practical-guide-for-analysts]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
