---
title: 'SQLAlchemy MissingGreenlet in Async Code: Fix Lazy Loading With selectinload,
  awaitable_attrs, or lazy="raise"'
date: '2026-11-12'
source: https://dev.to/libme/sqlalchemy-missinggreenlet-in-async-code-fix-lazy-loading-with-selectinload-awaitableattrs-or-nko
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-04-backend-interview-question-why-does-loading-20-orders-run-21-queries]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
status: unread
---

> **TL;DR:** sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here means you touched a relationship or expired column that wasn't loaded, and SQLAlchemy tried to run a lazy-load query from s…

## What’s new and why it matters
sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here means you touched a relationship or expired column that wasn't loaded, and SQLAlchemy tried to run a lazy-load query from synchronous attribute access inside an async session. The durable fix is to decide at query time which relationships you need ( selectinload or joinedload ) instead of letting attribute access trigger I/O. Use awaitable_attrs for the occasional one-off, and lazy="raise" to turn the bug into a loud, early failure. (Written against SQLAlchemy 2.0.x as of late 2026.) Why does Missi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/libme/sqlalchemy-missinggreenlet-in-async-code-fix-lazy-loading-with-selectinload-awaitableattrs-or-nko

## Related notes
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-04-backend-interview-question-why-does-loading-20-orders-run-21-queries]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
