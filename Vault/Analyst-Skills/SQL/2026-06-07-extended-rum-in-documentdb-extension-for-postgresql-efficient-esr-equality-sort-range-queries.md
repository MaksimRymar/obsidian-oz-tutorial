---
title: 'Extended RUM in DocumentDB extension for PostgreSQL: Efficient ESR (Equality,
  Sort, Range) Queries'
date: '2026-06-07'
source: https://dev.to/franckpachot/extended-rum-in-documentdb-extension-for-postgresql-efficient-esr-equality-sort-range-queries-5bkj
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-12-postgresql-jsonb-a-complete-guide-to-storing-and-querying-json-data]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-04-10-postgresql-gin-indexes-jsonb-arrays-full-text-search]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
status: unread
---

> **TL;DR:** Last year, I examined RUM indexes within this series on multi-key indexing, demonstrating that they cannot substitute MongoDB's compound indexes for sorted queries. A year later, Microsoft has fixed this in the DocumentD…

## What’s new and why it matters
Last year, I examined RUM indexes within this series on multi-key indexing, demonstrating that they cannot substitute MongoDB's compound indexes for sorted queries. A year later, Microsoft has fixed this in the DocumentDB extension for PostgreSQL with an Extended RUM index that preserves the ordering of the keys, allowing an ordered scan rather than a bitmap scan. Let's revisit our pagination query to see how it performs now. I start a container with the latest DocumentDB (version v0.112-0 from May 26, 2026): docker run -d --name documentdb-local -p 10260:10260 -p 9712:9712 ghcr.io/documentdb/…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/extended-rum-in-documentdb-extension-for-postgresql-efficient-esr-equality-sort-range-queries-5bkj

## Related notes
- [[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-12-postgresql-jsonb-a-complete-guide-to-storing-and-querying-json-data]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-04-10-postgresql-gin-indexes-jsonb-arrays-full-text-search]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
