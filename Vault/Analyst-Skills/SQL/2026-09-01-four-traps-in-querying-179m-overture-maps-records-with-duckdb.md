---
title: Four traps in querying 1.79M Overture Maps records with DuckDB
date: '2026-09-01'
source: https://dev.to/azorkai/four-traps-in-querying-179m-overture-maps-records-with-duckdb-4231
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#python'
- '#sql'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-26-sql-taught-me-that-there-is-always-an-easier-way-to-do-things]]'
- '[[2026-08-29-how-to-set-up-duckdb-run-sql-on-a-csv-with-no-import-step]]'
status: unread
---

> **TL;DR:** We needed a business directory for Turkey inside our CRM, so we went to Overture Maps places: open, CDLA-Permissive, no API key, no quota, ~1.8M Turkish records sitting in public GeoParquet on S3. Reading it turned out t…

## What’s new and why it matters
We needed a business directory for Turkey inside our CRM, so we went to Overture Maps places: open, CDLA-Permissive, no API key, no quota, ~1.8M Turkish records sitting in public GeoParquet on S3. Reading it turned out to be the easy part. Here are the four things that actually cost us time, and the numbers that came out the other end. 1. A join against remote parquet does not stream The obvious query is one statement: read the places theme, read the divisions theme, keep the rows whose point falls inside a Turkish province. -- Do not do this against S3. SELECT p . * FROM read_parquet ( 's3://…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/azorkai/four-traps-in-querying-179m-overture-maps-records-with-duckdb-4231

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-26-sql-taught-me-that-there-is-always-an-easier-way-to-do-things]]
- [[2026-08-29-how-to-set-up-duckdb-run-sql-on-a-csv-with-no-import-step]]
