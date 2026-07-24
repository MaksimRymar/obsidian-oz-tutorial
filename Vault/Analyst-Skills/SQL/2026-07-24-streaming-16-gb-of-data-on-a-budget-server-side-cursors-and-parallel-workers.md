---
title: 'Streaming 16 GB of data on a budget: server-side cursors and parallel workers'
date: '2026-07-24'
source: https://dev.to/wondadav/streaming-16-gb-of-data-on-a-budget-server-side-cursors-and-parallel-workers-5een
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-07-04-database-indexing-and-query-optimization-for-python-developers]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
status: unread
---

> **TL;DR:** A data processing pipeline that processes 100,000 rows is not the same as one that processes 10 million. At a small scale, a single-threaded Python script does the job. At tens of millions of rows, the first bottleneck y…

## What’s new and why it matters
A data processing pipeline that processes 100,000 rows is not the same as one that processes 10 million. At a small scale, a single-threaded Python script does the job. At tens of millions of rows, the first bottleneck you hit is time: the pipeline takes too long to finish. The obvious fix is to run the work in parallel across multiple workers, and that's where the second bottleneck shows up: memory. Sequential is too slow and naive parallelizing hits memory A typical pipeline reads from a database, transforms each row in Python, and writes the results back. The first pass is a straight loop a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wondadav/streaming-16-gb-of-data-on-a-budget-server-side-cursors-and-parallel-workers-5een

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-07-04-database-indexing-and-query-optimization-for-python-developers]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
