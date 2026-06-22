---
title: 'Vector Search with Filters: pgvector vs DiskANN on HorizonDB'
date: '2026-06-22'
source: https://dev.to/franckpachot/vector-search-with-filters-pgvector-vs-diskann-on-horizondb-i2k
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-03-01-postgresql-global-statistics-on-partitionned-table-require-a-manual-analyze]]'
status: unread
---

> **TL;DR:** In a previous post , I explained that using filtering with pgvector can decrease recall in approximate nearest neighbor (ANN) searches. This post repeats the same experiment and dataset but compares two methods: pgvector…

## What’s new and why it matters
In a previous post , I explained that using filtering with pgvector can decrease recall in approximate nearest neighbor (ANN) searches. This post repeats the same experiment and dataset but compares two methods: pgvector with HNSW , a popular PostgreSQL extension HorizonDB with DiskANN , Microsoft’s vector index The goal is to understand what happens when similarity search is combined with filtering. Both setups were tested on a HorizonDB instance with 2 vCores and 16 GiB RAM in Azure public preview, where I activated the extensions by adding them to azure.extensions . In real applications, SQ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/vector-search-with-filters-pgvector-vs-diskann-on-horizondb-i2k

## Related notes
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-03-01-postgresql-global-statistics-on-partitionned-table-require-a-manual-analyze]]
