---
title: Joins In SQL
date: '2026-10-17'
source: https://dev.to/naomi_kwamboka1001/joins-in-sql-36ln
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-04-28-understanding-subquery-and-common-table-expressionsctes]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Introduction-SQL window functions A window function calculates a value for each row using a set of related rows, called the window, and it keeps every input row. GROUP BY is the other aggregate tool: it collapses each gr…

## What’s new and why it matters
Introduction-SQL window functions A window function calculates a value for each row using a set of related rows, called the window, and it keeps every input row. GROUP BY is the other aggregate tool: it collapses each group into one row. Use a window when the hospital still needs the visit, and also needs a rank, a running total, or a comparison with the previous visit. OVER(), PARTITION BY, ORDER BY, and window frames -OVER() is what makes an aggregate or ranking function a window function. Everything inside OVER() defines which rows are visible to the current row. PARTITION BY splits the res…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/naomi_kwamboka1001/joins-in-sql-36ln

## Related notes
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-04-28-understanding-subquery-and-common-table-expressionsctes]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
