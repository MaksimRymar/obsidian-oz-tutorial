---
title: Ad-Hoc Video Analytics with DuckDB on Parquet Exports from Production SQLite
date: '2026-06-28'
source: https://dev.to/ahmet_gedik778845/ad-hoc-video-analytics-with-duckdb-on-parquet-exports-from-production-sqlite-9oh
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-06-25-duckdb-for-data-engineering-in-process-olap-local-etl-parquet-first-workflows]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** Every couple of hours, a cron job on a cheap LiteSpeed shared host wakes up, hits the YouTube Data API for eight regions — US, GB, DE, FR, IN, BR, AU, CA — and writes trending-video metadata into a single SQLite database…

## What’s new and why it matters
Every couple of hours, a cron job on a cheap LiteSpeed shared host wakes up, hits the YouTube Data API for eight regions — US, GB, DE, FR, IN, BR, AU, CA — and writes trending-video metadata into a single SQLite database. That is the entire ingestion pipeline behind TrendVidStream , a multi-region video streaming discovery site I run. PHP 8.4 renders the pages, SQLite FTS5 powers search, and deploys happen over plain FTP because that is what the hosting gives you. It works, it is boring, and it costs almost nothing. What this setup does not handle gracefully is me, at 11pm, asking questions li…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ahmet_gedik778845/ad-hoc-video-analytics-with-duckdb-on-parquet-exports-from-production-sqlite-9oh

## Related notes
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-06-25-duckdb-for-data-engineering-in-process-olap-local-etl-parquet-first-workflows]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
