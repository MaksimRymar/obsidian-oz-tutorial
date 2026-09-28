---
title: 'PostgreSQL numeric vs double precision vs money: Which Type to Use for Prices'
date: '2026-09-28'
source: https://dev.to/tbson87/postgresql-numeric-vs-double-precision-vs-money-which-type-to-use-for-prices-5b9j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]'
- '[[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Store prices and other amounts of money as numeric with a declared scale, such as numeric(12,2) . A doub…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Store prices and other amounts of money as numeric with a declared scale, such as numeric(12,2) . A double precision column cannot hold 0.10 exactly, and in a 1,000,000-row test its sum() gave a different answer on each parallel run. The money type is exact but ties its fractional digits and output to the server's lc_monetary locale, stores no currency, and truncates on division. For prices, totals and balances in PostgreSQL, reach for numeric(12,2) or another bounded numeric . I…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/postgresql-numeric-vs-double-precision-vs-money-which-type-to-use-for-prices-5b9j

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-06-02-sql-data-types-deep-dive-int-numeric-varchar-json-array-timestamp]]
- [[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
