---
title: 'SQL Date Functions: How to Group by Month Without Losing One'
date: '2026-08-30'
source: https://dev.to/michaelnocito/sql-date-functions-how-to-group-by-month-without-losing-one-2lf4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-21-month-over-month-growth-in-sql-lag-the-growth-formula-and-the-traps]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** By Michael Nocito , data analyst · Published August 8, 2026 By the end of this page you can summarise any table by month in one line, pull the year, month or weekday out of a date, filter a period without accidentally ex…

## What’s new and why it matters
By Michael Nocito , data analyst · Published August 8, 2026 By the end of this page you can summarise any table by month in one line, pull the year, month or weekday out of a date, filter a period without accidentally excluding the last day of it, do date arithmetic that survives month ends, and make a month with no activity appear in your results instead of silently vanishing. It is about twenty-five minutes, and every query and result below was run. Here is what to do today. Take your monthly report and count its rows against the number of months in the period. Four rows for a five-month per…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/sql-date-functions-how-to-group-by-month-without-losing-one-2lf4

## Related notes
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-21-month-over-month-growth-in-sql-lag-the-growth-formula-and-the-traps]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
