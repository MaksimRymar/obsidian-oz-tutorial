---
title: jOOQ codegen from Flyway migrations, with no database
date: '2026-08-29'
source: https://dev.to/behzodhalil/jooq-codegen-from-flyway-migrations-with-no-database-1mia
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-16-review-sql-migrations-in-30-seconds-seed-migrate-compare]]'
status: unread
---

> **TL;DR:** jOOQ generates its code from a schema, which means something has to be holding a schema at build time. The usual answer is a database, and a database is the one thing our CI does not have. StockPlus runs a Spring Boot ba…

## What’s new and why it matters
jOOQ generates its code from a schema, which means something has to be holding a schema at build time. The usual answer is a database, and a database is the one thing our CI does not have. StockPlus runs a Spring Boot backend where every query is written in the jOOQ DSL, so nothing on the server compiles until the generator has produced its classes. The GitHub Actions workflow has no services: block, no Docker, and no Postgres. This is how the schema gets there anyway, which property in the config is the one to read twice, and the single migration mistake that no build configuration can catch.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/behzodhalil/jooq-codegen-from-flyway-migrations-with-no-database-1mia

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-16-review-sql-migrations-in-30-seconds-seed-migrate-compare]]
