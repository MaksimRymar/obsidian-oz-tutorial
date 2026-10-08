---
title: 'SQL: Find the Top 2 Orders for Every Customer Using Window Functions'
date: '2026-10-08'
source: https://dev.to/kailas_warade_d2a15d1ef8a/sql-find-the-top-2-orders-for-every-customer-using-window-functions-1dnp
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-09-sql-functions]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-09-11-sql-subqueries-ctes-write-smarter-cleaner-queries]]'
- '[[2026-08-07-stop-learning-data-analytics-tools-in-isolation-build-this-one-project-instead]]'
status: unread
---

> **TL;DR:** SQL: Find the Top 2 Orders for Every Customer Using Window Functions One SQL problem I often see people get wrong is: How do you find the top 2 orders for every customer? Finding the top 2 orders overall is easy. The int…

## What’s new and why it matters
SQL: Find the Top 2 Orders for Every Customer Using Window Functions One SQL problem I often see people get wrong is: How do you find the top 2 orders for every customer? Finding the top 2 orders overall is easy. The interesting part is “for every customer.” Let’s take a simple example. Sample Data CID| OID| AMT C001| 1001| 12000 C001| 1002| 7500 C001| 1003| 9000 C002| 1004| 15000 C002| 1005| 6000 C002| 1006| 11000 C003| 1007| 5000 C003| 1008| 18000 C003| 1009| 12000 We want the top 2 orders for each customer based on order amount. The expected result is: CID| OID| AMT C001| 1001| 12000 C001|…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/sql-find-the-top-2-orders-for-every-customer-using-window-functions-1dnp

## Related notes
- [[2026-09-09-sql-functions]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-09-11-sql-subqueries-ctes-write-smarter-cleaner-queries]]
- [[2026-08-07-stop-learning-data-analytics-tools-in-isolation-build-this-one-project-instead]]
