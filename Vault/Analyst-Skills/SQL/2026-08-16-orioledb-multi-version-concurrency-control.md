---
title: OrioleDB Multi-Version Concurrency Control
date: '2026-08-16'
source: https://dev.to/franckpachot/orioledb-multi-version-concurrency-control-43d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-24-b-tree-block-split-whats-the-impact]]'
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
- '[[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]'
- '[[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]'
- '[[2026-04-10-postgresql-gin-indexes-jsonb-arrays-full-text-search]]'
status: unread
---

> **TL;DR:** MVCC not only tracks row history but also records the search-key space. To better understand PostgreSQL MVCC, it's useful to look at some alternatives. One is zheap, which introduced out-of-place undo logging to rebuild…

## What’s new and why it matters
MVCC not only tracks row history but also records the search-key space. To better understand PostgreSQL MVCC, it's useful to look at some alternatives. One is zheap, which introduced out-of-place undo logging to rebuild historical row versions by storing old tuples in an undo log instead of the heap. This was done entirely at the table access method level, without modifying the index access method, but it was eventually abandoned. A more recent development is OrioleDB, which extends this approach to cover the search-key space with an MVCC index access method. Due to PostgreSQL's extensive ecos…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/orioledb-multi-version-concurrency-control-43d

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-24-b-tree-block-split-whats-the-impact]]
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
- [[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]
- [[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]
- [[2026-04-10-postgresql-gin-indexes-jsonb-arrays-full-text-search]]
