---
title: JOINS, WINDOW FUNCTIONS, CTEs AND SUBQUERIES
date: '2026-10-19'
source: https://dev.to/lynne_chanzu/joins-window-functions-ctes-and-subqueries-1c2d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-18-sql-concepts---window-functions-joins-common-table-expressions-subqueries]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]'
- '[[2026-03-01-sql-joins]]'
status: unread
---

> **TL;DR:** JOINS Joins are operations used to combine rows from two or more tables based on a related column between them. Types of SQL Joins 1.INNER JOIN It returns only the rows that have matching values in both tables. Applicabl…

## What’s new and why it matters
JOINS Joins are operations used to combine rows from two or more tables based on a related column between them. Types of SQL Joins 1.INNER JOIN It returns only the rows that have matching values in both tables. Applicable when you only need matching records. Example To check the number of visits by each patient: select p . patient_id , p . patient_name , count ( v . visit_id ) as visits_number from patients as p inner join visits as v ON p . patient_id = v . patient_id group by p . patient_id , p . patient_name order by p . patient_id asc ; 2. LEFT JOIN Returns all rows from the left table, pl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lynne_chanzu/joins-window-functions-ctes-and-subqueries-1c2d

## Related notes
- [[2026-10-18-sql-concepts---window-functions-joins-common-table-expressions-subqueries]]
- [[2026-09-09-sql-joins]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]
- [[2026-03-01-sql-joins]]
