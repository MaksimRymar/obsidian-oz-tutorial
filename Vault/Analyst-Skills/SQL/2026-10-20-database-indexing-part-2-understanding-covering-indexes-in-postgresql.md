---
title: 'Database Indexing – Part 2: Understanding Covering Indexes in PostgreSQL'
date: '2026-10-20'
source: https://dev.to/anusha_renangi_05a4e41d35/database-indexing-part-2-understanding-covering-indexes-in-postgresql-17ee
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]'
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
status: unread
---

> **TL;DR:** Recently, while working on a performance optimization task, I came across an interesting problem. I had a query where I needed to fetch document versions for around 6,500 document IDs . Something like this: SELECT docume…

## What’s new and why it matters
Recently, while working on a performance optimization task, I came across an interesting problem. I had a query where I needed to fetch document versions for around 6,500 document IDs . Something like this: SELECT document_id , document_version FROM documents WHERE document_id IN ( 101 , 102 , 103 , ..., 6500 ); This looks like a simple query, right? But the entire operation was taking around 4 seconds . When I checked where the time was being spent, I noticed that this single database query was taking almost 85% of the total time . That's around 3.4 seconds for just one database query! So, I…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/anusha_renangi_05a4e41d35/database-indexing-part-2-understanding-covering-indexes-in-postgresql-17ee

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-07-why-adding-an-index-wont-fix-your-slow-count-in-postgresql]]
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
