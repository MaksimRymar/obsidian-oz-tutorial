---
title: SQL Window Functions 101
date: '2026-09-11'
source: https://dev.to/young_odhiambo/sql-window-functions-101-5fli
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]'
- '[[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]'
- '[[2026-03-20-postgresqlaggregative-functions]]'
- '[[2026-05-11-postgresql-sql-cheat-sheet-clause-order-joins-aggregates-windows]]'
- '[[2026-06-12-gbase-8a-olap-window-functions-in-practice-ranking-running-totals-mom-and-ratio-analysis]]'
- '[[2026-03-02-mastering-sql-joins-and-window-functions]]'
status: unread
---

> **TL;DR:** Introduction. Window functions in SQL are powerful tools used to perform calculations across a specific "window" of rows related to the current row. Unlike aggregate functions (like SUM() , AVG() , COUNT() ), which colla…

## What’s new and why it matters
Introduction. Window functions in SQL are powerful tools used to perform calculations across a specific "window" of rows related to the current row. Unlike aggregate functions (like SUM() , AVG() , COUNT() ), which collapse multiple rows into a single result, window functions retain individual rows while adding calculated values. They are commonly used for tasks like aggregates, rankings and running totals. The OVER clause defines the “window” of rows for the calculation. It can: PARTITION BY: It divides the data into groups using PARTITION BY. ORDER BY: It specifies the order of rows within e…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/young_odhiambo/sql-window-functions-101-5fli

## Related notes
- [[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]
- [[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]
- [[2026-03-20-postgresqlaggregative-functions]]
- [[2026-05-11-postgresql-sql-cheat-sheet-clause-order-joins-aggregates-windows]]
- [[2026-06-12-gbase-8a-olap-window-functions-in-practice-ranking-running-totals-mom-and-ratio-analysis]]
- [[2026-03-02-mastering-sql-joins-and-window-functions]]
