---
title: PostgreSql(Aggregative Functions)
date: '2026-03-20'
source: https://dev.to/s_mathavi_2fa1e3ea8514f34/postgresqlaggregative-functions-2bf5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-02-22-5-most-asked-sql-interview-questions]]'
- '[[2026-03-18-window-functions-for-call-centre-analytics-a-practical-postgresql-guide]]'
- '[[2026-03-01-from-tables-to-trends-understanding-joins-and-window-functions-in-sql]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-06-joins-and-window-functions-in-sql]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** Aggregative Function: Aggregate functions perform calculations on multiple rows and return a single result. They’re essential for: Summarizing data (e.g., total salary, average marks) Analyzing trends (e.g., highest sale…

## What’s new and why it matters
Aggregative Function: Aggregate functions perform calculations on multiple rows and return a single result. They’re essential for: Summarizing data (e.g., total salary, average marks) Analyzing trends (e.g., highest sales, number of employees per department) Filtering grouped results using HAVING #Common SQL Aggregate Functions: SELECT SUM ( salary ) FROM Employee ; SELECT COUNT ( * ) FROM Employee ; SELECT MAX ( salary ) FROM Employee ; SELECT MIN ( salary ) FROM Employee ; Using Aggregate Functions with GROUP BY: SELECT dept_id , AVG ( salary ) FROM Employee GROUP BY dept_id ; Filtering Grou…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/s_mathavi_2fa1e3ea8514f34/postgresqlaggregative-functions-2bf5

## Related notes
- [[2026-02-22-5-most-asked-sql-interview-questions]]
- [[2026-03-18-window-functions-for-call-centre-analytics-a-practical-postgresql-guide]]
- [[2026-03-01-from-tables-to-trends-understanding-joins-and-window-functions-in-sql]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-06-joins-and-window-functions-in-sql]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
