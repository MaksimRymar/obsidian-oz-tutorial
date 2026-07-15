---
title: 'Postgres: force drop a database that is being accessed by other users'
date: '2026-07-15'
source: https://dev.to/philip_mcclarence_2ef9475/postgres-force-drop-a-database-that-is-being-accessed-by-other-users-4k3f
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
status: unread
---

> **TL;DR:** You are trying to drop an old database and Postgres gives you this: ERROR: database "analytics_old" is being accessed by other users DETAIL: There are 2 other sessions using the database. That error is literal. PostgreSQ…

## What’s new and why it matters
You are trying to drop an old database and Postgres gives you this: ERROR: database "analytics_old" is being accessed by other users DETAIL: There are 2 other sessions using the database. That error is literal. PostgreSQL will not drop a database while backend processes are connected to it. On PostgreSQL 13 or newer, the blunt tool is: DROP DATABASE analytics_old WITH ( FORCE ); Run that while connected to some other database, usually postgres : psql -d postgres Do not connect to analytics_old and then try to drop analytics_old . PostgreSQL will quite reasonably refuse. For PostgreSQL 12 and o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/postgres-force-drop-a-database-that-is-being-accessed-by-other-users-4k3f

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
