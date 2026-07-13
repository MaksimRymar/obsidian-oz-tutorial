---
title: 'Bitmap Heap Scan in Postgres: When It’s Smart and When It’s a Symptom'
date: '2026-07-13'
source: https://dev.to/philip_mcclarence_2ef9475/bitmap-heap-scan-in-postgres-when-its-smart-and-when-its-a-symptom-32ba
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
- '[[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]'
- '[[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]'
- '[[2026-04-14-why-postgresql-ignores-your-index]]'
status: unread
---

> **TL;DR:** I do not panic when I see Bitmap Heap Scan in a Postgres plan anymore. For years I treated it like a yellow warning light: not obviously broken, but suspicious. Then I spent time reading what the bitmap nodes actually do…

## What’s new and why it matters
I do not panic when I see Bitmap Heap Scan in a Postgres plan anymore. For years I treated it like a yellow warning light: not obviously broken, but suspicious. Then I spent time reading what the bitmap nodes actually do, and I realized many of my “fixes” were either useless or were really composite-index problems in disguise. A Bitmap Heap Scan usually means: Postgres found enough matching rows that plain index lookups would be too random, but not so many that a sequential scan clearly wins. So it batches heap access by page. That is often exactly the right plan. TL;DR A Bitmap Heap Scan is P…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/bitmap-heap-scan-in-postgres-when-its-smart-and-when-its-a-symptom-32ba

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-17-i-tested-postgresql-on-5-million-rows-heres-what-actually-makes-queries-fast]]
- [[2026-03-08-understanding-group-by-in-sql]]
- [[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]
- [[2026-05-10-why-where-phone-null-returns-nothing-in-sql]]
- [[2026-04-14-why-postgresql-ignores-your-index]]
