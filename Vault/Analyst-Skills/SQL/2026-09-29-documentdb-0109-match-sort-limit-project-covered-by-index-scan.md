---
title: 'DocumentDB 0.109: $match $sort $limit $project covered by index scan'
date: '2026-09-29'
source: https://dev.to/franckpachot/documentdb-0109-match-sort-limit-project-covered-by-index-scan-5hbf
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-08-postgresql-query-optimization-10-techniques-that-actually-work]]'
status: unread
---

> **TL;DR:** This should have been the first post of this series. A few months ago, I demonstrated ( video ) what I see as one of the key advantages of a document model: a compound index can support filtering, sorting, and pagination…

## What’s new and why it matters
This should have been the first post of this series. A few months ago, I demonstrated ( video ) what I see as one of the key advantages of a document model: a compound index can support filtering, sorting, and pagination across data embedded in a one-to-many relationship. In a normalized relational model, that relationship typically spans multiple tables. Indexes belong to individual tables, so answering the same query may require to join more rows before sorting and filtering. That demo used MongoDB. Some MongoDB emulations on SQL databases pretend compatibility but lack performance it they d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/documentdb-0109-match-sort-limit-project-covered-by-index-scan-5hbf

## Related notes
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-08-postgresql-query-optimization-10-techniques-that-actually-work]]
