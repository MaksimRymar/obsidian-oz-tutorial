---
title: 'How Database Indexes Work: A Billion Rows in 1.9 ms'
date: '2026-09-27'
source: https://medium.com/@breakingcode49/how-database-indexes-work-a-billion-rows-in-1-9-ms-860f60cc5882?source=rss------sql-5
domain: SQL
relevance: 🟡
tags:
- '#sql'
related:
- '[[2026-05-29-part-11-indexes-and-performance]]'
- '[[2026-07-04-database-indexing-and-query-optimization-for-python-developers]]'
- '[[2026-07-29-why-database-indexes-exist]]'
- '[[2026-06-14-how-database-indexes-actually-work-the-power-of-fewer-reads]]'
- '[[2026-07-04-database-indexing-and-query-optimization-for-java-developers]]'
- '[[2026-09-13-from-10-to-10-million-rows-what-happens-to-postgresql-query-speed-and-disk-footprint-when-you-add]]'
status: unread
---

> **TL;DR:** An index is a sorted copy of one column, kept as a B-tree, so a lookup costs four page reads instead of a hundred-gigabyte scan, and the… Continue reading on Medium »

## What’s new and why it matters
An index is a sorted copy of one column, kept as a B-tree, so a lookup costs four page reads instead of a hundred-gigabyte scan, and the… Continue reading on Medium »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://medium.com/@breakingcode49/how-database-indexes-work-a-billion-rows-in-1-9-ms-860f60cc5882?source=rss------sql-5

## Related notes
- [[2026-05-29-part-11-indexes-and-performance]]
- [[2026-07-04-database-indexing-and-query-optimization-for-python-developers]]
- [[2026-07-29-why-database-indexes-exist]]
- [[2026-06-14-how-database-indexes-actually-work-the-power-of-fewer-reads]]
- [[2026-07-04-database-indexing-and-query-optimization-for-java-developers]]
- [[2026-09-13-from-10-to-10-million-rows-what-happens-to-postgresql-query-speed-and-disk-footprint-when-you-add]]
