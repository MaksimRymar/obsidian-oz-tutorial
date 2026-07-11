---
title: Laravel’s withCount vs a Manual Join — The Real Query Difference
date: '2026-07-10'
source: https://levelup.gitconnected.com/laravels-withcount-vs-a-manual-join-the-real-query-difference-f9b5c05cb231?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-05-01-sql-coding-order-vs-execution-order-why-most-devs-write-queries-wrong]]'
- '[[2026-03-19-the-most-powerful-language-youve-been-running-from]]'
- '[[2026-05-26-subquery-vs-join-vs-exists-which-one-should-you-actually-use]]'
- '[[2026-05-18-pipeline]]'
- '[[2026-04-13-inner-join-vs-left-join-in-sql-whats-the-difference]]'
- '[[2026-06-15-money-is-a-ledger-not-a-balance]]'
status: unread
---

> **TL;DR:** “withCount is slow, use a JOIN!” Replace it → query gets slower. Add another count → wrong numbers. The Laravel SQL truth. Continue reading on Level Up Coding »

## What’s new and why it matters
“withCount is slow, use a JOIN!” Replace it → query gets slower. Add another count → wrong numbers. The Laravel SQL truth. Continue reading on Level Up Coding »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://levelup.gitconnected.com/laravels-withcount-vs-a-manual-join-the-real-query-difference-f9b5c05cb231?source=rss------sql-5

## Related notes
- [[2026-05-01-sql-coding-order-vs-execution-order-why-most-devs-write-queries-wrong]]
- [[2026-03-19-the-most-powerful-language-youve-been-running-from]]
- [[2026-05-26-subquery-vs-join-vs-exists-which-one-should-you-actually-use]]
- [[2026-05-18-pipeline]]
- [[2026-04-13-inner-join-vs-left-join-in-sql-whats-the-difference]]
- [[2026-06-15-money-is-a-ledger-not-a-balance]]
