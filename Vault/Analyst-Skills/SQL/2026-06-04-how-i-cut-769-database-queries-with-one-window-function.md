---
title: How I Cut 769 Database Queries With One Window Function
date: '2026-06-04'
source: https://dev.to/secona/how-i-cut-769-database-queries-with-one-window-function-27oi
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
status: unread
---

> **TL;DR:** From Grafana to Real Performance Gains I noticed in the Grafana dashboard that GET /api/v1/dokter/public/jadwal-dokter was on average taking 1 second even when not under load. To get measurable, reproducible numbers, I b…

## What’s new and why it matters
From Grafana to Real Performance Gains I noticed in the Grafana dashboard that GET /api/v1/dokter/public/jadwal-dokter was on average taking 1 second even when not under load. To get measurable, reproducible numbers, I built a benchmark pipeline and profiled the endpoint systematically. What started as a simple baseline measurement turned into a two-phase optimization effort that eliminated 25% of database round-trips and reduced median response time by 18%. The System The application is a FastAPI + SQLAlchemy + PostgreSQL hospital management backend. The endpoint under study: GET /api/v1/dokt…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/secona/how-i-cut-769-database-queries-with-one-window-function-27oi

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
