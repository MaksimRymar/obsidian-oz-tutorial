---
title: Using dbt to Transform OpenSky Flight Data
date: '2026-08-06'
source: https://dev.to/data_with_jelimo/using-dbt-to-transform-opensky-flight-data-2b51
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
- '[[2026-03-04-the-two-sql-concepts-that-made-me-finally-understand-real-data-joins-window-functions]]'
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-04-19-subqueries-vs-ctes-in-sql-a-complete-guide-for-beginners]]'
- '[[2026-04-13-introduction-to-databases-with-sql]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
status: unread
---

> **TL;DR:** Building an OpenSky Flight Data Pipeline with dbt Core Recently, I built an OpenSky Flight Data Pipeline that ingests aircraft state vectors into PostgreSQL and transforms them into analytics-ready datasets using dbt Cor…

## What’s new and why it matters
Building an OpenSky Flight Data Pipeline with dbt Core Recently, I built an OpenSky Flight Data Pipeline that ingests aircraft state vectors into PostgreSQL and transforms them into analytics-ready datasets using dbt Core . Along the way, I discovered that dbt isn't just about writing SQL, it brings software engineering practices like modularity, testing, documentation, and dependency management to analytics. In this article, I'll walk through how I used dbt, the concepts I learned, and how I organized my project. The Problem The OpenSky Network provides aircraft state vectors containing infor…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/data_with_jelimo/using-dbt-to-transform-opensky-flight-data-2b51

## Related notes
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
- [[2026-03-04-the-two-sql-concepts-that-made-me-finally-understand-real-data-joins-window-functions]]
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-04-19-subqueries-vs-ctes-in-sql-a-complete-guide-for-beginners]]
- [[2026-04-13-introduction-to-databases-with-sql]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
