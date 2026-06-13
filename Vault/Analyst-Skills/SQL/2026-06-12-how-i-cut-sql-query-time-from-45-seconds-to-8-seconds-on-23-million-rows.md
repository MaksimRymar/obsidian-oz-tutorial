---
title: How I Cut SQL Query Time from 45 Seconds to 8 Seconds on 2.3 Million Rows
date: '2026-06-12'
source: https://dev.to/danielnnadi/how-i-cut-sql-query-time-from-45-seconds-to-8-seconds-on-23-million-rows-o3e
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]'
- '[[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-28-before-sql-we-had-to-tell-computers-everything-then-one-idea-changed-that-forever]]'
status: unread
---

> **TL;DR:** I inherited a SQL Server database with 2.3 million rows. Queries took 45 seconds. Users were frustrated. Dashboards timed out. Here is exactly what I did. Step 1: Find the slowest queries I used SQL Server's query store…

## What’s new and why it matters
I inherited a SQL Server database with 2.3 million rows. Queries took 45 seconds. Users were frustrated. Dashboards timed out. Here is exactly what I did. Step 1: Find the slowest queries I used SQL Server's query store to identify the top 10 worst performing queries. Step 2: Check the execution plan Missing index warnings everywhere. Also saw table scans on a 2 million row table. Step 3: Add targeted indexes Created two non-clustered indexes on the most filtered columns. No over-indexing. Just what the queries actually needed. Step 4: Rewrite the worst join One query was joining 6 tables with…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/danielnnadi/how-i-cut-sql-query-time-from-45-seconds-to-8-seconds-on-23-million-rows-o3e

## Related notes
- [[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]
- [[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-28-before-sql-we-had-to-tell-computers-everything-then-one-idea-changed-that-forever]]
