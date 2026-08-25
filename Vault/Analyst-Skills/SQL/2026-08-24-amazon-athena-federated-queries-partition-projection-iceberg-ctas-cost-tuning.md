---
title: 'Amazon Athena & Federated Queries: Partition Projection, Iceberg & CTAS Cost
  Tuning'
date: '2026-08-24'
source: https://dev.to/gowthampotureddi/amazon-athena-federated-queries-partition-projection-iceberg-ctas-cost-tuning-1ga8
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
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-08-15-the-small-files-problem-compaction-optimize-file-sizing-across-engines]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]'
status: unread
---

> **TL;DR:** Amazon Athena bills you for exactly one thing — the bytes it reads off S3 to answer your query — and that single fact quietly decides whether your data lake is a cheap, fast query layer or a runaway line item that financ…

## What’s new and why it matters
Amazon Athena bills you for exactly one thing — the bytes it reads off S3 to answer your query — and that single fact quietly decides whether your data lake is a cheap, fast query layer or a runaway line item that finance flags at the end of the quarter. Because Athena is serverless Presto/Trino with no cluster to size and no per-hour meter, the entire cost-and-latency story collapses into how much data scanned each query touches, and every tuning lever — how you lay out partitions, whether you store rows or columns, whether you compress, whether the engine can prune before it reads — exists t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/amazon-athena-federated-queries-partition-projection-iceberg-ctas-cost-tuning-1ga8

## Related notes
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-08-15-the-small-files-problem-compaction-optimize-file-sizing-across-engines]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]
