---
title: 'When LINQ Isn''t Enough: Raw SQL in Entity Framework Core'
date: '2026-09-30'
source: https://dev.to/homolibere/when-linq-isnt-enough-raw-sql-in-entity-framework-core-2l80
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-04-23-calling-stored-procedures-in-entity-framework-and-choosing-the-right-orm-tool]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-09-23-cursor-pagination-vs-offset-pagination-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** When LINQ Isn't Enough: Raw SQL in Entity Framework Core Sometimes LINQ can't express what you need. A complex stored procedure. A database-specific function. A performance-critical query the ORM mangles. That's when you…

## What’s new and why it matters
When LINQ Isn't Enough: Raw SQL in Entity Framework Core Sometimes LINQ can't express what you need. A complex stored procedure. A database-specific function. A performance-critical query the ORM mangles. That's when you reach for raw SQL — but EF Core still wants to help. Let's explore the escape hatches. FromSqlRaw: Queries That Return Entities When you need raw SQL but still want entity tracking and LINQ composition: var products = dbContext . Products . FromSqlRaw ( "SELECT * FROM Products WHERE Price > 100" ) . ToList (); The results are tracked entities. You can modify and save them. Eve…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/homolibere/when-linq-isnt-enough-raw-sql-in-entity-framework-core-2l80

## Related notes
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-04-23-calling-stored-procedures-in-entity-framework-and-choosing-the-right-orm-tool]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-09-23-cursor-pagination-vs-offset-pagination-which-one-should-you-use]]
