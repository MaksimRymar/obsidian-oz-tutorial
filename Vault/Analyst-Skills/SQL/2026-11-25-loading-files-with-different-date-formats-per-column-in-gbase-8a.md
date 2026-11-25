---
title: Loading Files with Different Date Formats per Column in GBase 8a
date: '2026-11-25'
source: https://dev.to/michaelfv/loading-files-with-different-date-formats-per-column-in-gbase-8a-43bh
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-28-exporting-fixedlength-data-files-in-gbase-8a]]'
- '[[2026-10-28-sql-basics]]'
- '[[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-10-26-parameterized-queries-cant-help-here-6-sqlite-traps-when-an-llm-writes-your-sql]]'
- '[[2026-09-26-python-pandas-dataframe-a-beginners-guide]]'
status: unread
---

> **TL;DR:** GBase 8a, the China-domestically developed MPP analytical database from GBASE, lets you declare a date format when loading data. But what if one file mixes formats — the first date column as year-month-day and the second…

## What’s new and why it matters
GBase 8a, the China-domestically developed MPP analytical database from GBASE, lets you declare a date format when loading data. But what if one file mixes formats — the first date column as year-month-day and the second as month-day-year? The gbase loader handles this per column through table_fields , so the file can go in as-is. Date formats apply to date , datetime , timestamp , and time columns. Table Definition A three-column table where d1 and d2 are both date : gbase > create table td1 ( id int , d1 date , d2 date ) ; Query OK , 0 rows affected ( Elapsed : 00 : 00 : 00.18 ) Sample Data…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelfv/loading-files-with-different-date-formats-per-column-in-gbase-8a-43bh

## Related notes
- [[2026-07-28-exporting-fixedlength-data-files-in-gbase-8a]]
- [[2026-10-28-sql-basics]]
- [[2026-07-21-from-tables-to-insights-a-beginners-journey-into-sql]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-10-26-parameterized-queries-cant-help-here-6-sqlite-traps-when-an-llm-writes-your-sql]]
- [[2026-09-26-python-pandas-dataframe-a-beginners-guide]]
