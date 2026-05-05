---
title: How I was introduced to SQL window function
date: '2026-05-04'
source: https://dev.to/dhairya_pandya/how-i-was-introduced-to-sql-window-function-292m
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-18-window-functions-for-call-centre-analytics-a-practical-postgresql-guide]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-11-why-sum-over-order-by-sometimes-feels-wrong-a-practical-guide-to-sql-window-frames]]'
status: unread
---

> **TL;DR:** I was called at my firm for having to create a analytics dashboard for a multiTenet CRM dashboard where the magnitude of rows were in thousands and the efficiency i could not blame postgress or servers I had to figure ou…

## What’s new and why it matters
I was called at my firm for having to create a analytics dashboard for a multiTenet CRM dashboard where the magnitude of rows were in thousands and the efficiency i could not blame postgress or servers I had to figure out how to index, query and cache the data. The business questions were something like this Give the sales agents aggregated sales data from the month of January, till the current month in waterfall structure so that the numbers are aggregated in that order. Ranking the sales agents on the basis of their quaterly performance to reward the winner on the basis of how much sales the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dhairya_pandya/how-i-was-introduced-to-sql-window-function-292m

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-18-window-functions-for-call-centre-analytics-a-practical-postgresql-guide]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-11-why-sum-over-order-by-sometimes-feels-wrong-a-practical-guide-to-sql-window-frames]]
