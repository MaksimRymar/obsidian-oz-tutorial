---
title: 'Stop Using OFFSET for Pagination: Keyset Pagination Is 10,000x Faster on Deep
  Pages'
date: '2026-11-12'
source: https://dev.to/refactorly/stop-using-offset-for-pagination-keyset-pagination-is-10000x-faster-on-deep-pages-1mgp
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]'
- '[[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-09-23-cursor-pagination-vs-offset-pagination-which-one-should-you-use]]'
- '[[2026-11-10-offset-vs-cursor-pagination-in-sql]]'
- '[[2026-11-09-my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid]]'
status: unread
---

> **TL;DR:** Almost every API paginates like this: SELECT * FROM posts ORDER BY created_at DESC , id DESC LIMIT 20 OFFSET 40 ; -- page 3 It works great on page 1. On deep pages it gets thousands of times slower , and it can show user…

## What’s new and why it matters
Almost every API paginates like this: SELECT * FROM posts ORDER BY created_at DESC , id DESC LIMIT 20 OFFSET 40 ; -- page 3 It works great on page 1. On deep pages it gets thousands of times slower , and it can show users the same item twice. Here's the proof, and the fix. Video version: Measured: 1,000,000 rows in PostgreSQL 17 I filled a table with a million posts ( id , title , a 200-character body , created_at ), added an index on (created_at, id) , and timed the same 20-row page query at different offsets. These are medians of 7 runs: OFFSET 0 0.022 ms OFFSET 1000 0.041 ms OFFSET 10000 0.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refactorly/stop-using-offset-for-pagination-keyset-pagination-is-10000x-faster-on-deep-pages-1mgp

## Related notes
- [[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]
- [[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-09-23-cursor-pagination-vs-offset-pagination-which-one-should-you-use]]
- [[2026-11-10-offset-vs-cursor-pagination-in-sql]]
- [[2026-11-09-my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid]]
