---
title: Why Do Database Indexes Slow Down INSERTs? (The B+ Tree Page Split Dilemma)
date: '2026-10-24'
source: https://dev.to/binarydose/why-do-database-indexes-slow-down-inserts-the-b-tree-page-split-dilemma-31jg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]'
- '[[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
- '[[2026-10-05-postgres-indexes-under-write-load-every-index-is-a-tax-on-every-write]]'
status: unread
---

> **TL;DR:** Every junior engineer learns that adding an index to a database column makes SELECT queries blazing fast—reducing full table scans ((N)$) to logarithmic B+ Tree lookups ((\log N)$). So why shouldn't we just index every s…

## What’s new and why it matters
Every junior engineer learns that adding an index to a database column makes SELECT queries blazing fast—reducing full table scans ((N)$) to logarithmic B+ Tree lookups ((\log N)$). So why shouldn't we just index every single column in the table? Because on an indexed table, a simple INSERT is never just an append. In high-throughput systems, over-indexing can spike write latency by 300% to 500% . Here is what actually happens inside a database storage engine during an INSERT. 1. Unindexed Table: The O(1) Sequential Append When a table has no secondary indexes , inserting a row is straightforw…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/binarydose/why-do-database-indexes-slow-down-inserts-the-b-tree-page-split-dilemma-31jg

## Related notes
- [[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]
- [[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
- [[2026-10-05-postgres-indexes-under-write-load-every-index-is-a-tax-on-every-write]]
