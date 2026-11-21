---
title: Writing SQL basic queries
date: '2026-11-21'
source: https://dev.to/denoh/writing-sql-basic-queries-2ieb
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-21-understanding-sql-window-functions]]'
- '[[2026-10-01-sql-window-functions-explained]]'
- '[[2026-10-25-filtering-data-in-sql-a-beginners-guide-to-where-and-like-and-other-operators]]'
- '[[2026-09-09-getting-started-with-excel-for-data-analytics-from-the-basics-to-cleaning-data]]'
- '[[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
status: unread
---

> **TL;DR:** Before running any queries, I made sure I was working in the correct schema. SET search_path TO hospital; SHOW search_path; This allowed me to reference my tables without having to specify the schema name every time. Onc…

## What’s new and why it matters
Before running any queries, I made sure I was working in the correct schema. SET search_path TO hospital; SHOW search_path; This allowed me to reference my tables without having to specify the schema name every time. Once I confirmed the data was there, I started asking simple analytical questions. How many patients are there by gender? SELECT gender , COUNT (*) AS n_patients FROM patient_records GROUP BY gender; This was my first experience using the COUNT() aggregate function together with GROUP BY . Instead of listing every patient, SQL summarised the data into meaningful groups. Counting p…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/denoh/writing-sql-basic-queries-2ieb

## Related notes
- [[2026-09-21-understanding-sql-window-functions]]
- [[2026-10-01-sql-window-functions-explained]]
- [[2026-10-25-filtering-data-in-sql-a-beginners-guide-to-where-and-like-and-other-operators]]
- [[2026-09-09-getting-started-with-excel-for-data-analytics-from-the-basics-to-cleaning-data]]
- [[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
