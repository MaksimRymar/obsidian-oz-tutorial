---
title: 'SQL BETWEEN & Range Queries: Numeric, Date, Inclusive vs Exclusive'
date: '2026-06-03'
source: https://dev.to/gowthampotureddi/sql-between-range-queries-numeric-date-inclusive-vs-exclusive-2hdo
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
- '[[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]'
- '[[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
status: unread
---

> **TL;DR:** sql between is the most innocent-looking keyword in the entire SQL surface — three letters, two operands, "inclusive on both ends," done. Then your nightly report misses every record that landed on the last day of the mo…

## What’s new and why it matters
sql between is the most innocent-looking keyword in the entire SQL surface — three letters, two operands, "inclusive on both ends," done. Then your nightly report misses every record that landed on the last day of the month after midnight, your float column quietly excludes the values you swore were inside the range, and your created_at BETWEEN '2026-01-01' AND '2026-01-31' filter omits 23 hours and 59 minutes of traffic. The keyword isn't broken; the mental model "inclusive both ends" simply doesn't survive contact with timestamps, floats, and back-to-back monthly buckets. This guide walks th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/sql-between-range-queries-numeric-date-inclusive-vs-exclusive-2hdo

## Related notes
- [[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]
- [[2026-05-11-postgresql-sql-data-types-practical-column-type-guide]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
