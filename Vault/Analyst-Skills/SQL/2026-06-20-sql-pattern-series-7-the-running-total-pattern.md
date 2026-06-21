---
title: 'SQL Pattern Series #7: The Running Total Pattern'
date: '2026-06-20'
source: https://dev.to/baldwin_apps/sql-pattern-series-7-the-running-total-pattern-5af9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-06-09-sql-pattern-series-4-the-moving-sum-pattern]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-05-30-sql-pattern-series-1-the-presence-pattern]]'
- '[[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]'
- '[[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]'
- '[[2026-06-06-sql-pattern-series-3-the-missing-data-pattern]]'
status: unread
---

> **TL;DR:** Seeing how values build over time SQL Pattern Series #7 of 21 A collection of practical SQL patterns that help developers recognize common solutions to recurring database problems. What You'll Learn In this article you'l…

## What’s new and why it matters
Seeing how values build over time SQL Pattern Series #7 of 21 A collection of practical SQL patterns that help developers recognize common solutions to recurring database problems. What You'll Learn In this article you'll learn: What a running total is How SUM() works as a window function Why ORDER BY matters inside OVER() When to use running totals in reports and dashboards Most reports show totals. But sometimes a single total is not enough. You may also need to see how that total builds over time. For example: What were cumulative sales by day? or: How did the balance grow after each transa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/baldwin_apps/sql-pattern-series-7-the-running-total-pattern-5af9

## Related notes
- [[2026-06-09-sql-pattern-series-4-the-moving-sum-pattern]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-05-30-sql-pattern-series-1-the-presence-pattern]]
- [[2026-04-27-sql-group-by-having-the-beginners-guide-to-summarizing-data-like-a-pro]]
- [[2026-04-19-sql-deep-dive-subqueries-vs-ctes-which-one-should-you-use]]
- [[2026-06-06-sql-pattern-series-3-the-missing-data-pattern]]
