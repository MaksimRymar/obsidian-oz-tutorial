---
title: 'MySQL to PostgreSQL Schema Conversion: What Each Column Type Should Become,
  and What Silently Changes'
date: '2026-10-29'
source: https://dev.to/tbson87/mysql-to-postgresql-schema-conversion-what-each-column-type-should-become-and-what-silently-ecf
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-01-changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes]]'
- '[[2026-10-22-how-to-auto-update-an-updatedat-column-mysql-on-update-vs-a-database-trigger-vs-the-orm]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Most MySQL types have an obvious PostgreSQL twin, but eight need a decision: TINYINT(1) , UNSIGNED integ…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Most MySQL types have an obvious PostgreSQL twin, but eight need a decision: TINYINT(1) , UNSIGNED integers, DATETIME vs TIMESTAMP , ENUM , SET , ON UPDATE CURRENT_TIMESTAMP , AUTO_INCREMENT and the collation behind every unique text column. The last one fails silently: a MySQL unique email refuses Ana@Example.com after ana@example.com , and the same constraint on PostgreSQL accepts both. Converting a MySQL schema to PostgreSQL is mostly mechanical, and the parts that are not mec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/mysql-to-postgresql-schema-conversion-what-each-column-type-should-become-and-what-silently-ecf

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-01-changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes]]
- [[2026-10-22-how-to-auto-update-an-updatedat-column-mysql-on-update-vs-a-database-trigger-vs-the-orm]]
