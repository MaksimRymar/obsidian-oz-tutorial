---
title: Can You Find Employees Who Joined This Month Using SQL? (Oracle TRUNC & ADD_MONTHS)
date: '2026-11-08'
source: https://dev.to/kailas_warade_d2a15d1ef8a/can-you-find-employees-who-joined-this-month-using-sql-oracle-trunc-addmonths-518c
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#career'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-11-02-sql-challenge-can-you-find-employees-earning-more-than-their-departments-average-salary]]'
- '[[2026-11-03-sql-case-when-how-to-categorize-employee-salaries-into-low-medium-and-high]]'
- '[[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]'
- '[[2026-11-04-sql-challenge-why-is-your-sql-query-still-returning-null]]'
- '[[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]'
- '[[2026-11-02-sql-join-example-how-to-get-employee-names-along-with-department-names]]'
status: unread
---

> **TL;DR:** Your HR manager asks you to find all employees who joined during the current month. You could filter for November 2026, but would you have to change the query when December starts? Can you make it dynamic? employees emp_…

## What’s new and why it matters
Your HR manager asks you to find all employees who joined during the current month. You could filter for November 2026, but would you have to change the query when December starts? Can you make it dynamic? employees emp_id|employee_name|joining_date 101 | Amit | 2026-11-02 102 | Neha | 2026-10-25 103 | Rahul | 2026-11-05 104 | Priya | 2026-09-18 105 | Sneha | 2026-11-08 106 | Karan | 2026-12-01 Your Challenge Write a query to: Find employees who joined this month. Exclude previous and future months. Avoid hardcoding dates. Think before you scroll! The SQL Solution (Oracle) SELECT emp_id, emplo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/can-you-find-employees-who-joined-this-month-using-sql-oracle-trunc-addmonths-518c

## Related notes
- [[2026-11-02-sql-challenge-can-you-find-employees-earning-more-than-their-departments-average-salary]]
- [[2026-11-03-sql-case-when-how-to-categorize-employee-salaries-into-low-medium-and-high]]
- [[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]
- [[2026-11-04-sql-challenge-why-is-your-sql-query-still-returning-null]]
- [[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]
- [[2026-11-02-sql-join-example-how-to-get-employee-names-along-with-department-names]]
