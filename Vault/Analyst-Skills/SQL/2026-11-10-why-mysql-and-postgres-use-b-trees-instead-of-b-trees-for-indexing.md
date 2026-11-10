---
title: Why MySQL and Postgres Use B+ Trees Instead of B-Trees for Indexing
date: '2026-11-10'
source: https://dev.to/binarydose/why-mysql-and-postgres-use-b-trees-instead-of-b-trees-for-indexing-4cp7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]'
- '[[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]'
- '[[2026-09-04-how-databases-store-data-pages-b-trees-lsm-trees]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]'
status: unread
---

> **TL;DR:** Why MySQL and Postgres Use B+ Trees Instead of B-Trees for Indexing When indexing relational databases (such as MySQL's InnoDB or PostgreSQL's standard btree index), the underlying data structure is almost universally a…

## What’s new and why it matters
Why MySQL and Postgres Use B+ Trees Instead of B-Trees for Indexing When indexing relational databases (such as MySQL's InnoDB or PostgreSQL's standard btree index), the underlying data structure is almost universally a B+ Tree , rather than a standard B-Tree. To understand why, we must analyze how physical storage hardware and operating system page caches interact with tree fan-out. 1. The Fan-Out Problem in Standard B-Trees In a standard B-Tree, every node (both internal and leaf) stores: Search Keys Child Pointers Record / Tuple Pointers (Data Pointers) Because physical storage is organized…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/binarydose/why-mysql-and-postgres-use-b-trees-instead-of-b-trees-for-indexing-4cp7

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]
- [[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]
- [[2026-09-04-how-databases-store-data-pages-b-trees-lsm-trees]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]
