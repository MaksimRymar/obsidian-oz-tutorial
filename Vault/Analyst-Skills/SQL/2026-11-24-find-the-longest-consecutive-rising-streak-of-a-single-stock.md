---
title: Find the Longest Consecutive Rising Streak of a Single Stock
date: '2026-11-24'
source: https://dev.to/esproc_spl/find-the-longest-consecutive-rising-streak-of-a-single-stock-392
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-10-08-start-and-end-dates-of-the-longest-rising-period]]'
- '[[2026-10-20-sqlazy-find-strings-with-5-or-more-consecutive-alphabetical-letters]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
status: unread
---

> **TL;DR:** Problem Description The table stock records the daily closing prices of many stocks, with the fields CODE (stock code), DT (trading date) and CL (closing price). For a given stock (100046 in this example), find the numbe…

## What’s new and why it matters
Problem Description The table stock records the daily closing prices of many stocks, with the fields CODE (stock code), DT (trading date) and CL (closing price). For a given stock (100046 in this example), find the number of days in its longest consecutive rising period. A consecutive rise here means the closing price does not fall back from one day to the next. Source Data The source table is large, so only part of the records are listed below: Expected Result Only one value, the maximum number of consecutive rising days: 4 On 01-02 the closing price rose from 3.89 to 3.93, a consecutive rise…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esproc_spl/find-the-longest-consecutive-rising-streak-of-a-single-stock-392

## Related notes
- [[2026-10-08-start-and-end-dates-of-the-longest-rising-period]]
- [[2026-10-20-sqlazy-find-strings-with-5-or-more-consecutive-alphabetical-letters]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-03-08-understanding-group-by-in-sql]]
