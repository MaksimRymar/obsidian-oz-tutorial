---
title: 'How to Auto-Update an updated_at Column: MySQL ON UPDATE vs a Database Trigger
  vs the ORM'
date: '2026-10-22'
source: https://dev.to/tbson87/how-to-auto-update-an-updatedat-column-mysql-on-update-vs-a-database-trigger-vs-the-orm-2eik
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-10-01-changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes]]'
- '[[2026-08-21-column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A DEFAULT CURRENT_TIMESTAMP fills updated_at only once, at insert. On MySQL, add ON UPDATE CURRENT_TIMES…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A DEFAULT CURRENT_TIMESTAMP fills updated_at only once, at insert. On MySQL, add ON UPDATE CURRENT_TIMESTAMP to the column; on PostgreSQL, SQL Server and SQLite, write a trigger; or let the ORM set it, which works on every database but misses every write that does not go through the ORM. Pick the database side when scripts, admins or other services write to the table, and the ORM side when only one application does. Whether updated_at should be set by the database or by the ORM c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/how-to-auto-update-an-updatedat-column-mysql-on-update-vs-a-database-trigger-vs-the-orm-2eik

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-10-01-changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes]]
- [[2026-08-21-column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
