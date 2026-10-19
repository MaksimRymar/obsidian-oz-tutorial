---
title: Window Functions, Joins, CTEs and Subqueries
date: '2026-10-19'
source: https://dev.to/victoria_fa8/window-functions-joins-ctes-and-subqueries-59n9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-05-11-inner-vs-outer-joins-the-two-fundamental-join-types-in-sql]]'
- '[[2026-10-17-joins-in-sql]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-05-29-part-10-subqueries-and-ctes]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
status: unread
---

> **TL;DR:** Once you've got filtering and grouping down, SQL starts asking harder questions. Which doctor handles the most visits? Which department has the most unpaid bills? You can't answer those with a single SELECT ... WHERE . Y…

## What’s new and why it matters
Once you've got filtering and grouping down, SQL starts asking harder questions. Which doctor handles the most visits? Which department has the most unpaid bills? You can't answer those with a single SELECT ... WHERE . You need window functions, joins, CTEs and subqueries. I worked through all four on a real dataset: 672 visits from a mock data: Hospital Health Records workbook, split into a star schema ( visits_fact plus dim_patients , dim_doctors and dim_departments ). Everything below is PostgreSQL. Window functions: keep the rows, add the context GROUP BY squashes rows together. A window f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/victoria_fa8/window-functions-joins-ctes-and-subqueries-59n9

## Related notes
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-05-11-inner-vs-outer-joins-the-two-fundamental-join-types-in-sql]]
- [[2026-10-17-joins-in-sql]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-05-29-part-10-subqueries-and-ctes]]
- [[2026-04-21-sql-window-functions-and-ctes]]
