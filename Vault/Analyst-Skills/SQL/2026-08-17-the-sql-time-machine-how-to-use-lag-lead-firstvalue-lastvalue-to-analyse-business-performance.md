---
title: 'The SQL Time Machine: How to use LAG(), LEAD(), FIRST_VALUE() & LAST_VALUE()
  to analyse business performance'
date: '2026-08-17'
source: https://dev.to/rose_odiwuor/the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-3942
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
status: unread
---

> **TL;DR:** Introduction SQL window functions perform calculations across a set of rows related to the current row, without collapsing results into a single aggregated row. They are defined using the OVER() clause, which can include…

## What’s new and why it matters
Introduction SQL window functions perform calculations across a set of rows related to the current row, without collapsing results into a single aggregated row. They are defined using the OVER() clause, which can include PARTITION BY (to group rows) and ORDER BY (to define row order within each group). Basic Syntax: SELECT column_name1 , window_function ( column_name2 ) OVER ([ PARTITION BY column_name3 ] [ ORDER BY column_name4 ]) AS new_column FROM table_name ; Unlike standard aggregates, window functions retain individual rows while adding calculated values such as rankings, running totals,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rose_odiwuor/the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-3942

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
