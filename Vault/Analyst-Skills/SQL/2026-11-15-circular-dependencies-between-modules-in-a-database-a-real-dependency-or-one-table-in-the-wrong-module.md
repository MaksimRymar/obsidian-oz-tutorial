---
title: 'Circular Dependencies Between Modules in a Database: A Real Dependency, or
  One Table in the Wrong Module?'
date: '2026-11-15'
source: https://dev.to/tbson87/circular-dependencies-between-modules-in-a-database-a-real-dependency-or-one-table-in-the-wrong-4eod
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A cycle between modules is counted from two things: the foreign keys, and the list that says which table…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A cycle between modules is counted from two things: the foreign keys, and the list that says which table belongs to which module. On a 34-table PostgreSQL store split into seven modules, ten cycles fell to three when addresses moved to the accounts module and to zero when stock_levels moved to shipping, with no constraint changed. A cycle is a real dependency when every table already sits with the module that writes it; then one foreign key has to go, or the two modules are one.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/circular-dependencies-between-modules-in-a-database-a-real-dependency-or-one-table-in-the-wrong-4eod

## Related notes
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
