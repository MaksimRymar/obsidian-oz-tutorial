---
title: 'Building SaarDB, Part 3: Compaction'
date: '2026-07-20'
source: https://dev.to/gagandeepahuja09/building-saardb-part-3-compaction-2fhc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
- '[[2026-07-02-dont-use-not-in]]'
- '[[2026-06-20-python-for-beginners-part-2-variables-data-types-numbers]]'
status: unread
---

> **TL;DR:** In Parts 1 and 2, we built a storage engine: WAL for durability and LSM tree for efficient disk reads. This works. But there is a problem growing quietly in the background. Problem: SSTable Files Keep Growing Every memta…

## What’s new and why it matters
In Parts 1 and 2, we built a storage engine: WAL for durability and LSM tree for efficient disk reads. This works. But there is a problem growing quietly in the background. Problem: SSTable Files Keep Growing Every memtable flush creates a new SSTable file. After 10 flushes, you have 10 files. After 1000 flushes, you have 1000 files. Now consider what happens when you serve a GET request: GET user_42 Search SSTable 1000 (newest) → not found Search SSTable 999 → not found Search SSTable 998 → not found ... Search SSTable 1 → found! In the worst case, we search ALL 1000 files before finding the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gagandeepahuja09/building-saardb-part-3-compaction-2fhc

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-05-09-how-i-built-a-real-time-postgresql-wal-reader-in-go]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
- [[2026-07-02-dont-use-not-in]]
- [[2026-06-20-python-for-beginners-part-2-variables-data-types-numbers]]
