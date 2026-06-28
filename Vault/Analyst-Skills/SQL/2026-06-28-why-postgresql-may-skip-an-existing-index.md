---
title: Why PostgreSQL May Skip an Existing Index
date: '2026-06-28'
source: https://medium.com/@milkoeugene/why-postgresql-may-skip-an-existing-index-da60f8db3469?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-04-23-postgresql-index-usage-and-optimization]]'
- '[[2026-05-16-stop-indexing-every-where-column-in-postgresql]]'
- '[[2026-04-07-when-to-use-skip-locked-clause]]'
- '[[2026-06-14-indexing-in-databases-a-guide-to-b-trees-and-why-not-binary-search]]'
- '[[2026-04-15-the-missing-foreign-key-index-that-degrades-delete-performance]]'
- '[[2026-05-10-sql-null-is-not-an-empty-value]]'
status: unread
---

> **TL;DR:** A common surprise when reading PostgreSQL execution plans is seeing a sequential scan even though a seemingly suitable index exists. Continue reading on Medium »

## What’s new and why it matters
A common surprise when reading PostgreSQL execution plans is seeing a sequential scan even though a seemingly suitable index exists. Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@milkoeugene/why-postgresql-may-skip-an-existing-index-da60f8db3469?source=rss------sql-5

## Related notes
- [[2026-04-23-postgresql-index-usage-and-optimization]]
- [[2026-05-16-stop-indexing-every-where-column-in-postgresql]]
- [[2026-04-07-when-to-use-skip-locked-clause]]
- [[2026-06-14-indexing-in-databases-a-guide-to-b-trees-and-why-not-binary-search]]
- [[2026-04-15-the-missing-foreign-key-index-that-degrades-delete-performance]]
- [[2026-05-10-sql-null-is-not-an-empty-value]]
