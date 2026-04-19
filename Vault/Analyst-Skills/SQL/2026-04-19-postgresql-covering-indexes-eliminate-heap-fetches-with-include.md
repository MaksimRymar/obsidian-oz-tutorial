---
title: 'PostgreSQL Covering Indexes: Eliminate Heap Fetches with INCLUDE'
date: '2026-04-19'
source: https://dev.to/philip_mcclarence_2ef9475/postgresql-covering-indexes-eliminate-heap-fetches-with-include-3lcl
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-21-postgresql-performance-10-queries-youre-writing-wrong-2026-edition]]'
- '[[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
status: unread
---

> **TL;DR:** PostgreSQL Covering Indexes: Eliminate Heap Fetches with INCLUDE You have an index on customer_id . Your query filters by customer_id and selects customer_name and customer_email . PostgreSQL finds the matching rows in t…

## What’s new and why it matters
PostgreSQL Covering Indexes: Eliminate Heap Fetches with INCLUDE You have an index on customer_id . Your query filters by customer_id and selects customer_name and customer_email . PostgreSQL finds the matching rows in the index (fast), then fetches each row from the heap table to get the name and email (slow). Those heap fetches are random I/O operations scattered across the table. On a 100M-row table returning 1,000 rows, that is 1,000 random reads -- and they dominate the query execution time. A covering index eliminates them entirely. How Index Lookups Actually Work Every standard B-tree i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/postgresql-covering-indexes-eliminate-heap-fetches-with-include-3lcl

## Related notes
- [[2026-03-01-sql-joins]]
- [[2026-03-10-joins-window-functions]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-21-postgresql-performance-10-queries-youre-writing-wrong-2026-edition]]
- [[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
