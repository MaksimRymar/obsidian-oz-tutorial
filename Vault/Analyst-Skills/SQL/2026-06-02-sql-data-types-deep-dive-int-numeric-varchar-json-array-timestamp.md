---
title: 'SQL Data Types Deep Dive: INT, NUMERIC, VARCHAR, JSON, ARRAY, TIMESTAMP'
date: '2026-06-02'
source: https://dev.to/gowthampotureddi/sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp-5g3d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#sql'
- '#tableau'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-12-postgresql-jsonb-a-complete-guide-to-storing-and-querying-json-data]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
status: unread
---

> **TL;DR:** sql data types decide three things on every column you ever ship — how many bytes the row costs on disk, how fast the planner can compare values, and whether arithmetic returns the answer the business expects. Every seni…

## What’s new and why it matters
sql data types decide three things on every column you ever ship — how many bytes the row costs on disk, how fast the planner can compare values, and whether arithmetic returns the answer the business expects. Every senior data engineering review reaches for the type catalogue because the wrong choice at table-design time becomes a silent bug under load — INT overflow on a fast-growing event table, FLOAT rounding on a payment ledger, TIMESTAMP without time zone drifting across regions. This guide is a working reference for the types of sql data types that show up in every schema: integers and…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp-5g3d

## Related notes
- [[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-12-postgresql-jsonb-a-complete-guide-to-storing-and-querying-json-data]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
