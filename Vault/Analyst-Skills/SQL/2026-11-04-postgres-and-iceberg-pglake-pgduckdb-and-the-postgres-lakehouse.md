---
title: 'Postgres and Iceberg: pg_lake, pg_duckdb and the Postgres lakehouse'
date: '2026-11-04'
source: https://dev.to/mohammed_arshadansari_f2/postgres-and-iceberg-pglake-pgduckdb-and-the-postgres-lakehouse-2hcp
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-31-create-index-on-a-live-postgres-table-locks-writes-concurrently-fixes-that-if-you-keep-it-out-of-a-transaction]]'
- '[[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]'
- '[[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]'
- '[[2026-06-25-duckdb-for-data-engineering-in-process-olap-local-etl-parquet-first-workflows]]'
- '[[2026-10-28-sql-basics]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** "Postgres Iceberg" covers four different jobs. You might want to query Iceberg or Parquet files on S3 from Postgres. You might want Postgres to write Iceberg tables. You might want Postgres to be the catalog that other e…

## What’s new and why it matters
"Postgres Iceberg" covers four different jobs. You might want to query Iceberg or Parquet files on S3 from Postgres. You might want Postgres to write Iceberg tables. You might want Postgres to be the catalog that other engines use. Or you might want your Postgres data to land in Iceberg for a warehouse to read. Each job has a different tool, and two of the tools people still recommend are no longer maintained. This post sorts them out. I have not run pg_lake or Iceberg in production. What I did run, on my laptop: PyIceberg 0.12.0 with a plain Postgres 16 container as the Iceberg catalog, and t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/mohammed_arshadansari_f2/postgres-and-iceberg-pglake-pgduckdb-and-the-postgres-lakehouse-2hcp

## Related notes
- [[2026-10-31-create-index-on-a-live-postgres-table-locks-writes-concurrently-fixes-that-if-you-keep-it-out-of-a-transaction]]
- [[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]
- [[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]
- [[2026-06-25-duckdb-for-data-engineering-in-process-olap-local-etl-parquet-first-workflows]]
- [[2026-10-28-sql-basics]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
