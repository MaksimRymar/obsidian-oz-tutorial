---
title: 'UUID vs BIGINT Primary Keys: I Inserted 5 Million Rows to Find Out'
date: '2026-11-21'
source: https://dev.to/refactorly/uuid-vs-bigint-primary-keys-i-inserted-5-million-rows-to-find-out-idc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]'
- '[[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]'
- '[[2026-11-20-sql-joins-finally-made-sense-when-i-stopped-memorizing-them]]'
- '[[2026-11-12-stop-using-offset-for-pagination-keyset-pagination-is-10000x-faster-on-deep-pages]]'
- '[[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]'
- '[[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]'
status: unread
---

> **TL;DR:** Should your primary key be a number or a UUID? Developers argue about this constantly, so I measured it: 5 million rows in PostgreSQL with three kinds of keys. One of them made the index almost twice as big and wrote sev…

## What’s new and why it matters
Should your primary key be a number or a UUID? Developers argue about this constantly, so I measured it: 5 million rows in PostgreSQL with three kinds of keys. One of them made the index almost twice as big and wrote seven times more pages. Here's which one, and why. Video version: The three contenders Key Example Size BIGINT 1, 2, 3, 4 … 8 bytes UUID v4 2cfaa8c2-a484-42d2-84f6-1706ab865fad 16 bytes, fully random UUID v7 01a1ef62-ec01-707d-88df-a4aca2b3f289 16 bytes, timestamp first Three UUID v7 values generated one millisecond apart: 01a1ef62-ec01-707d-88df-a4aca2b3f289 01a1ef62-ec02-7022-ad…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refactorly/uuid-vs-bigint-primary-keys-i-inserted-5-million-rows-to-find-out-idc

## Related notes
- [[2026-08-04-optimizing-an-18-tb-azure-sql-hyperscale-database-part-3-the-real-cost-of-indexes]]
- [[2026-11-12-a-createdat-only-cursor-lost-587-rows-even-with-clocktimestamp-and-microseconds]]
- [[2026-11-20-sql-joins-finally-made-sense-when-i-stopped-memorizing-them]]
- [[2026-11-12-stop-using-offset-for-pagination-keyset-pagination-is-10000x-faster-on-deep-pages]]
- [[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]
- [[2026-10-22-why-offset-pagination-is-killing-your-postgresql-queries-and-how-to-implement-keyset-pagination-in-nodejs]]
