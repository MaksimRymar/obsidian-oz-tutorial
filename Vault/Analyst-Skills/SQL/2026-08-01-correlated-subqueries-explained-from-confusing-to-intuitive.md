---
title: 'Correlated Subqueries Explained: From Confusing to Intuitive'
date: '2026-08-01'
source: https://dev.to/saamiabbaskhan/correlated-subqueries-explained-from-confusing-to-intuitive-32jn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-05-01-subqueries-and-ctes-sql-gets-readable]]'
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
status: unread
---

> **TL;DR:** Hey everyone! 👋 It's been a while since I posted here. Over the past few days, I've been revisiting SQL from the ground up—not just solving problems, but understanding why different SQL concepts exist and when they shoul…

## What’s new and why it matters
Hey everyone! 👋 It's been a while since I posted here. Over the past few days, I've been revisiting SQL from the ground up—not just solving problems, but understanding why different SQL concepts exist and when they should be used. One topic that confused me (and many beginners) was correlated subqueries . You may have seen queries like this: SELECT ... FROM table1 t1 WHERE EXISTS ( SELECT * FROM table2 t2 WHERE t2 . id = t1 . id ); and wondered: How is the inner query accessing columns from the outer query? When does the inner query execute? How is this different from a normal subquery? In thi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/saamiabbaskhan/correlated-subqueries-explained-from-confusing-to-intuitive-32jn

## Related notes
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-05-01-subqueries-and-ctes-sql-gets-readable]]
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
