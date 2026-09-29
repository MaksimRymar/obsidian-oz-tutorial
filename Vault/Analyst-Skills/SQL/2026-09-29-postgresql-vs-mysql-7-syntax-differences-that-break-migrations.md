---
title: 'PostgreSQL vs MySQL: 7 syntax differences that break migrations'
date: '2026-09-29'
source: https://dev.to/sharefun2023/postgresql-vs-mysql-7-syntax-differences-that-break-migrations-4d52
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-17-i-thought-mssql-and-mysql-were-the-same-i-was-wrong]]'
- '[[2026-08-16-writing-a-postgres-seed-script-that-survives-the-next-migration]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
status: unread
---

> **TL;DR:** Porting a working MySQL schema to PostgreSQL is rarely a find-and-replace. The SQL standard leaves enough room that the two engines disagree on quoting, types, upserts, and pagination — and most of the disagreements fail…

## What’s new and why it matters
Porting a working MySQL schema to PostgreSQL is rarely a find-and-replace. The SQL standard leaves enough room that the two engines disagree on quoting, types, upserts, and pagination — and most of the disagreements fail at runtime, not at parse time. Here are the seven that cost me the most time. 1. Identifier quoting is not the same character MySQL uses backticks, PostgreSQL uses double quotes (which is the ANSI standard): SELECT `order` FROM orders ; -- MySQL SELECT "order" FROM orders ; -- PostgreSQL Two consequences people miss. First, backticks in PostgreSQL are a syntax error, so any ge…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/sharefun2023/postgresql-vs-mysql-7-syntax-differences-that-break-migrations-4d52

## Related notes
- [[2026-04-22-upsert-in-mysql-postgresql-sqlite-ms-sql-server-a-complete-comparison]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-17-i-thought-mssql-and-mysql-were-the-same-i-was-wrong]]
- [[2026-08-16-writing-a-postgres-seed-script-that-survives-the-next-migration]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
