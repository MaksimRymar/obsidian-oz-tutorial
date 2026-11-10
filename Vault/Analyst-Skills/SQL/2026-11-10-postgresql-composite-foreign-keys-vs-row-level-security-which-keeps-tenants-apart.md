---
title: 'PostgreSQL Composite Foreign Keys vs Row-Level Security: Which Keeps Tenants
  Apart?'
date: '2026-11-10'
source: https://dev.to/tbson87/postgresql-composite-foreign-keys-vs-row-level-security-which-keeps-tenants-apart-2h5d
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-10-13-how-to-change-a-primary-key-that-foreign-keys-already-point-at]]'
- '[[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Row-level security decides which rows a session can read and write, but PostgreSQL foreign key checks by…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Row-level security decides which rows a session can read and write, but PostgreSQL foreign key checks bypass it, so an Acme task can still be assigned to a Globex member the session cannot even see. A composite foreign key such as (company_id, assignee_id) referencing members (company_id, id) makes the database itself refuse that row. They close different holes: keep the composite keys for references between tenant tables, and add row-level security when queries need a second lin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/tbson87/postgresql-composite-foreign-keys-vs-row-level-security-which-keeps-tenants-apart-2h5d

## Related notes
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-10-13-how-to-change-a-primary-key-that-foreign-keys-already-point-at]]
- [[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]
