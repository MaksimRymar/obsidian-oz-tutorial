---
title: Postgres earthdistance
date: '2026-09-04'
source: https://dev.to/dshumw/postgres-earthdistance-23g0
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-08-06-find-your-worst-postgres-query-in-15-minutes-with-pgstatstatements]]'
- '[[2026-06-25-what-actually-happens-when-you-type-what-is-python-into-chatgpt]]'
- '[[2026-08-19-postgis-vs-duckdb-choosing-the-right-tool-for-spatial-data]]'
- '[[2026-04-20-greatcircledistance-in-clickhouse-avoiding-full-table-scans]]'
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
- '[[2026-05-17-devmcp-context-a-simple-ai-memory-layer-for-your-agent]]'
status: unread
---

> **TL;DR:** One PostgreSQL feature I recently revisited is earthdistance, a nice reminder that not every problem involving latitude and longitude requires a full GIS stack. The earthdistance extension provides a straightforward way…

## What’s new and why it matters
One PostgreSQL feature I recently revisited is earthdistance, a nice reminder that not every problem involving latitude and longitude requires a full GIS stack. The earthdistance extension provides a straightforward way to calculate great-circle distances between locations on Earth. Combined with PostgreSQL’s cube extension, ll_to_earth() converts latitude and longitude into a representation that earth_distance() can use to calculate distance in meters. It also provides earth_box(), which is useful for nearby-location searches. An indexed bounding-box search can quickly narrow the candidates,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dshumw/postgres-earthdistance-23g0

## Related notes
- [[2026-08-06-find-your-worst-postgres-query-in-15-minutes-with-pgstatstatements]]
- [[2026-06-25-what-actually-happens-when-you-type-what-is-python-into-chatgpt]]
- [[2026-08-19-postgis-vs-duckdb-choosing-the-right-tool-for-spatial-data]]
- [[2026-04-20-greatcircledistance-in-clickhouse-avoiding-full-table-scans]]
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
- [[2026-05-17-devmcp-context-a-simple-ai-memory-layer-for-your-agent]]
