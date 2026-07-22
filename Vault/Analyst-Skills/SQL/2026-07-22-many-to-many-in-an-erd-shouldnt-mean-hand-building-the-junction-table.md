---
title: Many-to-Many in an ERD Shouldn't Mean Hand-Building the Junction Table
date: '2026-07-22'
source: https://dev.to/tbson87/many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table-4fj1
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-06-15-how-to-choose-the-right-sql-database-for-your-project]]'
- '[[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Relational databases cannot store a many-to-many relationship directly, so most ERD tools make you hand-…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Relational databases cannot store a many-to-many relationship directly, so most ERD tools make you hand-build the junction table - Microsoft documents six manual steps for one relationship. In Schemity, you drag between the two entities and pick N:N; the junction table appears with its foreign keys, composite primary key, and convention-following name already in place, as a real table you can rename and extend. One refinement: keep that composite primary key when both parents liv…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table-4fj1

## Related notes
- [[2026-07-18-the-data-dictionary-should-live-in-the-erd-not-in-a-spreadsheet]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-06-15-how-to-choose-the-right-sql-database-for-your-project]]
- [[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
