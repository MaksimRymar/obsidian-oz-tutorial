---
title: A Full Table Scan Isn’t Always a Mistake
date: '2026-11-13'
source: https://dev.to/tharun_parepalli/a-full-table-scan-isnt-always-a-mistake-3aj4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
status: unread
---

> **TL;DR:** The orders dashboard is slow, so you pull up the Oracle execution plan. There it is: TABLE ACCESS FULL on a million-row table. The query filters on status, and there’s already an index on that column. You run the same qu…

## What’s new and why it matters
The orders dashboard is slow, so you pull up the Oracle execution plan. There it is: TABLE ACCESS FULL on a million-row table. The query filters on status, and there’s already an index on that column. You run the same query with a different status and see an index range scan. It’s tempting to conclude that Oracle missed an obvious optimization on the first run. Now look at what the two queries ask for. One totals nearly every order the system has ever shipped. The other totals a small set of orders held for review. Both have the same SQL shape and use the same filter column, but they ask Oracl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tharun_parepalli/a-full-table-scan-isnt-always-a-mistake-3aj4

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-11-09-sql-where-vs-having-differences-execution-order-and-when-to-use-each-tested-examples]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
