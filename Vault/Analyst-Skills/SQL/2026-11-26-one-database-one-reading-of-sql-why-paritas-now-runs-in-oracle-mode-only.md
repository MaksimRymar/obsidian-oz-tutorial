---
title: 'One database, one reading of SQL: why Paritas now runs in Oracle mode only'
date: '2026-11-26'
source: https://dev.to/ejazarain/one-database-one-reading-of-sql-why-paritas-now-runs-in-oracle-mode-only-1jg8
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-11-06-paritas-an-oracle-compatible-postgresql-that-tells-you-where-compatibility-ends]]'
- '[[2026-11-23-5-mysql-explain-signals-that-tell-you-exactly-why-your-query-is-slow]]'
- '[[2026-10-04-replacing-azure-data-studio-8-sql-clients-priced-for-a-5-dev-team]]'
- '[[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]'
status: unread
---

> **TL;DR:** First published on the Tech Style blog . Until this month, a Paritas server could speak two dialects at once. Oracle mode listened on one port, PostgreSQL's on another, and a session chose its grammar by where it came in…

## What’s new and why it matters
First published on the Tech Style blog . Until this month, a Paritas server could speak two dialects at once. Oracle mode listened on one port, PostgreSQL's on another, and a session chose its grammar by where it came in. It sounded like the best of both. We have now taken it out, and a Paritas server runs in Oracle mode only. This post explains why, because the reasons are the kind of thing that only shows up when you test against a real Oracle. Two readings of the same object Oracle has one reading of SQL text in a database. Two grammars in one server means two readings, and the trouble is t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ejazarain/one-database-one-reading-of-sql-why-paritas-now-runs-in-oracle-mode-only-1jg8

## Related notes
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-11-06-paritas-an-oracle-compatible-postgresql-that-tells-you-where-compatibility-ends]]
- [[2026-11-23-5-mysql-explain-signals-that-tell-you-exactly-why-your-query-is-slow]]
- [[2026-10-04-replacing-azure-data-studio-8-sql-clients-priced-for-a-5-dev-team]]
- [[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]
