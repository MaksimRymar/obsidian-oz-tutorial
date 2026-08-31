---
title: 'Running Total in SQL: The Window Frame That Decides the Answer'
date: '2026-08-31'
source: https://dev.to/michaelnocito/running-total-in-sql-the-window-frame-that-decides-the-answer-2g7j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#presentations'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
status: unread
---

> **TL;DR:** By Michael Nocito , data analyst · Published August 8, 2026 By the end of this page you can add a cumulative column to any ordered result, write the frame clause that says exactly which rows are being added, run separate…

## What’s new and why it matters
By Michael Nocito , data analyst · Published August 8, 2026 By the end of this page you can add a cumulative column to any ordered result, write the frame clause that says exactly which rows are being added, run separate totals for each group in one pass, turn the same shape into a moving average, and check the whole thing with one comparison. It is about twenty-five minutes, and every result below was run. Here is what to do today. Find your running-total query and look for the words ROWS BETWEEN . If they are not there, you are using the default frame, and on any column with repeated values…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/michaelnocito/running-total-in-sql-the-window-frame-that-decides-the-answer-2g7j

## Related notes
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
