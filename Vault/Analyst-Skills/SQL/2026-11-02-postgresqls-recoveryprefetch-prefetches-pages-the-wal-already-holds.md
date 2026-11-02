---
title: PostgreSQL's recovery_prefetch prefetches pages the WAL already holds
date: '2026-11-02'
source: https://dev.to/importstatic/postgresqls-recoveryprefetch-prefetches-pages-the-wal-already-holds-3fc6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]'
- '[[2026-10-24-pdfua-the-verapdf-failures-you-can-fix-with-30-lines-of-pikepdf-measured-on-24-files]]'
- '[[2026-08-29-i-broke-production-with-a-plsql-loop-here-are-the-10-steps-i-skipped]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Originally published on ImportStatic . A post on ardentperf from October 20, which reached the Hacker News front page, describes a synchronous standby on a 500 IOPS cloud disk that fell behind after a write burst and sta…

## What’s new and why it matters
Originally published on ImportStatic . A post on ardentperf from October 20, which reached the Hacker News front page, describes a synchronous standby on a 500 IOPS cloud disk that fell behind after a write burst and stalled writes on the primary for over 30 minutes. With recovery_prefetch = off the long stall went away, and the author leans towards turning it off everywhere. We don't have a standby on metered storage, so we couldn't reproduce the outage. We did count what the prefetcher spends its reads on during replay on PostgreSQL 18.6, and the same counters are available on your own stand…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/importstatic/postgresqls-recoveryprefetch-prefetches-pages-the-wal-already-holds-3fc6

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-09-28-set-based-vs-row-by-row-postgresql-refresh-from-114-to-12-seconds]]
- [[2026-10-24-pdfua-the-verapdf-failures-you-can-fix-with-30-lines-of-pikepdf-measured-on-24-files]]
- [[2026-08-29-i-broke-production-with-a-plsql-loop-here-are-the-10-steps-i-skipped]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
