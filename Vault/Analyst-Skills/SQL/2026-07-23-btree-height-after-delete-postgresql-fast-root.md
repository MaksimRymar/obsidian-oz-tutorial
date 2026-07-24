---
title: 'B+tree height after delete: PostgreSQL fast root'
date: '2026-07-23'
source: https://dev.to/franckpachot/btree-height-after-delete-oracle-rebuild-vs-postgresql-fastroot-1ia4
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]'
status: unread
---

> **TL;DR:** Many databases use B+tree indexes, but they all differ. It's a sorted structure. The leaf pages are logically sorted so that a specific key value belongs to one page. A lookup by value reaches a single leaf page and eith…

## What’s new and why it matters
Many databases use B+tree indexes, but they all differ. It's a sorted structure. The leaf pages are logically sorted so that a specific key value belongs to one page. A lookup by value reaches a single leaf page and either directly finds an entry for that value or immediately knows there's no entry with that key. When a page becomes full, it is split into two pages, each covering its own dedicated range. To find the right page, an internal page holds the range of values for the pages below. This internal page can become full, and a new level is added above it. Finally, at the highest level, th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/btree-height-after-delete-oracle-rebuild-vs-postgresql-fastroot-1ia4

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-04-why-your-database-index-gets-ignored-and-how-to-design-one-that-isnt]]
