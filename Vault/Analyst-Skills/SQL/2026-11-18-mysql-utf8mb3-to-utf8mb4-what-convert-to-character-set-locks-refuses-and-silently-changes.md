---
title: 'MySQL utf8mb3 to utf8mb4: What CONVERT TO CHARACTER SET Locks, Refuses and
  Silently Changes'
date: '2026-11-18'
source: https://dev.to/tbson87/mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes-3blj
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]'
- '[[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]'
- '[[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On MySQL 8.4.11, ALTER TABLE ... CONVERT TO CHARACTER SET utf8mb4 ran in place with writes allowed when…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On MySQL 8.4.11, ALTER TABLE ... CONVERT TO CHARACTER SET utf8mb4 ran in place with writes allowed when no converted column was indexed, and copied the table when one was: 9.3 seconds on 2,000,000 rows, with an INSERT waiting 7.8 of them. It is refused by a foreign key on a string column (error 3780), an index that would pass 3,072 bytes (3886 or 1071), a VARCHAR over 16,383 characters (1074) and values the new collation treats as equal (1062). When it runs, it turns TEXT into ME…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes-3blj

## Related notes
- [[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]
- [[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]
- [[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
