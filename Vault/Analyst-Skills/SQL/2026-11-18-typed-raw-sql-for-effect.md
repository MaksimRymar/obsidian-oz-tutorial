---
title: Typed raw SQL for Effect
date: '2026-11-18'
source: https://dev.to/ismailkarsli/typed-raw-sql-for-effect-13co
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-06-20-oracle-ora-00937-error-causes-and-solutions-complete-guide]]'
- '[[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]'
status: unread
---

> **TL;DR:** I wanted to write plain SQL in Effect code and still get typed rows, without a query builder and without writing row types by hand. So I made @typesql/effect . import { Effect } from "effect" ; import { createSql } from…

## What’s new and why it matters
I wanted to write plain SQL in Effect code and still get typed rows, without a query builder and without writing row types by hand. So I made @typesql/effect . import { Effect } from "effect" ; import { createSql } from "@typesql/effect" ; import { postgresDialect } from "@typesql/core/postgres" ; import type { DB } from "./db/schema.js" ; const sql = createSql < DB > ( postgresDialect ) ; export const program = Effect . gen ( function * ( ) { const author = yield * sql ( "SELECT id, name FROM authors ORDER BY followers DESC LIMIT 1" , ) . execTakeFirst ( ) ; const books = yield * sql ( ` WITH…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ismailkarsli/typed-raw-sql-for-effect-13co

## Related notes
- [[2026-05-13-sql-execution-order-write-queries-that-think-like-the-database]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-06-20-oracle-ora-00937-error-causes-and-solutions-complete-guide]]
- [[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]
