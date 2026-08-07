---
title: Find Your Worst Postgres Query in 15 Minutes with pg_stat_statements
date: '2026-08-06'
source: https://dev.to/mukesh_13/find-your-worst-postgres-query-in-15-minutes-with-pgstatstatements-5foj
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-02-debugging-postgresql-performance]]'
- '[[2026-06-10-your-database-is-fast-your-queries-are-slow]]'
- '[[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]'
status: unread
---

> **TL;DR:** If your app has a slow endpoint and you're staring at application logs trying to guess which query is the culprit, stop. Postgres already tracked every query it ran, how long each one took, and how often — you just haven…

## What’s new and why it matters
If your app has a slow endpoint and you're staring at application logs trying to guess which query is the culprit, stop. Postgres already tracked every query it ran, how long each one took, and how often — you just haven't asked it yet. pg_stat_statements is a built-in extension that turns "something feels slow" into "this exact query, called 40,000 times a day, is burning 60% of your database's CPU." Fifteen minutes from now you'll have a ranked list of your worst offenders and a fix for the top one. Step 1: Turn it on (2 minutes) pg_stat_statements ships with Postgres but isn't loaded by def…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mukesh_13/find-your-worst-postgres-query-in-15-minutes-with-pgstatstatements-5foj

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-02-debugging-postgresql-performance]]
- [[2026-06-10-your-database-is-fast-your-queries-are-slow]]
- [[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]
