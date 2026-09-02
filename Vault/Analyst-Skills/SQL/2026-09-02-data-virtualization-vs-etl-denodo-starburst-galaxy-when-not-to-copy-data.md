---
title: 'Data Virtualization vs ETL: Denodo, Starburst Galaxy & When Not to Copy Data'
date: '2026-09-02'
source: https://dev.to/gowthampotureddi/data-virtualization-vs-etl-denodo-starburst-galaxy-when-not-to-copy-data-em
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-08-26-low-latency-serving-layers-tinybird-cube-clickhouse-apis-for-sub-second-product-analytics]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-08-24-amazon-athena-federated-queries-partition-projection-iceberg-ctas-cost-tuning]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Data virtualization is the discipline of leaving data where it already lives — in a Postgres OLTP database, an Iceberg table on S3, a Snowflake account, a SaaS API — and querying it through a single logical layer that fe…

## What’s new and why it matters
Data virtualization is the discipline of leaving data where it already lives — in a Postgres OLTP database, an Iceberg table on S3, a Snowflake account, a SaaS API — and querying it through a single logical layer that federates the sources at runtime, instead of the older reflex of copying everything into one central store with a batch pipeline before anyone can ask a question of it. The hard architectural question was never "can we move the data"; it was " should we." Every copy is a new thing to schedule, to backfill, to keep in sync, to secure twice, and to explain when it drifts from the s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gowthampotureddi/data-virtualization-vs-etl-denodo-starburst-galaxy-when-not-to-copy-data-em

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-08-26-low-latency-serving-layers-tinybird-cube-clickhouse-apis-for-sub-second-product-analytics]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-08-24-amazon-athena-federated-queries-partition-projection-iceberg-ctas-cost-tuning]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
