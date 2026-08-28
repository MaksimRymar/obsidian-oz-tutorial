---
title: 'SQL Execution Order Internals: Why WHERE Fails on Aliases but ORDER BY Succeeds'
date: '2026-08-28'
source: https://dev.to/arpitmbangre/sql-execution-order-internals-why-where-fails-on-aliases-but-order-by-succeeds-1774
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]'
- '[[2026-05-13-understanding-sql-query-structure]]'
- '[[2026-02-22-5-most-asked-sql-interview-questions]]'
- '[[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]'
- '[[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]'
- '[[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]'
status: unread
---

> **TL;DR:** Ever wondered why this query fails in SQL? SELECT department_id , COUNT ( * ) AS emp_count FROM employees WHERE emp_count > 5 -- ❌ Error: Invalid column name 'emp_count' GROUP BY department_id ; The 6-Stage Execution Eng…

## What’s new and why it matters
Ever wondered why this query fails in SQL? SELECT department_id , COUNT ( * ) AS emp_count FROM employees WHERE emp_count > 5 -- ❌ Error: Invalid column name 'emp_count' GROUP BY department_id ; The 6-Stage Execution Engine: FROM & JOIN — Load source tables & evaluate join conditions WHERE — Filter raw rows before grouping GROUP BY — Aggregate rows into buckets HAVING — Filter aggregated buckets SELECT — Compute expressions & column aliases ORDER BY — Sort final output Why It Fails: Because WHERE executes at Stage 2 , the emp_count alias created at Stage 5 (SELECT) does not exist in memory yet…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arpitmbangre/sql-execution-order-internals-why-where-fails-on-aliases-but-order-by-succeeds-1774

## Related notes
- [[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]
- [[2026-05-13-understanding-sql-query-structure]]
- [[2026-02-22-5-most-asked-sql-interview-questions]]
- [[2026-03-25-the-only-sql-cheatsheet-youll-ever-need-with-real-examples]]
- [[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]
- [[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]
