---
title: 'Postgres OFFSET vs Keyset Pagination: Up to 9 Seconds vs 0.07 ms on 10M Rows'
date: '2026-11-10'
source: https://medium.com/@nazmul_hasan/postgres-offset-vs-keyset-pagination-up-to-9-seconds-vs-0-07-ms-on-10m-rows-31f534a778c8?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-11-09-why-page-10000-is-slow-offset-vs-keyset-pagination-in-php]]'
- '[[2026-06-15-pagination-with-the-seek-method-in-sql]]'
- '[[2026-11-02-our-slowest-postgres-query-went-from-14-seconds-to-4-ms-with-one-line-of-sql]]'
- '[[2026-07-21-why-a-left-join-with-a-where-clause-becomes-an-inner-join]]'
- '[[2026-04-27-accidentally-updated-a-table-without-a-where-clause-heres-how-to-restore-it-in-sql]]'
- '[[2026-02-26-does-the-order-of-where-clauses-matter-in-postgresql-a-deep-dive-with-composite-indexes]]'
status: unread
---

> **TL;DR:** Keyset only stays flat with an id tie-breaker and a row-value WHERE clause. Here’s the Python. Continue reading on Medium »

## What’s new and why it matters
Keyset only stays flat with an id tie-breaker and a row-value WHERE clause. Here’s the Python. Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@nazmul_hasan/postgres-offset-vs-keyset-pagination-up-to-9-seconds-vs-0-07-ms-on-10m-rows-31f534a778c8?source=rss------sql-5

## Related notes
- [[2026-11-09-why-page-10000-is-slow-offset-vs-keyset-pagination-in-php]]
- [[2026-06-15-pagination-with-the-seek-method-in-sql]]
- [[2026-11-02-our-slowest-postgres-query-went-from-14-seconds-to-4-ms-with-one-line-of-sql]]
- [[2026-07-21-why-a-left-join-with-a-where-clause-becomes-an-inner-join]]
- [[2026-04-27-accidentally-updated-a-table-without-a-where-clause-heres-how-to-restore-it-in-sql]]
- [[2026-02-26-does-the-order-of-where-clauses-matter-in-postgresql-a-deep-dive-with-composite-indexes]]
