---
title: 'DuckLake: DuckDB''s SQL-Native Lakehouse Format vs Iceberg & Delta'
date: '2026-08-29'
source: https://dev.to/gowthampotureddi/ducklake-duckdbs-sql-native-lakehouse-format-vs-iceberg-delta-pb7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
status: unread
---

> **TL;DR:** DuckLake is the lakehouse format that made a heretical observation out loud: the open table formats everyone standardised on already need a database to be correct, so instead of encoding metadata into a maze of files on…

## What’s new and why it matters
DuckLake is the lakehouse format that made a heretical observation out loud: the open table formats everyone standardised on already need a database to be correct, so instead of encoding metadata into a maze of files on object storage and then bolting a catalog database on top for the one atomic thing files cannot do, put all the metadata in the SQL database and leave only the Parquet data on storage. The result is a table format whose entire catalog and table metadata — schemas, snapshots, file lists, statistics, partition values — lives as ordinary rows in a transactional SQL database, while…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/ducklake-duckdbs-sql-native-lakehouse-format-vs-iceberg-delta-pb7

## Related notes
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
