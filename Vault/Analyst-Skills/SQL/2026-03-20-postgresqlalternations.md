---
title: PostgreSQL(Alternations)
date: '2026-03-20'
source: https://dev.to/s_mathavi_2fa1e3ea8514f34/postgresqlalternations-2en3
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-02-26-beginner-friendly-guide---leetcode-problem-1404-c-python-javascript]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]'
- '[[2026-03-14-schema-risk]]'
- '[[2026-03-10-how-to-auto-fill-sql-query-results-into-a-custom-excel-template-mysqlpostgresqloraclesql-server]]'
- '[[2026-03-15-i-built-the-first-open-source-fp8-linear-solver-in-python-2-3x-faster-than-cublas]]'
status: unread
---

> **TL;DR:** -ALTER TABLE → modify existing table structure. -Operations: add/drop column, change datatype, rename column/table, add/drop constraints. Common ALTER TABLE Operations 1. Add a new column ALTER TABLE Employee ADD COLUMN…

## What’s new and why it matters
-ALTER TABLE → modify existing table structure. -Operations: add/drop column, change datatype, rename column/table, add/drop constraints. Common ALTER TABLE Operations 1. Add a new column ALTER TABLE Employee ADD COLUMN email VARCHAR(100); 2. Drop (remove) a column ALTER TABLE Employee DROP COLUMN email; 3. Change datatype of a column ALTER TABLE Employee ALTER COLUMN salary TYPE NUMERIC(12,2); 4. Rename a column ALTER TABLE Employee RENAME COLUMN name TO full_name; 5. Add a constraint ALTER TABLE Employee ADD CONSTRAINT salary_positive CHECK (salary > 0); 6. Drop a constraint ALTER TABLE Empl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/s_mathavi_2fa1e3ea8514f34/postgresqlalternations-2en3

## Related notes
- [[2026-02-26-beginner-friendly-guide---leetcode-problem-1404-c-python-javascript]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-02-24-countcolumn-vs-count-in-sql-with-inner-left-right-full-join-explained]]
- [[2026-03-14-schema-risk]]
- [[2026-03-10-how-to-auto-fill-sql-query-results-into-a-custom-excel-template-mysqlpostgresqloraclesql-server]]
- [[2026-03-15-i-built-the-first-open-source-fp8-linear-solver-in-python-2-3x-faster-than-cublas]]
