---
title: 'Database Indexing – Part 5: Sequential Scan vs. Index Scan vs. Bitmap Index
  Scan in PostgreSQL'
date: '2026-10-25'
source: https://dev.to/anusha_renangi_05a4e41d35/database-indexing-part-5-sequential-scan-vs-index-scan-vs-bitmap-index-scan-in-postgresql-e3m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-09-sql-joins]]'
- '[[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]'
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
- '[[2026-10-23-database-indexing-part-4-covering-vs-composite-indexes-in-postgresql-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** In my previous articles, we explored different types of indexes in PostgreSQL. But creating an index doesn't mean PostgreSQL will always use it. Depending on the query and the number of matching records, PostgreSQL may c…

## What’s new and why it matters
In my previous articles, we explored different types of indexes in PostgreSQL. But creating an index doesn't mean PostgreSQL will always use it. Depending on the query and the number of matching records, PostgreSQL may choose a Sequential Scan, an Index Scan, or a Bitmap Index Scan. In this article, we'll understand how these scan methods work using practical examples and PostgreSQL execution plans. Understanding Scan Methods with an Example Let's use a students table to understand when PostgreSQL chooses a Sequential Scan, Index Scan, or Bitmap Index Scan. 1. Creating the Table CREATE TABLE s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/anusha_renangi_05a4e41d35/database-indexing-part-5-sequential-scan-vs-index-scan-vs-bitmap-index-scan-in-postgresql-e3m

## Related notes
- [[2026-09-15-sql-joins-explained]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-09-sql-joins]]
- [[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
- [[2026-10-23-database-indexing-part-4-covering-vs-composite-indexes-in-postgresql-which-one-should-you-use]]
