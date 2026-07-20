---
title: When to Use an ORM vs SQL and Query Builders
date: '2026-07-19'
source: https://dev.to/doogal/when-to-use-an-orm-vs-sql-and-query-builders-1k
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-07-13-we-dont-need-another-go-orm-we-need-a-better-one]]'
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-03-02-sql-joins-and-window-functions-a-developers-guide]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
status: unread
---

> **TL;DR:** ORMs like Prisma and Hibernate are excellent for simplifying basic CRUD operations. However, for complex queries involving window functions, CTEs, or deep joins, ORMs often get in the way. For advanced use cases, learnin…

## What’s new and why it matters
ORMs like Prisma and Hibernate are excellent for simplifying basic CRUD operations. However, for complex queries involving window functions, CTEs, or deep joins, ORMs often get in the way. For advanced use cases, learning SQL first and using a modern query builder like Drizzle offers the perfect balance of static typing and control. We have all been there. You start a new project, pull in a heavy Object-Relational Mapper (ORM) to make database interactions "easier," and everything goes smoothly while you are just writing basic endpoints. But the moment you need to fetch nested data with a comp…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/doogal/when-to-use-an-orm-vs-sql-and-query-builders-1k

## Related notes
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-07-13-we-dont-need-another-go-orm-we-need-a-better-one]]
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-03-02-sql-joins-and-window-functions-a-developers-guide]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
