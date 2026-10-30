---
title: EF Core Isn't Slow. These 5 Query Patterns Are.
date: '2026-10-29'
source: https://dev.to/vladut02/ef-core-isnt-slow-these-5-query-patterns-are-1m82
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
status: unread
---

> **TL;DR:** Four lines of C# can send 101 queries to SQL Server. One line can pull a whole table into memory just to show ten rows. In both cases EF Core is doing exactly what the code asked for. The problem is the SQL that the code…

## What’s new and why it matters
Four lines of C# can send 101 queries to SQL Server. One line can pull a whole table into memory just to show ten rows. In both cases EF Core is doing exactly what the code asked for. The problem is the SQL that the code turns into. Here are five patterns behind a lot of slow EF Core code, plus the one habit that catches all of them. First: LINQ isn't run as C When you write a LINQ query against a DbSet , EF Core doesn't run your lambdas. It reads the query as an expression tree and translates it into SQL. Nothing hits the database until you ask for results, with ToList , First , foreach and t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vladut02/ef-core-isnt-slow-these-5-query-patterns-are-1m82

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
