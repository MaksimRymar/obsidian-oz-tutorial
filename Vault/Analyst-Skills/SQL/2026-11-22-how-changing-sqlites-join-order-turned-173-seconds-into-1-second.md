---
title: How Changing SQLite's JOIN Order Turned 173 Seconds into 1 Second
date: '2026-11-22'
source: https://dev.to/tanahiro2010/how-changing-sqlites-join-order-turned-173-seconds-into-1-second-46en
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#presentations'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** How Changing SQLite's JOIN Order Took Processing from 173 Seconds to 1 Second Rewriting JOIN as CROSS JOIN took us from 173 seconds to 1 second. The takeaway While working on my own CLI tool, ghusage, I was getting frust…

## What’s new and why it matters
How Changing SQLite's JOIN Order Took Processing from 173 Seconds to 1 Second Rewriting JOIN as CROSS JOIN took us from 173 seconds to 1 second. The takeaway While working on my own CLI tool, ghusage, I was getting frustrated by how long CI took on every PR. It turned out that generating reports from SQLite's cache took 173 seconds per run. I rewrote JOIN as CROSS JOIN to fix the loop order, and got the time down to the 1-second range. Wow. The cause was SQLite choosing the wrong tables for the outer and inner loops of a nested loop SQLite made that choice because it didn't have table statisti…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tanahiro2010/how-changing-sqlites-join-order-turned-173-seconds-into-1-second-46en

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
