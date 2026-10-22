---
title: Why OFFSET Pagination Is Killing Your PostgreSQL Queries (And How to Implement
  Keyset Pagination in Node.js)
date: '2026-10-22'
source: https://dev.to/subashthiruppathy_5e0f532/why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-1m8m
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
status: unread
---

> **TL;DR:** Almost every API starts with the same pagination code: SELECT * FROM orders ORDER BY created_at DESC LIMIT 20 OFFSET 40 ; It's simple, it works in development, and it ships. Months later, the table has millions of rows a…

## What’s new and why it matters
Almost every API starts with the same pagination code: SELECT * FROM orders ORDER BY created_at DESC LIMIT 20 OFFSET 40 ; It's simple, it works in development, and it ships. Months later, the table has millions of rows and you're seeing: Page 1 loads in 5 ms. Page 5,000 takes 3 seconds. A crawler or an export job walking through pages brings the database to its knees. Users report seeing the same item twice, or missing items entirely, as they page through a live feed. All three have the same root cause: OFFSET pagination doesn't scale and isn't stable. This post explains why, then builds the a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/subashthiruppathy_5e0f532/why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-1m8m

## Related notes
- [[2026-07-09-stop-using-offset-for-pagination-switching-to-cursor-based-filtering-for-massive-datasets]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
