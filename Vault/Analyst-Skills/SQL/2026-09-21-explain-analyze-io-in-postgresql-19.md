---
title: EXPLAIN (ANALYZE, IO) in PostgreSQL 19
date: '2026-09-21'
source: https://dev.to/franckpachot/explain-analyze-io-in-postgresql-19-igh
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]'
- '[[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]'
- '[[2026-09-14-why-the-index-i-added-made-my-query-slower]]'
status: unread
---

> **TL;DR:** I'll be showcasing some exciting PostgreSQL work, featuring contributions from Microsoft engineers at pgconf.eu: Postgres 19, 20, & Beyond: Live Demos of New Features & Tools . During the demos, we'll explore many execut…

## What’s new and why it matters
I'll be showcasing some exciting PostgreSQL work, featuring contributions from Microsoft engineers at pgconf.eu: Postgres 19, 20, & Beyond: Live Demos of New Features & Tools . During the demos, we'll explore many execution plans, including a new PostgreSQL 19 feature—the IO option for EXPLAIN . EXPLAIN (ANALYZE) executes the query and reports runtime statistics. BUFFERS shows logical buffer activity: cache hits and reads. IO goes further, reporting how the read stream behaved: how far ahead PostgreSQL was able to prefetch, how many physical I/O requests were issued, their sizes, the level of…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/franckpachot/explain-analyze-io-in-postgresql-19-igh

## Related notes
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]
- [[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]
- [[2026-09-14-why-the-index-i-added-made-my-query-slower]]
