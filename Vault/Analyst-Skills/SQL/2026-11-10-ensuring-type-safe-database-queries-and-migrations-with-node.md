---
title: Ensuring type safe database queries and migrations with Node
date: '2026-11-10'
source: https://dev.to/lucastonelli/ensuring-type-safe-database-queries-and-migrations-with-node-2gng
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]'
status: unread
---

> **TL;DR:** Talking to a database with Node usually goes one of two ways: you write raw SQL and trust that the strings in your code still match the columns in the database, while dealing with SQL injections and migrations by yoursel…

## What’s new and why it matters
Talking to a database with Node usually goes one of two ways: you write raw SQL and trust that the strings in your code still match the columns in the database, while dealing with SQL injections and migrations by yourself, or you pull in a full ORM and inherit an entire opinionated world just to run simple queries. Both work fine until someone renames a column and you find out about it in production, or you want to do something slightly different and your ORM just won't let you. Fortunately, there's a middle ground where you can get the best of both worlds. Writing queries with Kysely Kysely i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/lucastonelli/ensuring-type-safe-database-queries-and-migrations-with-node-2gng

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]
