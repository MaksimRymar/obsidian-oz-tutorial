---
title: Online enabling checksums in PostgreSQL 19
date: '2026-09-23'
source: https://dev.to/franckpachot/online-enabling-checksums-in-postgresql-19-2agd
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
- '[[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-01-restore-of-database-failed-because-database-is-in-use-causes-solutions]]'
status: unread
---

> **TL;DR:** Enabling data checksums is strongly recommended to detect corruption originating in the storage or I/O layer, which can silently lead to incorrect query results. Although PostgreSQL performs basic sanity checks on the pa…

## What’s new and why it matters
Enabling data checksums is strongly recommended to detect corruption originating in the storage or I/O layer, which can silently lead to incorrect query results. Although PostgreSQL performs basic sanity checks on the page header without checksums, it does not cryptographically verify page contents. As a result, many types of silent corruption could go unnoticed and produce inaccurate query outcomes. In PostgreSQL 18, data pages across database clusters include a checksum by default, which is verified each time a page is read from disk and recalculated when written. Since checksums are enabled…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/online-enabling-checksums-in-postgresql-19-2agd

## Related notes
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
- [[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-01-restore-of-database-failed-because-database-is-in-use-causes-solutions]]
