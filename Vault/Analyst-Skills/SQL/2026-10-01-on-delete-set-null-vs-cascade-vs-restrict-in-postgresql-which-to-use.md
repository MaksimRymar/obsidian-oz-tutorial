---
title: 'ON DELETE SET NULL vs CASCADE vs RESTRICT in PostgreSQL: Which to Use'
date: '2026-10-01'
source: https://dev.to/tbson87/on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use-1n6l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-07-30-on-delete-cascade-is-invisible-in-your-erd-and-in-your-database-logs]]'
- '[[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]'
- '[[2026-10-01-changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Pick the action by what the child row means once its parent is gone: CASCADE when it means nothing, SET…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Pick the action by what the child row means once its parent is gone: CASCADE when it means nothing, SET NULL when it stays valid with the link removed, and RESTRICT or NO ACTION when it is a record that must not change behind anyone's back. SET NULL is the one PostgreSQL accepts and then refuses at delete time, if the column is NOT NULL , a check needs the value, or the key is composite and nulls a tenant column along with it. A foreign key's ON DELETE action should follow from o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use-1n6l

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-07-30-on-delete-cascade-is-invisible-in-your-erd-and-in-your-database-logs]]
- [[2026-09-27-postgresql-generated-column-vs-trigger-which-to-use-for-a-derived-column]]
- [[2026-10-01-changing-a-column-type-in-sqlite-the-table-rebuild-and-what-it-deletes]]
