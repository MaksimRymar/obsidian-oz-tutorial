---
title: I Tested PostgreSQL on 5 Million Rows, Here’s What Actually Makes Queries Fast
date: '2026-04-17'
source: https://dev.to/faizanfirdousi/how-postgresql-actually-reads-your-data-sequential-scan-vs-index-scan-vs-index-only-scan-ah7
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]'
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-18-how-do-postgresql-indices-work-anyways]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
status: unread
---

> **TL;DR:** when you run a query on a large table in postgres, the performance difference is rarely about the query syntax, it’s about how postgres chooses to access the data underneath to understand this better, i tested on my loca…

## What’s new and why it matters
when you run a query on a large table in postgres, the performance difference is rarely about the query syntax, it’s about how postgres chooses to access the data underneath to understand this better, i tested on my local machine the same query on a table with 5 million rows under different execution strategies and the results were drastically different What Really Happens When PostgreSQL Scans Your Entire Table when you do the query select * from table_name where id = 17 postgres can do a full sequential scan if there is no usable index or if it thinks scanning everything is cheaper. so what…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/faizanfirdousi/how-postgresql-actually-reads-your-data-sequential-scan-vs-index-scan-vs-index-only-scan-ah7

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-18-how-do-postgresql-indices-work-anyways]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
