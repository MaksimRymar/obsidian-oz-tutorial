---
title: PostgreSQL ALTER
date: '2026-08-27'
source: https://dev.to/kamalesh_ar_6252544786997/postgresql-alter-2d15
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-08-11-sql-update-statement-how-to-modify-existing-data-in-a-database]]'
- '[[2026-04-15-understanding-ddl-and-dml-sql-concepts]]'
- '[[2026-06-18-oracle-ora-00922-error-causes-and-solutions-complete-guide]]'
- '[[2026-03-26-alter-table]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-04-13-first-week-reflections-on-sql]]'
status: unread
---

> **TL;DR:** ALTER TABLE: We want to add a column named color to our cars table. When adding columns we must also specify the data type of the column. Our color column will be a string, and we specify string types with the VARCHAR ke…

## What’s new and why it matters
ALTER TABLE: We want to add a column named color to our cars table. When adding columns we must also specify the data type of the column. Our color column will be a string, and we specify string types with the VARCHAR keyword. we also want to restrict the number of characters to 25 postgres =# ALTER TABLE car ADD color VARCHAR ( 25 ); ALTER TABLE UPDATE TABLE: The UPDATE statement is used to modify the value(s) in existing records in a table. postgres =# UPDATE car SET color = 'red' WHERE brand = 'Volvo' ; UPDATE 1 postgres =# select * from car ; brand | model | year | color --------+---------…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kamalesh_ar_6252544786997/postgresql-alter-2d15

## Related notes
- [[2026-08-11-sql-update-statement-how-to-modify-existing-data-in-a-database]]
- [[2026-04-15-understanding-ddl-and-dml-sql-concepts]]
- [[2026-06-18-oracle-ora-00922-error-causes-and-solutions-complete-guide]]
- [[2026-03-26-alter-table]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-04-13-first-week-reflections-on-sql]]
