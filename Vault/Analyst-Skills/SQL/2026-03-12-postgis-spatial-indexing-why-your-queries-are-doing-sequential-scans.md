---
title: 'PostGIS Spatial Indexing: Why Your Queries Are Doing Sequential Scans'
date: '2026-03-12'
source: https://dev.to/philip_mcclarence_2ef9475/postgis-spatial-indexing-why-your-queries-are-doing-sequential-scans-6jl
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]'
- '[[2026-03-01-sql-joins]]'
- '[[2026-03-11-sql-joins-window-functions]]'
- '[[2026-03-05-learning-sql-join-and-window-functions]]'
- '[[2026-03-10-joins-window-functions]]'
status: unread
---

> **TL;DR:** The One PostGIS Function Swap That Makes Spatial Queries 1000x Faster I have seen this exact pattern break production at three different companies. A location-based feature ships, it works great in staging, and then it h…

## What’s new and why it matters
The One PostGIS Function Swap That Makes Spatial Queries 1000x Faster I have seen this exact pattern break production at three different companies. A location-based feature ships, it works great in staging, and then it hits production with millions of rows and every "find nearby" query takes seconds instead of milliseconds. The cause is always the same: ST_Distance in a WHERE clause. The Function That Looks Right But Isn't This query is logically correct. It finds all points of interest within roughly 1 km of a location: SELECT name , ST_Distance ( geom , ST_SetSRID ( ST_MakePoint ( - 73 . 985…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/postgis-spatial-indexing-why-your-queries-are-doing-sequential-scans-6jl

## Related notes
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]
- [[2026-03-01-sql-joins]]
- [[2026-03-11-sql-joins-window-functions]]
- [[2026-03-05-learning-sql-join-and-window-functions]]
- [[2026-03-10-joins-window-functions]]
