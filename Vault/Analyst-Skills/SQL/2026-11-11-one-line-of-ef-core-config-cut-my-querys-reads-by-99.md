---
title: One Line of EF Core Config Cut My Query’s Reads by 99%
date: '2026-11-11'
source: https://dev.to/umerfarooqofficial/one-line-of-ef-core-config-cut-my-querys-reads-by-99-1pc6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** Your EF Core query is correct. It returns the right row. The column has an index. And SQL Server still reads the whole index to find one row. The cause is one EF Core default that most C# developers never think about. In…

## What’s new and why it matters
Your EF Core query is correct. It returns the right row. The column has an index. And SQL Server still reads the whole index to find one row. The cause is one EF Core default that most C# developers never think about. In this post, I will show you the problem with a real demo, the one-line fix, and a checklist to find it in your own project. TL;DR: EF Core sends C# strings as nvarchar by default. If your column is varchar , SQL Server converts the column and can scan the whole index. In my demo, one line of configuration, .IsUnicode(false) , cut logical reads from 887 to 3. The Setup Here is a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/umerfarooqofficial/one-line-of-ef-core-config-cut-my-querys-reads-by-99-1pc6

## Related notes
- [[2026-09-09-still-writing-slow-sql-queries-10-ways-to-improve-performance]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
