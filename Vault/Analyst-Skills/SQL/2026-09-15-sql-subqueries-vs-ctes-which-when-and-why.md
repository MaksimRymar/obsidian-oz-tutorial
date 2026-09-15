---
title: 'SQL Subqueries vs CTEs: Which, When and Why'
date: '2026-09-15'
source: https://dev.to/sguantai/sql-subqueries-vs-ctes-which-when-and-why-418h
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]'
- '[[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]'
- '[[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** Inside you there are two wolves, one wants to use a subquery and the other prefers a CTE. Both are SQL developers, and neither will stop arguing about which one is better. Today we will discuss which wolf to feed (depend…

## What’s new and why it matters
Inside you there are two wolves, one wants to use a subquery and the other prefers a CTE. Both are SQL developers, and neither will stop arguing about which one is better. Today we will discuss which wolf to feed (depending on the situation). What Are Subqueries? A subquery is a query nested inside another query. It usually runs first and its result gets used by the outer query either as a value to compare against, a list to check against or a table to select from. Subqueries can show up in a few places: the WHERE clause, the SELECT list, the FROM clause, or even inside another subquery. The '…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sguantai/sql-subqueries-vs-ctes-which-when-and-why-418h

## Related notes
- [[2026-04-30-subqueries-vs-ctes-in-sql-master-nested-queries-and-write-cleaner-smarter-code]]
- [[2026-09-10-subqueries-ctes-breaking-complex-queries-into-steps]]
- [[2026-04-22-understanding-subqueries-vs-ctes-in-sql-with-examples]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
