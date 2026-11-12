---
title: 'StarRocks Indexes and Best Practices (Part 1): Sort Keys, Prefix, Bitmap and
  Bloom Filter'
date: '2026-11-12'
source: https://sahilkhaire.medium.com/starrocks-indexes-and-best-practices-part-1-sort-keys-prefix-bitmap-and-bloom-filter-2e2e769d3560?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
related:
- '[[2026-11-12-starrocks-indexes-and-best-practices-part-2-n-gram-full-text-vector-and-verifying-index-usage]]'
- '[[2026-10-12-storage-101-pages-heap-tuples-tids-vacuum]]'
- '[[2026-10-22-inside-postgresql-hash-indexes-equality-lookups-and-when-they-are-worth-it]]'
- '[[2026-03-15-understanding-composite-indexes-and-the-left-most-prefix-rule-and-why-b-trees-make-it-work]]'
- '[[2026-08-28-databend-cluster-key-best-practices-choosing-columns-key-order-and-granularity]]'
- '[[2026-08-11-uuid-vs-bigint-what-happens-when-your-database-hits-200m-rows]]'
status: unread
---

> **TL;DR:** Part 1 of 2: sort keys, the built-in indexes, and when to add Bitmap and Bloom filter indexes. Continue reading on Medium »

## What’s new and why it matters
Part 1 of 2: sort keys, the built-in indexes, and when to add Bitmap and Bloom filter indexes. Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://sahilkhaire.medium.com/starrocks-indexes-and-best-practices-part-1-sort-keys-prefix-bitmap-and-bloom-filter-2e2e769d3560?source=rss------sql-5

## Related notes
- [[2026-11-12-starrocks-indexes-and-best-practices-part-2-n-gram-full-text-vector-and-verifying-index-usage]]
- [[2026-10-12-storage-101-pages-heap-tuples-tids-vacuum]]
- [[2026-10-22-inside-postgresql-hash-indexes-equality-lookups-and-when-they-are-worth-it]]
- [[2026-03-15-understanding-composite-indexes-and-the-left-most-prefix-rule-and-why-b-trees-make-it-work]]
- [[2026-08-28-databend-cluster-key-best-practices-choosing-columns-key-order-and-granularity]]
- [[2026-08-11-uuid-vs-bigint-what-happens-when-your-database-hits-200m-rows]]
