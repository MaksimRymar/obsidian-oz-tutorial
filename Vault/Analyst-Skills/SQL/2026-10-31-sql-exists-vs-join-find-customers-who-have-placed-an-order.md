---
title: 'SQL EXISTS vs JOIN: Find Customers Who Have Placed an Order'
date: '2026-10-31'
source: https://dev.to/kailas_warade_d2a15d1ef8a/sql-exists-vs-join-find-customers-who-have-placed-an-order-149d
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]'
- '[[2026-10-27-sql-not-in-vs-not-exists-handling-null-values-safely]]'
- '[[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
status: unread
---

> **TL;DR:** SQL EXISTS vs JOIN: Find Customers Who Have Placed an Order Imagine your manager asks you to find all customers who have placed at least one order. You have two tables. Some customers have placed multiple orders, while o…

## What’s new and why it matters
SQL EXISTS vs JOIN: Find Customers Who Have Placed an Order Imagine your manager asks you to find all customers who have placed at least one order. You have two tables. Some customers have placed multiple orders, while others haven't placed any. How would you write this query? Let's look at the data. Sample Tables customers cust_id| name| city 101| Amit| Pune 102| Neha| Mumbai 103| Rahul| Pune 104| Priya| Delhi orders order_id| cust_id| amount 501| 101| 5000 502| 101| 3000 503| 103| 7000 504| 103| 2000 Notice that Amit and Rahul have placed two orders each. Neha and Priya haven't placed any or…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/sql-exists-vs-join-find-customers-who-have-placed-an-order-149d

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]
- [[2026-10-27-sql-not-in-vs-not-exists-handling-null-values-safely]]
- [[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]
- [[2026-03-01-sql-joins]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
