---
title: 'Soft Delete vs Archive Table: Which One Keeps Your Foreign Keys Working'
date: '2026-11-27'
source: https://dev.to/tbson87/soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working-2k4a
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-11-27-natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Use a deleted_at column on a table other tables point at, such as products or users, and make those fore…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Use a deleted_at column on a table other tables point at, such as products or users, and make those foreign keys reference the surrogate id . Use an archive table for rows nothing references, where you want them physically out of the live table. Both fail in ways PostgreSQL will not warn you about: a soft-deleted row still accepts new references, and an archive copy written with SELECT * lands in the wrong columns after a schema change. A soft delete column and an archive table f…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working-2k4a

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-11-27-natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]
