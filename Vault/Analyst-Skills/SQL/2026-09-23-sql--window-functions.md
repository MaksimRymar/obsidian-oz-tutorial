---
title: SQL- Window Functions
date: '2026-09-23'
source: https://dev.to/maryngure/sql-window-functions-3jid
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]'
- '[[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]'
- '[[2026-09-22-window-functions-vs-aggregate-functions-in-sql-with-examples]]'
- '[[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]'
- '[[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]'
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
status: unread
---

> **TL;DR:** If you've ever needed to calculate a running total, rank rows within groups, or compare a row to the one before it without collapsing your result set with GROUP BY , window functions are the tool for the job. They're one…

## What’s new and why it matters
If you've ever needed to calculate a running total, rank rows within groups, or compare a row to the one before it without collapsing your result set with GROUP BY , window functions are the tool for the job. They're one of the most powerful (and underused) features in SQL, and once they click, you'll reach for them constantly. What Are Window Functions? A window function performs a calculation across a set of rows that are related to the current row, called the "window", without reducing the number of rows returned. This is the key difference from aggregate functions like SUM() or AVG() used…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/maryngure/sql-window-functions-3jid

## Related notes
- [[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]
- [[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]
- [[2026-09-22-window-functions-vs-aggregate-functions-in-sql-with-examples]]
- [[2026-08-12-sql-window-functions-how-to-get-the-top-row-per-group]]
- [[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
