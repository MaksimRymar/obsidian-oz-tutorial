---
title: 'Writing Clean SQL: 7 Anti-Patterns That Murder Query Performance'
date: '2026-10-01'
source: https://dev.to/devanshu_patil/writing-clean-sql-7-anti-patterns-that-murder-query-performance-4ine
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-03-21-postgresql-performance-10-queries-youre-writing-wrong-2026-edition]]'
- '[[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]'
- '[[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]'
- '[[2026-04-10-postgresql-gin-indexes-jsonb-arrays-full-text-search]]'
- '[[2026-07-04-database-indexing-and-query-optimization-for-python-developers]]'
- '[[2026-09-11-understanding-database-indexes-the-missing-mental-model]]'
status: unread
---

> **TL;DR:** Most application developers interact with relational databases through ORMs like Hibernate, Prisma, or SQLAlchemy. While ORMs provide immense development velocity, they also generate abstracted SQL queries that look harm…

## What’s new and why it matters
Most application developers interact with relational databases through ORMs like Hibernate, Prisma, or SQLAlchemy. While ORMs provide immense development velocity, they also generate abstracted SQL queries that look harmless in development but cripple production performance under load. Even when writing raw SQL, subtle anti-patterns can trick query planners into discarding indexes, inflating memory buffers, and scanning millions of disk blocks. Here are the most dangerous SQL anti-patterns and how to fix them for instant query optimization. 1. Wrapping Indexed Columns in Functions (Non-SARGabl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devanshu_patil/writing-clean-sql-7-anti-patterns-that-murder-query-performance-4ine

## Related notes
- [[2026-03-21-postgresql-performance-10-queries-youre-writing-wrong-2026-edition]]
- [[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]
- [[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]
- [[2026-04-10-postgresql-gin-indexes-jsonb-arrays-full-text-search]]
- [[2026-07-04-database-indexing-and-query-optimization-for-python-developers]]
- [[2026-09-11-understanding-database-indexes-the-missing-mental-model]]
