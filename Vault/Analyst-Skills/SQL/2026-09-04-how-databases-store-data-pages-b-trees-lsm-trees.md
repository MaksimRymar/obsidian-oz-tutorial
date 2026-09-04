---
title: 'How Databases Store Data: Pages, B-Trees & LSM Trees'
date: '2026-09-04'
source: https://dev.to/gowthampotureddi/how-databases-store-data-pages-b-trees-lsm-trees-3a67
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** Understanding how databases store data is the difference between guessing why a query is slow and knowing it — because every SELECT , INSERT , and UPDATE you write eventually turns into physical reads and writes against…

## What’s new and why it matters
Understanding how databases store data is the difference between guessing why a query is slow and knowing it — because every SELECT , INSERT , and UPDATE you write eventually turns into physical reads and writes against fixed-size database pages on disk, and the shape of the on-disk structure decides the cost. Beneath the SQL you type sits a storage engine : the component that lays rows out into pages, keeps an index over them, buffers hot pages in memory, and logs every change so a crash can't lose a committed transaction. Two on-disk index families dominate that layer — the read-optimized b-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/how-databases-store-data-pages-b-trees-lsm-trees-3a67

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
