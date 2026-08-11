---
title: PostgreSQL(part-5)
date: '2026-08-11'
source: https://dev.to/kiruthiga_05/postgresqlpart-5-1be6
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-03-01-sql-joins]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-03-02-joins-and-window-functions-in-sql]]'
- '[[2026-05-23-sql-union-vs-union-all-vs-intersect-vs-except]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
status: unread
---

> **TL;DR:** UNION Used to combine two or more rows and removes duplicates select empid from employee union select empid from team ; empid 118 123 101 124 111 UNION ALL Used to combine two or more rows and remains duplicates select e…

## What’s new and why it matters
UNION Used to combine two or more rows and removes duplicates select empid from employee union select empid from team ; empid 118 123 101 124 111 UNION ALL Used to combine two or more rows and remains duplicates select empid from employee union all select empid from team ; empid 101 123 101 124 118 101 111 118 101 123 124 INTERSECT Get the values that are common to both tables select empid from employee intersect select empid from team ; empid 101 124 118 123 EXCEPT Gets the values that are in the first query but NOT in the second query select empid from employee except select empid from team…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kiruthiga_05/postgresqlpart-5-1be6

## Related notes
- [[2026-03-01-sql-joins]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-03-10-joins-window-functions]]
- [[2026-03-02-joins-and-window-functions-in-sql]]
- [[2026-05-23-sql-union-vs-union-all-vs-intersect-vs-except]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
