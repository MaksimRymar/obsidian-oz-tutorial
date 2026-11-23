---
title: 'Offset vs Cursor Pagination: Why Your API Breaks at Scale'
date: '2026-11-22'
source: https://dev.to/tanmay2627/offset-vs-cursor-pagination-why-your-api-breaks-at-scale-32ei
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]'
- '[[2026-09-23-cursor-pagination-vs-offset-pagination-which-one-should-you-use]]'
- '[[2026-10-25-pagination-that-skips-rows-is-an-off-by-one-in-the-data-model]]'
- '[[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]'
- '[[2026-11-12-stop-using-offset-for-pagination-keyset-pagination-is-10000x-faster-on-deep-pages]]'
- '[[2026-11-21-database-indexing-basics-that-will-save-you-from-slow-sql-queries]]'
status: unread
---

> **TL;DR:** Most APIs start with offset-based pagination. It feels natural: GET /items?page=500&limit=20 is easy to understand, easy to build, and works seamlessly when your database tables contain a few thousand records. However, o…

## What’s new and why it matters
Most APIs start with offset-based pagination. It feels natural: GET /items?page=500&limit=20 is easy to understand, easy to build, and works seamlessly when your database tables contain a few thousand records. However, once your database table grows to hundreds of thousands or millions of rows, offset pagination quietly degrades performance and causes subtle data anomalies that frustrate end users. Here is why offset pagination fails at scale and how cursor-based pagination fixes it. The Hidden Cost of OFFSET To understand why offset pagination slows down, look at what the database engine does…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tanmay2627/offset-vs-cursor-pagination-why-your-api-breaks-at-scale-32ei

## Related notes
- [[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]
- [[2026-09-23-cursor-pagination-vs-offset-pagination-which-one-should-you-use]]
- [[2026-10-25-pagination-that-skips-rows-is-an-off-by-one-in-the-data-model]]
- [[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]
- [[2026-11-12-stop-using-offset-for-pagination-keyset-pagination-is-10000x-faster-on-deep-pages]]
- [[2026-11-21-database-indexing-basics-that-will-save-you-from-slow-sql-queries]]
