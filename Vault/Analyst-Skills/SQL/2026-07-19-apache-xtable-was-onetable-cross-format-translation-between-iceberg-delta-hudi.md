---
title: 'Apache XTable (was OneTable): Cross-Format Translation Between Iceberg, Delta
  & Hudi'
date: '2026-07-19'
source: https://dev.to/gowthampotureddi/apache-xtable-was-onetable-cross-format-translation-between-iceberg-delta-hudi-3f21
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-06-13-apache-hudi-merge-on-read-vs-copy-on-write-picking-the-right-table-type]]'
- '[[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
status: unread
---

> **TL;DR:** apache xtable is the metadata-only translator that answers the awkward question every senior data engineer eventually gets asked in 2026 — "we have Snowflake queries, Databricks notebooks, Trino dashboards, and a legacy…

## What’s new and why it matters
apache xtable is the metadata-only translator that answers the awkward question every senior data engineer eventually gets asked in 2026 — "we have Snowflake queries, Databricks notebooks, Trino dashboards, and a legacy Hudi pipeline all pointing at the same S3 prefix; how do we not maintain three physical copies of the data?" — and it answers it by writing translated Iceberg, Delta, and Hudi metadata on top of one shared Parquet directory so every engine sees a table in the format it prefers, without ever copying a single byte of column data. The project began life as apache onetable inside O…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gowthampotureddi/apache-xtable-was-onetable-cross-format-translation-between-iceberg-delta-hudi-3f21

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-06-13-apache-hudi-merge-on-read-vs-copy-on-write-picking-the-right-table-type]]
- [[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
