---
title: 'PostgreSQL serial vs identity: Which to Use, and How to Convert Old serial
  Columns'
date: '2026-10-05'
source: https://dev.to/tbson87/postgresql-serial-vs-identity-which-to-use-and-how-to-convert-old-serial-columns-4h59
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Use GENERATED ALWAYS AS IDENTITY for new tables. serial is a shortcut for a separate sequence plus a def…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Use GENERATED ALWAYS AS IDENTITY for new tables. serial is a shortcut for a separate sequence plus a default, so the column and its counter drift apart: an explicit id breaks the next insert, a widened key still stops at 2,147,483,647, and a copied table shares the counter. An existing serial key converts to identity in a few milliseconds, with no table rewrite. For a new PostgreSQL table, use an identity column: id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY . serial still w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/postgresql-serial-vs-identity-which-to-use-and-how-to-convert-old-serial-columns-4h59

## Related notes
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-10-01-adding-a-not-null-column-to-a-large-postgresql-table-constant-default-backfill-or-not-valid]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
