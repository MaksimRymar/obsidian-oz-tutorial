---
title: Offset vs cursor pagination in SQL
date: '2026-11-10'
source: https://dev.to/israay/offset-vs-cursor-pagination-in-sql-56hh
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]'
- '[[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
status: unread
---

> **TL;DR:** Pagination means splitting a long list into smaller pages, like showing 10 posts at a time instead of every row in the table. It's a favorite backend interview topic, and the question usually sounds like this: offset or…

## What’s new and why it matters
Pagination means splitting a long list into smaller pages, like showing 10 posts at a time instead of every row in the table. It's a favorite backend interview topic, and the question usually sounds like this: offset or cursor, and why? Every example here is plain SQL for PostgreSQL 18, the current version. You can run it in psql, the command-line tool that comes with Postgres, or in any SQL editor. You'll fill a table with 100,000 posts, watch offset pagination slow down and repeat rows, then fix both problems with a cursor. It takes about 10 minutes to read and try. Offset pagination says "s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/israay/offset-vs-cursor-pagination-in-sql-56hh

## Related notes
- [[2026-10-17-server-side-sorting-and-filtering-for-a-react-data-grid-and-five-places-your-sql-quietly-disagree]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]
- [[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
