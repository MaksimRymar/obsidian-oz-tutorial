---
title: 'SQL Window Frames Explained: How UNBOUNDED PRECEDING Creates a Running Total'
date: '2026-08-23'
source: https://dev.to/saamiabbaskhan/sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total-m21
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]'
- '[[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]'
- '[[2026-06-30-cte-vs-temporary-tables-in-sql-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** If you have started learning SQL window functions, you have probably seen something like this: SUM ( weight ) OVER ( ORDER BY turn RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) At first glance, the syntax looks int…

## What’s new and why it matters
If you have started learning SQL window functions, you have probably seen something like this: SUM ( weight ) OVER ( ORDER BY turn RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW ) At first glance, the syntax looks intimidating. What exactly is a frame ? What does UNBOUNDED PRECEDING mean? Why does CURRENT ROW not mean that the calculation only considers the current row? And how does this produce: 10 30 60 100 instead of just giving the total 100 everywhere? I had the same confusion, so let's break it down from first principles and then use LeetCode 1204 — Last Person to Fit in the Bus as a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/saamiabbaskhan/sql-window-frames-explained-how-unbounded-preceding-creates-a-running-total-m21

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]
- [[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]
- [[2026-06-30-cte-vs-temporary-tables-in-sql-which-one-should-you-use]]
