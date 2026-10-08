---
title: Start and End Dates of the Longest Rising Period
date: '2026-10-08'
source: https://dev.to/esproc_spl/start-and-end-dates-of-the-longest-rising-period-3m6j
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-08-22-customer-segmentation-in-sql-with-case-when]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** Problem Description The stock table records the daily closing prices of many stocks, with the fields CODE (stock code), DT (trading date) and CL (closing price). For a given target stock, find the period during which it…

## What’s new and why it matters
Problem Description The stock table records the daily closing prices of many stocks, with the fields CODE (stock code), DT (trading date) and CL (closing price). For a given target stock, find the period during which it rose for the largest number of consecutive days, and give the start date and end date of that period. Source Data stock table (only the records of the target stock CODE = 100046 are listed, in ascending DT order): Expected Result NoRisingDays is the interval number: On 01-02 the closing price rose from 3.89 to 3.93, a continuous rise; on 01-05 it fell from 3.93 to 3.78, which b…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esproc_spl/start-and-end-dates-of-the-longest-rising-period-3m6j

## Related notes
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-08-22-customer-segmentation-in-sql-with-case-when]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
