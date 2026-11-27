---
title: 'MySQL Cannot Drop Index Needed in a Foreign Key Constraint: Which Fix to Use'
date: '2026-11-27'
source: https://dev.to/tbson87/mysql-cannot-drop-index-needed-in-a-foreign-key-constraint-which-fix-to-use-4c9e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
- '[[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-11-27-natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: MySQL refuses to drop the last index whose leading columns hold a foreign key's columns, and turning off…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: MySQL refuses to drop the last index whose leading columns hold a foreign key's columns, and turning off foreign_key_checks does not change that on MySQL 8.4. If the foreign key is going too, drop it and the index in one ALTER TABLE . If the key stays, add the replacement index in the same statement as the drop. The trap is an index MySQL swapped in for its own without telling you, which turns a routine rollback into error 1553. MySQL error 1553, Cannot drop index 'customer_id':…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/mysql-cannot-drop-index-needed-in-a-foreign-key-constraint-which-fix-to-use-4c9e

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
- [[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-11-27-natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference]]
