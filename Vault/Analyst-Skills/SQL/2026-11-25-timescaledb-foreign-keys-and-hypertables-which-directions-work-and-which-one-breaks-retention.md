---
title: 'TimescaleDB Foreign Keys and Hypertables: Which Directions Work, and Which
  One Breaks Retention'
date: '2026-11-25'
source: https://dev.to/tbson87/timescaledb-foreign-keys-and-hypertables-which-directions-work-and-which-one-breaks-retention-4h88
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A hypertable can reference a plain table, a plain table can reference a hypertable, and a hypertable can…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A hypertable can reference a plain table, a plain table can reference a hypertable, and a hypertable cannot reference a hypertable, itself included. The middle case is the trap: the key is accepted, and then drop_chunks and the retention policy refuse to drop chunks, even when no row points into them. Point the key at the plain entity table, such as devices , and keep the reading time as an ordinary column. A TimescaleDB hypertable can reference a plain table, and a plain table c…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/timescaledb-foreign-keys-and-hypertables-which-directions-work-and-which-one-breaks-retention-4h88

## Related notes
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
