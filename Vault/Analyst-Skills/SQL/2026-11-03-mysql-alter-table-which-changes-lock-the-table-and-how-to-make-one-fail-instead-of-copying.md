---
title: 'MySQL ALTER TABLE: Which Changes Lock the Table, and How to Make One Fail
  Instead of Copying'
date: '2026-11-03'
source: https://dev.to/tbson87/mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying-4e13
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-10-28-mysql-workbench-alternative-er-diagrams-past-250-tables]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On MySQL 8.4, adding, dropping or renaming a column and changing a default are metadata-only, and an ind…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On MySQL 8.4, adding, dropping or renaming a column and changing a default are metadata-only, and an index or NOT NULL builds while writes continue. Other type changes, including a VARCHAR that crosses 255 bytes, a CHECK and a foreign key with checks on copy the table and hold back writes until the copy ends. Every ALTER TABLE , instant ones included, first waits for an exclusive metadata lock, and new queries on the table queue behind it. On MySQL 8.4, most ALTER TABLE statement…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying-4e13

## Related notes
- [[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-10-28-mysql-workbench-alternative-er-diagrams-past-250-tables]]
