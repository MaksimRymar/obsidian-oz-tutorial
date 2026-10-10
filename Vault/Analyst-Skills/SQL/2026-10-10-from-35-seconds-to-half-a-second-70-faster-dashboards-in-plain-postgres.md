---
title: 'From 35 seconds to half a second: 70 faster dashboards in plain Postgres'
date: '2026-10-10'
source: https://dev.to/devon_theriault_85735c82a/from-35-seconds-to-half-a-second-70x-faster-dashboards-in-plain-postgres-513i
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** From 35 seconds to half a second: 70× faster dashboards in plain Postgres Pick "Last 12 months" on an analytics dashboard and Postgres reads every event of the year, once for every panel. At scale, ours took 35 seconds.…

## What’s new and why it matters
From 35 seconds to half a second: 70× faster dashboards in plain Postgres Pick "Last 12 months" on an analytics dashboard and Postgres reads every event of the year, once for every panel. At scale, ours took 35 seconds. Now it takes half a second on the same database, thanks to one table and one property of our numbers that most people forget to check. Every panel re-read the year A Foresite dashboard has about 18 panels, and each one is its own GROUP BY over the events in the chosen period: SQL for "sort the events into piles and count each pile", like pageviews per country or visitors per pa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devon_theriault_85735c82a/from-35-seconds-to-half-a-second-70x-faster-dashboards-in-plain-postgres-513i

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
