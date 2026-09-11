---
title: 'Cheat Sheet: SQL Query Interview Questions'
date: '2026-09-11'
source: https://dev.to/roydevashish/cheat-sheet-sql-query-interview-questions-4e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#sql'
related:
- '[[2026-05-10-sql-interview-questions-for-data-engineering]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-03-08-sql-queries-asked-in-interview]]'
- '[[2026-06-28-data-analysis-sql-asking-the-right-questions-and-using-the-right-tools]]'
- '[[2026-05-11-postgresql-sql-cheat-sheet-clause-order-joins-aggregates-windows]]'
- '[[2026-05-01-subqueries-and-ctes-sql-gets-readable]]'
status: unread
---

> **TL;DR:** 1. Find the Second Highest Salary SELECT MAX ( e1 . salary ) FROM employee e1 WHERE e1 . salary < ( SELECT MAX ( e2 . salary ) FROM employee e2 ); 2. Find the Nth Highest Salary Option 1: Using LIMIT and OFFSET SELECT DI…

## What’s new and why it matters
1. Find the Second Highest Salary SELECT MAX ( e1 . salary ) FROM employee e1 WHERE e1 . salary < ( SELECT MAX ( e2 . salary ) FROM employee e2 ); 2. Find the Nth Highest Salary Option 1: Using LIMIT and OFFSET SELECT DISTINCT e . salary FROM employee e ORDER BY e . salary DESC LIMIT 1 OFFSET n - 1 ; -- Replace 'n-1' with the calculated offset number Option 2: Using a Correlated Subquery SELECT DISTINCT e1 . salary FROM employee e1 WHERE n - 1 = ( -- Replace 'n-1' with your target ranking index SELECT COUNT ( DISTINCT e2 . salary ) FROM employee e2 WHERE e2 . salary > e1 . salary ); 3. Find Du…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/roydevashish/cheat-sheet-sql-query-interview-questions-4e

## Related notes
- [[2026-05-10-sql-interview-questions-for-data-engineering]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-03-08-sql-queries-asked-in-interview]]
- [[2026-06-28-data-analysis-sql-asking-the-right-questions-and-using-the-right-tools]]
- [[2026-05-11-postgresql-sql-cheat-sheet-clause-order-joins-aggregates-windows]]
- [[2026-05-01-subqueries-and-ctes-sql-gets-readable]]
