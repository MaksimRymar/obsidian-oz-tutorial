---
title: 'SQL NOT IN vs NOT EXISTS: Handling NULL Values Safely'
date: '2026-10-27'
source: https://dev.to/doogal/sql-not-in-vs-not-exists-handling-null-values-safely-2cl0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-09-06-when-sql-has-nothing-to-say-understanding-nulls]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-10-26-sql-for-beginners]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
status: unread
---

> **TL;DR:** Quick Answer: In SQL, using WHERE column NOT IN (SELECT ...) returns zero rows if the subquery contains a single NULL . This occurs because NOT IN expands to chained != operators joined by AND , and any comparison agains…

## What’s new and why it matters
Quick Answer: In SQL, using WHERE column NOT IN (SELECT ...) returns zero rows if the subquery contains a single NULL . This occurs because NOT IN expands to chained != operators joined by AND , and any comparison against NULL yields UNKNOWN . To avoid silent query failures, always use NOT EXISTS or explicitly filter out NULL values in the subquery. Imagine running a routine query to find customers who have never placed an order, only for the database to return an empty result set—even though you know inactive users exist in your table. You double-check your dataset, confirm that inactive cust…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/doogal/sql-not-in-vs-not-exists-handling-null-values-safely-2cl0

## Related notes
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-09-06-when-sql-has-nothing-to-say-understanding-nulls]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-10-26-sql-for-beginners]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
