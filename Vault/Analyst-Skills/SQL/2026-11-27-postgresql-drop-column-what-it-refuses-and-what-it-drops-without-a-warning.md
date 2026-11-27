---
title: 'PostgreSQL DROP COLUMN: What It Refuses, and What It Drops Without a Warning'
date: '2026-11-27'
source: https://dev.to/tbson87/postgresql-drop-column-what-it-refuses-and-what-it-drops-without-a-warning-19ko
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-11-27-soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-11-27-natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A plain DROP COLUMN in PostgreSQL stops only for objects outside the table's own keys: views, other tabl…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A plain DROP COLUMN in PostgreSQL stops only for objects outside the table's own keys: views, other tables' foreign keys, generated columns and row-level security policies. Every index, unique constraint, CHECK and statistics object that uses the column is dropped with it, with no notice, including a partial index on a different column whose WHERE names it. CASCADE removes the blockers too, and a policy removed that way can leave the table showing zero rows to your application. D…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/postgresql-drop-column-what-it-refuses-and-what-it-drops-without-a-warning-19ko

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-11-27-soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-11-27-natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
