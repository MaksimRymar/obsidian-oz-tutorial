---
title: PostgreSql - Relationships(joins)
date: '2026-03-20'
source: https://dev.to/s_mathavi_2fa1e3ea8514f34/postgresql-relationshipsjoins-4c6o
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]'
- '[[2026-03-03-mastering-joins-and-window-functions-in-sql]]'
- '[[2026-03-17-joins-and-window-functions-in-sql]]'
- '[[2026-03-01-a-simple-guide-to-joins-and-window-functions]]'
- '[[2026-03-02-sql-joins-explained-case-example]]'
- '[[2026-03-01-sql-joins]]'
status: unread
---

> **TL;DR:** How to connect Two Database in innerjoin? 1.Most Important step is Create Extension. CREATE EXTENSION dblink; Example: SELECT e . name , d . dept_name FROM Employee e JOIN dblink ( 'dbname=department_db' , 'SELECT dept_i…

## What’s new and why it matters
How to connect Two Database in innerjoin? 1.Most Important step is Create Extension. CREATE EXTENSION dblink; Example: SELECT e . name , d . dept_name FROM Employee e JOIN dblink ( 'dbname=department_db' , 'SELECT dept_id, dept_name FROM Department' ) AS d ( dept_id INT , dept_name TEXT ) ON e . department_id = d . dept_id ; Same Database: Example: SELECT e.name, d.dept_name FROM Employee e INNER JOIN Department d ON e.dept_id = d.dept_id; Now we Start , Tables Setup Employee table: emp_id name dept_id 1 Udaya 2 2 Mathavi 3 3 Kumar 1 4 Meena NULL Department table: dept_id dept_name 1 IT 2 Fina…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/s_mathavi_2fa1e3ea8514f34/postgresql-relationshipsjoins-4c6o

## Related notes
- [[2026-03-02-simple-guides-to-table-joins-and-window-functions-in-sql]]
- [[2026-03-03-mastering-joins-and-window-functions-in-sql]]
- [[2026-03-17-joins-and-window-functions-in-sql]]
- [[2026-03-01-a-simple-guide-to-joins-and-window-functions]]
- [[2026-03-02-sql-joins-explained-case-example]]
- [[2026-03-01-sql-joins]]
