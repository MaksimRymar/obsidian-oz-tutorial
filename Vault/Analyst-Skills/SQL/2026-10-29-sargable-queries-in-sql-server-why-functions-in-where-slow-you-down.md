---
title: 'SARGable Queries in SQL Server: Why Functions in WHERE Slow You Down'
date: '2026-10-29'
source: https://dev.to/lingamsuyambu/sargable-queries-in-sql-server-why-functions-in-where-slow-you-down-35m9
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-09-sql-joins]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
status: unread
---

> **TL;DR:** Originally published at SQL & Cloud Lab . You add the perfect index, run the query, and SQL Server still scans the whole table. One of the most common reasons is a non-SARGable predicate: a WHERE clause written in a way…

## What’s new and why it matters
Originally published at SQL & Cloud Lab . You add the perfect index, run the query, and SQL Server still scans the whole table. One of the most common reasons is a non-SARGable predicate: a WHERE clause written in a way that stops SQL Server from using the index to seek. The fix is usually a small rewrite. What SARGable means SARGable stands for Search ARGument-able . A predicate is SARGable when SQL Server can use it to jump straight to the matching rows in an index (an index seek). If you wrap the indexed column in a function or calculation, SQL Server can no longer search the index for a va…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lingamsuyambu/sargable-queries-in-sql-server-why-functions-in-where-slow-you-down-35m9

## Related notes
- [[2026-09-09-sql-joins]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
