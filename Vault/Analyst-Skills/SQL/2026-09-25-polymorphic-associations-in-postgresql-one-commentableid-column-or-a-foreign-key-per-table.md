---
title: 'Polymorphic Associations in PostgreSQL: One commentable_id Column or a Foreign
  Key per Table?'
date: '2026-09-25'
source: https://dev.to/tbson87/polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table-5297
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-08-21-column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-30-on-delete-cascade-is-invisible-in-your-erd-and-in-your-database-logs]]'
- '[[2026-07-22-many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A polymorphic association stores a type name and an id in two columns, and PostgreSQL has no foreign key…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A polymorphic association stores a type name and an id in two columns, and PostgreSQL has no foreign key that can point at a different table on each row, so nothing stops orphans or typos. For a small fixed set of parents, use one nullable foreign key per parent with a CHECK that exactly one is set; for many parents, use a shared supertype table. Keep the polymorphic pair only when the set of parents is open-ended, and document it in the ERD as virtual relations, which is how Sch…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table-5297

## Related notes
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-08-21-column-comments-in-postgresql-and-mysql-how-to-document-columns-without-a-migration]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-30-on-delete-cascade-is-invisible-in-your-erd-and-in-your-database-logs]]
- [[2026-07-22-many-to-many-in-an-erd-shouldnt-mean-hand-building-the-junction-table]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
