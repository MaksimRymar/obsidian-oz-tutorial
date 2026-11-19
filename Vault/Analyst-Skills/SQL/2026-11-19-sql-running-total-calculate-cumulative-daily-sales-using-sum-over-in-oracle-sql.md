---
title: 'SQL Running Total: Calculate Cumulative Daily Sales Using SUM() OVER() in
  Oracle SQL'
date: '2026-11-19'
source: https://dev.to/kailas_warade_d2a15d1ef8a/sql-running-total-calculate-cumulative-daily-sales-using-sum-over-in-oracle-sql-3e6k
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-17-joins-in-sql]]'
- '[[2026-09-17-window-functions]]'
- '[[2026-10-18-mastering-sql-window-functions-joins-ctes-and-subqueries]]'
- '[[2026-09-21-understanding-sql-window-functions]]'
- '[[2026-10-22-5-sql-window-function-exercises-taken-from-real-business-problems]]'
- '[[2026-09-15-sql-joins-explained]]'
status: unread
---

> **TL;DR:** When working with sales data, you may come across a requirement to calculate how much revenue a business has generated up to a particular date. For example, a sales manager may want to see daily sales along with the tota…

## What’s new and why it matters
When working with sales data, you may come across a requirement to calculate how much revenue a business has generated up to a particular date. For example, a sales manager may want to see daily sales along with the total sales accumulated from the beginning of the month. This is called a Running Total or Cumulative Sum. In SQL, we can calculate it easily using the "SUM()" window function with the "OVER()" clause. In this SQL Challenge #105, let's see how to calculate a running total using Oracle SQL. The Sales Table Assume we have a table named "sales" containing daily sales information. sale…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/sql-running-total-calculate-cumulative-daily-sales-using-sum-over-in-oracle-sql-3e6k

## Related notes
- [[2026-10-17-joins-in-sql]]
- [[2026-09-17-window-functions]]
- [[2026-10-18-mastering-sql-window-functions-joins-ctes-and-subqueries]]
- [[2026-09-21-understanding-sql-window-functions]]
- [[2026-10-22-5-sql-window-function-exercises-taken-from-real-business-problems]]
- [[2026-09-15-sql-joins-explained]]
