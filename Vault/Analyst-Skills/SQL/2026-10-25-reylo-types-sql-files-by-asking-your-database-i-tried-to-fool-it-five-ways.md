---
title: Reylo types .sql files by asking your database. I tried to fool it five ways.
date: '2026-10-25'
source: https://dev.to/frankchu/reylo-types-sql-files-by-asking-your-database-i-tried-to-fool-it-five-ways-46d4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-10-12-introducing-sqlsift-schema-aware-static-analysis-for-sql-no-database-needed]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
status: unread
---

> **TL;DR:** Every TypeScript codebase that talks SQL has the same slow leak: the queries live in one place, the row types live in another, and nothing checks them against each other or against the actual schema. Reylo — a new projec…

## What’s new and why it matters
Every TypeScript codebase that talks SQL has the same slow leak: the queries live in one place, the row types live in another, and nothing checks them against each other or against the actual schema. Reylo — a new project from Colin McDonnell (the Zod author), 1,245 stars in its first four days on GitHub — takes the most direct possible route around the problem: you write the query in a .sql file, import it from TypeScript, and the type checker asks your database what the rows look like. -- get_author.sql select u . id , u . name , u . email , count ( p . id ) as post_count from users u left j…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/frankchu/reylo-types-sql-files-by-asking-your-database-i-tried-to-fool-it-five-ways-46d4

## Related notes
- [[2026-10-12-introducing-sqlsift-schema-aware-static-analysis-for-sql-no-database-needed]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
