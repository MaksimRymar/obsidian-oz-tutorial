---
title: PostgreSQL global statistics on partitionned table require a manual ANALYZE
date: '2026-03-01'
source: https://dev.to/aws-heroes/postgresql-global-statistics-on-partitionned-table-require-a-manual-analyze-473h
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
- '[[2026-02-27-sql-query-optimization-15-techniques-to-speed-up-your-database-2026]]'
- '[[2026-03-01-advanced-data-retrieval-master-sql-joins-and-window-functions]]'
- '[[2026-02-27-joins-and-window-functions-in-sql]]'
- '[[2026-03-01-understanding-joins-and-window-functions-in-sql]]'
status: unread
---

> **TL;DR:** PostgreSQL auto-analyze collects statistics on tables with rows. For partitioned tables, it excludes the parent as it has no rows by itself. So how does the query planner estimate cardinality when a query spans multiple…

## What’s new and why it matters
PostgreSQL auto-analyze collects statistics on tables with rows. For partitioned tables, it excludes the parent as it has no rows by itself. So how does the query planner estimate cardinality when a query spans multiple partitions? Some statistics are easy to derive: if it knows each partition’s row count, the global count is the total. Column statistics are trickier, especially with the number of distinct values, a key factor to estimate cardinalities with predicates or aggregates. Even with the number of distinct values per partition, it still doesn’t know how much those values overlap acros…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aws-heroes/postgresql-global-statistics-on-partitionned-table-require-a-manual-analyze-473h

## Related notes
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
- [[2026-02-27-sql-query-optimization-15-techniques-to-speed-up-your-database-2026]]
- [[2026-03-01-advanced-data-retrieval-master-sql-joins-and-window-functions]]
- [[2026-02-27-joins-and-window-functions-in-sql]]
- [[2026-03-01-understanding-joins-and-window-functions-in-sql]]
