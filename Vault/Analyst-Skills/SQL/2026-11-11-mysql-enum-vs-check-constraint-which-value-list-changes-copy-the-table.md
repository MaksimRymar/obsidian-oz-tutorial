---
title: 'MySQL ENUM vs CHECK Constraint: Which Value List Changes Copy the Table'
date: '2026-11-11'
source: https://dev.to/tbson87/mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table-4jh3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On MySQL 8.4, appending a value to the end of an ENUM of up to 255 values is a metadata change that take…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On MySQL 8.4, appending a value to the end of an ENUM of up to 255 values is a metadata change that takes no time, while inserting one in the middle, reordering, or removing one copies the whole table and holds back writes. Removing a value that rows still hold fails with error 1265. An enforced CHECK on a VARCHAR copies the table for every change to its list, appends included, and a lookup table needs no ALTER TABLE at all. On MySQL 8.4, an ENUM is the cheapest value list to ext…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table-4jh3

## Related notes
- [[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
