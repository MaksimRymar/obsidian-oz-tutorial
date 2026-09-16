---
title: SQL Window Functions Made Simple
date: '2026-09-16'
source: https://dev.to/alex_murithi/sql-window-functions-made-simple-4ni9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]'
- '[[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]'
- '[[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]'
- '[[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]'
- '[[2026-05-22-sql-window-functions-for-data-engineering-interviews-rownumber-rank-laglead-and-running-totals]]'
- '[[2026-09-15-window-functions-in-sql]]'
status: unread
---

> **TL;DR:** When you need to calculate averages, ranks, or totals without collapsing rows, SQL’s window functions are your best friend. They let you perform calculations across related rows while keeping every original record visibl…

## What’s new and why it matters
When you need to calculate averages, ranks, or totals without collapsing rows, SQL’s window functions are your best friend. They let you perform calculations across related rows while keeping every original record visible - perfect for analytics, leaderboards, and comparisons. Exploring window functions using a sample Safari Trips database . Safari Trips Database Schema Working with two tables: drivers and trips . drivers driver_id driver_name city 1 James Kariuki Nairobi 2 Mary Achieng Kisumu 3 Peter Otieno Mombasa 4 Sarah Njeri Eldoret trips trip_id driver_id rider_id trip_date fare rider_ra…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alex_murithi/sql-window-functions-made-simple-4ni9

## Related notes
- [[2026-05-30-sql-window-functions-a-practical-guide-to-rownumber-rank-lag-and-lead]]
- [[2026-08-17-the-sql-time-machine-how-to-use-lag-lead-firstvalue-lastvalue-to-analyse-business-performance]]
- [[2026-07-01-10-sql-window-functions-that-separate-junior-from-senior-developers]]
- [[2026-04-27-sql-window-functions-explained-stop-collapsing-your-data-with-group-by]]
- [[2026-05-22-sql-window-functions-for-data-engineering-interviews-rownumber-rank-laglead-and-running-totals]]
- [[2026-09-15-window-functions-in-sql]]
