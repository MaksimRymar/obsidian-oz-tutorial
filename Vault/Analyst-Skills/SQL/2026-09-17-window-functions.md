---
title: WINDOW FUNCTIONS
date: '2026-09-17'
source: https://dev.to/super_b8c82b4153dee9fab1c/window-functions-im4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-11-sql-window-functions-101]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]'
- '[[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]'
- '[[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]'
- '[[2026-09-09-sql-functions]]'
status: unread
---

> **TL;DR:** Window function performs a calculation across a set of rows related to the current row The result is calculated per row, but the calculation itself can look at other rows around it. Window function has over() which turns…

## What’s new and why it matters
Window function performs a calculation across a set of rows related to the current row The result is calculated per row, but the calculation itself can look at other rows around it. Window function has over() which turns a normal aggregate function into a window function. in this example you are able to see the average total amount compared to each room type . determines the sequence rows are processed in for that window — essential for ranking functions and for anything _Partition by _ It is usually written inside the over and is used to group data to the thing that you what it be grouped. It…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/super_b8c82b4153dee9fab1c/window-functions-im4

## Related notes
- [[2026-09-11-sql-window-functions-101]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]
- [[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]
- [[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]
- [[2026-09-09-sql-functions]]
