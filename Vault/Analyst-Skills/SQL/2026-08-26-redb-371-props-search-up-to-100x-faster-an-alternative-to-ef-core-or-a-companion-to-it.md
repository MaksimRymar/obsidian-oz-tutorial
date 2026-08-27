---
title: 'redb 3.7.1: props search up to 100x faster. An alternative to EF Core, or
  a companion to it'
date: '2026-08-26'
source: https://dev.to/rinat_kozin/redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it-12og
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
status: unread
---

> **TL;DR:** Query cost did not depend on what you searched for: the filter sat above GROUP BY. Now the cut happens before the aggregate, on three engines, with no application code changed. Up to 100x on a date range and 5.3x on a fu…

## What’s new and why it matters
Query cost did not depend on what you searched for: the filter sat above GROUP BY. Now the cut happens before the aggregate, on three engines, with no application code changed. Up to 100x on a date range and 5.3x on a full result set in SQL Server. There is a class of performance problem you cannot see on small data and cannot miss on large. Ours looked like this: a query hunting for one rare order number among a hundred thousand objects took exactly as long as a search that found nothing at all. Selectivity did not move the clock. At all. The cause was the shape of the generated SQL. Props va…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rinat_kozin/redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it-12og

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
