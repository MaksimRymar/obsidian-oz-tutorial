---
title: 'From 9 Seconds to 2 Milliseconds: Database Indexes Explained'
date: '2026-11-13'
source: https://dev.to/thebytemechanics/from-9-seconds-to-2-milliseconds-database-indexes-explained-4h1k
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-09-11-understanding-database-indexes-the-missing-mental-model]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
status: unread
---

> **TL;DR:** How an index works, why it's a B-tree, and the one mistake that makes the database ignore it This query took nine seconds: SELECT * FROM users WHERE email = 'priya@example.com'; One line of SQL made it two milliseconds.…

## What’s new and why it matters
How an index works, why it's a B-tree, and the one mistake that makes the database ignore it This query took nine seconds: SELECT * FROM users WHERE email = 'priya@example.com'; One line of SQL made it two milliseconds. That's four thousand times faster, with no new hardware and no code changes. That line creates a database index. But here's the twist: you can have exactly the right index, and the database will still ignore it, because of one tiny thing in your query. By the end of this article you'll know how indexes work, and you'll spot that mistake in your own code. If you'd rather watch,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/thebytemechanics/from-9-seconds-to-2-milliseconds-database-indexes-explained-4h1k

## Related notes
- [[2026-09-11-understanding-database-indexes-the-missing-mental-model]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
