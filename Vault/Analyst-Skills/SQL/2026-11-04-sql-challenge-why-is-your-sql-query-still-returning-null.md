---
title: 'SQL Challenge: Why Is Your SQL Query Still Returning NULL?'
date: '2026-11-04'
source: https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-why-is-your-sql-query-still-returning-null-154b
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-02-sql-challenge-can-you-find-employees-earning-more-than-their-departments-average-salary]]'
- '[[2026-11-03-sql-case-when-how-to-categorize-employee-salaries-into-low-medium-and-high]]'
- '[[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]'
- '[[2026-11-02-sql-join-example-how-to-get-employee-names-along-with-department-names]]'
- '[[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]'
- '[[2026-10-19-find-departments-with-an-average-salary-above-the-company-average]]'
status: unread
---

> **TL;DR:** Imagine your manager asks you to prepare a salary report. Some employees have a bonus, while others have no bonus recorded. Your manager wants to see 0 instead of NULL for missing bonuses. You write a query, but the resu…

## What’s new and why it matters
Imagine your manager asks you to prepare a salary report. Some employees have a bonus, while others have no bonus recorded. Your manager wants to see 0 instead of NULL for missing bonuses. You write a query, but the result still shows NULL. What went wrong? Let's look at the data. employees emp_id| name| department| salary| bonus 101 | Amit | IT | 90000| 10000 102 | Priya | IT | 70000| NULL 103 | Rahul | IT | 60000| 5000 104 | Neha | HR | 80000| NULL 105 | Sneha | HR | 85000| 15000 106 | Kiran | HR | 95000| NULL 107 | Meera | Finance | 75000| 8000 108 | Arjun | Finance | 55000| NULL Your chall…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/sql-challenge-why-is-your-sql-query-still-returning-null-154b

## Related notes
- [[2026-11-02-sql-challenge-can-you-find-employees-earning-more-than-their-departments-average-salary]]
- [[2026-11-03-sql-case-when-how-to-categorize-employee-salaries-into-low-medium-and-high]]
- [[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]
- [[2026-11-02-sql-join-example-how-to-get-employee-names-along-with-department-names]]
- [[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]
- [[2026-10-19-find-departments-with-an-average-salary-above-the-company-average]]
