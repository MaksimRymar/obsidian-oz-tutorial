---
title: 'Exchange Rates API Data in a Database: Schema, Indexes and As-Of Queries'
date: '2026-11-11'
source: https://dev.to/exchange_rateapi_ee936ad/exchange-rates-api-data-in-a-database-schema-indexes-and-as-of-queries-1jd
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]'
status: unread
---

> **TL;DR:** Sooner or later, every app that uses an exchange rates API needs its own copy of the rates. Invoices must be reproducible next year. Reports must use the rate of the transaction date, not today's. And you do not want a p…

## What’s new and why it matters
Sooner or later, every app that uses an exchange rates API needs its own copy of the rates. Invoices must be reproducible next year. Reports must use the rate of the transaction date, not today's. And you do not want a page view to depend on a network call. This guide gives a schema that holds up: one table, the right keys, an as-of lookup, idempotent loading and a retention plan. The SQL is for PostgreSQL, with notes for MySQL and SQLite at the end. The table CREATE TABLE fx_rate ( base CHAR ( 3 ) NOT NULL , -- ISO 4217, e.g. 'USD' quote CHAR ( 3 ) NOT NULL , -- 1 base = rate quote rate NUMER…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/exchange_rateapi_ee936ad/exchange-rates-api-data-in-a-database-schema-indexes-and-as-of-queries-1jd

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]
