---
title: 'Kysely for Beginners: Type-Safe SQL Without an ORM'
date: '2026-11-20'
source: https://dev.to/arhan_khan/kysely-for-beginners-type-safe-sql-without-an-orm-11g9
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-30-kysely-has-a-free-type-safe-sql-query-builder-like-knex-but-with-full-typescript-autocomplete]]'
- '[[2026-03-29-kysely-has-a-free-type-safe-sql-query-builder-with-zero-magic]]'
- '[[2026-03-28-kysely-has-a-free-api-type-safe-sql-query-builder-for-typescript]]'
- '[[2026-03-29-drizzle-orm-has-a-free-typescript-orm-that-thinks-in-sql]]'
- '[[2026-09-18-what-if-your-python-database-code-didnt-care-which-database-you-used]]'
- '[[2026-10-27-why-sql-not-in-returns-no-rows-when-the-column-has-null]]'
status: unread
---

> **TL;DR:** ORMs promise to hide SQL from you, but they often end up hiding the database itself — and then you fight the ORM instead of writing queries. Kysely takes the opposite approach: it is a type-safe SQL query builder. You wr…

## What’s new and why it matters
ORMs promise to hide SQL from you, but they often end up hiding the database itself — and then you fight the ORM instead of writing queries. Kysely takes the opposite approach: it is a type-safe SQL query builder. You write real SQL, in TypeScript, with full autocomplete and compile-time checks. Here is a simple query: import { Kysely , PostgresDialect } from 'kysely' ; interface Database { users : { id : number ; name : string ; email : string ; created_at : Date } ; posts : { id : number ; author_id : number ; title : string } ; } const db = new Kysely < Database > ( { dialect : new Postgres…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/arhan_khan/kysely-for-beginners-type-safe-sql-without-an-orm-11g9

## Related notes
- [[2026-03-30-kysely-has-a-free-type-safe-sql-query-builder-like-knex-but-with-full-typescript-autocomplete]]
- [[2026-03-29-kysely-has-a-free-type-safe-sql-query-builder-with-zero-magic]]
- [[2026-03-28-kysely-has-a-free-api-type-safe-sql-query-builder-for-typescript]]
- [[2026-03-29-drizzle-orm-has-a-free-typescript-orm-that-thinks-in-sql]]
- [[2026-09-18-what-if-your-python-database-code-didnt-care-which-database-you-used]]
- [[2026-10-27-why-sql-not-in-returns-no-rows-when-the-column-has-null]]
