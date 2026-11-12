---
title: 'SQL Window Functions in 5 Minutes: ROW_NUMBER, RANK, Running Totals, Top N'
date: '2026-11-12'
source: https://dev.to/refactorly/sql-window-functions-in-5-minutes-rownumber-rank-running-totals-top-n-4k67
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#sql'
- '#tool'
related:
- '[[2026-10-17-joins-in-sql]]'
- '[[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]'
- '[[2026-11-04-sql-window-functions-clicked-when-i-stopped-collapsing-rows]]'
- '[[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]'
- '[[2026-05-29-part-14-window-functions-ninja-mode]]'
- '[[2026-10-22-5-sql-window-function-exercises-taken-from-real-business-problems]]'
status: unread
---

> **TL;DR:** Running totals, rankings, "top 3 per category": without window functions these need messy self-joins and subqueries. With them, each one is a single line. Here's everything you need, with real results. I ran every query…

## What’s new and why it matters
Running totals, rankings, "top 3 per category": without window functions these need messy self-joins and subqueries. With them, each one is a single line. Here's everything you need, with real results. I ran every query in SQLite and PostgreSQL. Video version: The sample data -- employees -- name dept salary -- Ann Eng 120 -- Bob Eng 100 -- Cara Eng 100 -- Dan Eng 80 -- Eve Sales 90 -- Finn Sales 75 -- Gia Sales 60 The big idea: GROUP BY collapses rows, OVER keeps them GROUP BY dept squashes each department into one row. A window function , written with OVER (...) , calculates across a group o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refactorly/sql-window-functions-in-5-minutes-rownumber-rank-running-totals-top-n-4k67

## Related notes
- [[2026-10-17-joins-in-sql]]
- [[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]
- [[2026-11-04-sql-window-functions-clicked-when-i-stopped-collapsing-rows]]
- [[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]
- [[2026-05-29-part-14-window-functions-ninja-mode]]
- [[2026-10-22-5-sql-window-function-exercises-taken-from-real-business-problems]]
