---
title: How I Cut a 5-Hour Batch Job Down to 5 Minutes with PostgreSQL Query Optimization
date: '2026-03-20'
source: https://dev.to/minisundev/how-i-cut-a-5-hour-batch-job-down-to-5-minutes-with-postgresql-query-optimization-5c4e
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
status: unread
---

> **TL;DR:** *All names have been replaced with dessert-related terms for security compliance Problem Overview A serious DB server bottleneck occurred during a daily batch job on a service I had taken over just a month prior, leading…

## What’s new and why it matters
*All names have been replaced with dessert-related terms for security compliance Problem Overview A serious DB server bottleneck occurred during a daily batch job on a service I had taken over just a month prior, leading to a service outage. Symptoms A specific query ran for 5 hours without returning results Subsequent jobs were stuck in a waiting state, halting the entire batch process All data pipeline processing downstream of that process was also halted The query itself was unchanged from before, but performance had dropped sharply after a server rebuild pg_stat_activity results pid | usen…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/minisundev/how-i-cut-a-5-hour-batch-job-down-to-5-minutes-with-postgresql-query-optimization-5c4e

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
