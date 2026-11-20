---
title: 'JSONB performance: declare access patterns to PostgreSQL query planner'
date: '2026-11-20'
source: https://dev.to/franckpachot/jsonb-performance-declare-access-patterns-to-postgresql-query-planner-2cip
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-06-17-lie-to-the-postgres-planner-explain-your-query-at-10000-the-rows]]'
- '[[2026-11-13-postgres-not-using-your-index-its-counting-pages-not-rows]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-11-14-postgresql]]'
- '[[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]'
status: unread
---

> **TL;DR:** A common drawback of storing data in JSON fields is limited planner visibility: the optimizer doesn't automatically inspect documents, so selectivity estimates for JSON (or JSONB or BSON) predicates are often weak when u…

## What’s new and why it matters
A common drawback of storing data in JSON fields is limited planner visibility: the optimizer doesn't automatically inspect documents, so selectivity estimates for JSON (or JSONB or BSON) predicates are often weak when useful statistics aren’t available. That’s expected—if you choose JSON to avoid defining the full application schema in the database upfront, the database can’t infer everything about those fields. But this isn’t an all-or-nothing tradeoff. Even in MongoDB, you still declare part of the schema in practice—especially filter fields—through indexes. PostgreSQL, gives you two levers…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/jsonb-performance-declare-access-patterns-to-postgresql-query-planner-2cip

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-06-17-lie-to-the-postgres-planner-explain-your-query-at-10000-the-rows]]
- [[2026-11-13-postgres-not-using-your-index-its-counting-pages-not-rows]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-11-14-postgresql]]
- [[2026-09-05-how-query-optimizers-work-statistics-cardinality-join-order]]
