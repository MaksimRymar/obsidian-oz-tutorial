---
title: The same query went from 0.07 ms to 151 ms on its 6th run, because Postgres
  switched to a generic plan
date: '2026-11-19'
source: https://dev.to/muhammad_adnan_61b78b9816/the-same-query-went-from-007-ms-to-151-ms-on-its-6th-run-because-postgres-switched-to-a-generic-1gdi
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]'
- '[[2026-11-09-my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid]]'
- '[[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]'
- '[[2026-11-18-9-postgresql-fixes-that-took-real-queries-from-100-ms-to-under-1-ms-with-explain-output]]'
- '[[2026-11-13-postgres-not-using-your-index-its-counting-pages-not-rows]]'
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
status: unread
---

> **TL;DR:** Here's a query that was fast in every test, and fast the first five times it ran in production: SELECT id , customer_id , total , created_at FROM orders WHERE status = $1 ORDER BY created_at DESC LIMIT 20 ; On the sixth…

## What’s new and why it matters
Here's a query that was fast in every test, and fast the first five times it ran in production: SELECT id , customer_id , total , created_at FROM orders WHERE status = $1 ORDER BY created_at DESC LIMIT 20 ; On the sixth run it took 151 ms, and it kept taking 151 ms after that. Same query, same parameter, same data. Nothing changed except how many times the connection had run it. The setup PostgreSQL 16, 2,000,000 orders, with the skew most order tables have: status rows delivered 1,939,883 pending 59,909 refunded 208 There's an index on status and one on created_at . The query runs as a prepar…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/muhammad_adnan_61b78b9816/the-same-query-went-from-007-ms-to-151-ms-on-its-6th-run-because-postgres-switched-to-a-generic-1gdi

## Related notes
- [[2026-11-13-a-full-table-scan-isnt-always-a-mistake]]
- [[2026-11-09-my-latest-20-issues-query-read-200000-rows-even-with-an-index-on-projectid]]
- [[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]
- [[2026-11-18-9-postgresql-fixes-that-took-real-queries-from-100-ms-to-under-1-ms-with-explain-output]]
- [[2026-11-13-postgres-not-using-your-index-its-counting-pages-not-rows]]
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
