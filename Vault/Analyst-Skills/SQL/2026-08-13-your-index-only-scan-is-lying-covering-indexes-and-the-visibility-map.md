---
title: 'Your Index Only Scan Is Lying: Covering Indexes and the Visibility Map'
date: '2026-08-13'
source: https://dev.to/arnavsharma2711/your-index-only-scan-is-lying-covering-indexes-and-the-visibility-map-43nd
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-13-how-database-indexes-work-and-why-yours-might-be-useless]]'
- '[[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]'
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
- '[[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]'
status: unread
---

> **TL;DR:** Covering Indexes Explained: Why "Index Only Scan" Still Hits the Heap You ran EXPLAIN ANALYZE. You saw Index Only Scan in the output. You assumed the query never touched the table. Case closed, right? Then you looked one…

## What’s new and why it matters
Covering Indexes Explained: Why "Index Only Scan" Still Hits the Heap You ran EXPLAIN ANALYZE. You saw Index Only Scan in the output. You assumed the query never touched the table. Case closed, right? Then you looked one line lower. Heap Fetches: 4,827 . Your "index only" scan hit the heap almost five thousand times. Not so index-only after all. This trips up a lot of developers. The plan node says one thing, the runtime metric says another. I won't rehash what an index is or how B+ trees work (I've touched on index fundamentals before ). This post is about the covering trick and the gotcha th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arnavsharma2711/your-index-only-scan-is-lying-covering-indexes-and-the-visibility-map-43nd

## Related notes
- [[2026-05-02-why-standard-indexes-fail-the-architecture-of-the-covering-index]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-13-how-database-indexes-work-and-why-yours-might-be-useless]]
- [[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
- [[2026-06-19-how-to-embed-a-sql-dashboard-into-your-saas-app-without-building-everything-from-scratch]]
