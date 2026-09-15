---
title: 'SQL Is Surviving, Franklin: Now Rows Are Competing'
date: '2026-09-15'
source: https://dev.to/ms_njenga/sql-is-surviving-franklin-now-rows-are-competing-4kma
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** If you have survived SELECT , WHERE , JOIN , GROUP BY , subqueries, and CTEs, congratulations. Franklin has now discovered window functions . And window functions are where SQL starts doing something that feels a little…

## What’s new and why it matters
If you have survived SELECT , WHERE , JOIN , GROUP BY , subqueries, and CTEs, congratulations. Franklin has now discovered window functions . And window functions are where SQL starts doing something that feels a little suspicious. They can look at other rows without collapsing the rows you already have . You can have: An employee's salary and their department's average salary A student's score and their rank A month's sales and the running total Today's sales and yesterday's sales All in the same result. Franklin has questions. "Wait. SQL can look at other rows and still give me my original r…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ms_njenga/sql-is-surviving-franklin-now-rows-are-competing-4kma

## Related notes
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
