---
title: 'Replacing deep OFFSET pagination in D1: rows read and inserts between pages'
date: '2026-10-03'
source: https://dev.to/hirodeath/replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages-2b5
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
- '[[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-04-20-the-latest-bug-that-silently-duplicated-transaction-ids-in-production]]'
status: unread
---

> **TL;DR:** LIMIT 20 OFFSET ... makes the next page of a list easy to express. But deeper pages require skipping more rows without returning them. Using an index does not, by itself, eliminate that work. This experiment inserted 100…

## What’s new and why it matters
LIMIT 20 OFFSET ... makes the next page of a list easy to express. But deeper pages require skipping more rows without returning them. Using an index does not, by itself, eliminate that work. This experiment inserted 100,000 synthetic notifications into local D1 and fetched the same 20 records with OFFSET and a cursor. It examined how many rows were read and what happened when a new row arrived between pages. The checks ran on September 11, 2026. They do not measure production D1 latency or billing, or establish a universal row count at which pagination becomes slow. Define a key that preserve…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hirodeath/replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages-2b5

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
- [[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-04-20-the-latest-bug-that-silently-duplicated-transaction-ids-in-production]]
