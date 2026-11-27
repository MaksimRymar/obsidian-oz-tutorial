---
title: 'PostgreSQL Rewrites Your CHECK Constraints: Which Schema Differences Are Real
  Drift'
date: '2026-11-27'
source: https://dev.to/tbson87/postgresql-rewrites-your-check-constraints-which-schema-differences-are-real-drift-56k3
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-18-mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes]]'
- '[[2026-11-27-soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working]]'
- '[[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: PostgreSQL keeps a parsed CHECK , not your text, so status IN ('pending', 'paid') comes back as = ANY (A…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: PostgreSQL keeps a parsed CHECK , not your text, so status IN ('pending', 'paid') comes back as = ANY (ARRAY[...]) and BETWEEN as two comparisons. Those are the same rule. A DEFAULT 'now' frozen to the moment the table was created, or a value whose case changed, is not. Compare database to database, never your migration's text to a dump. A schema diff that compares your migration's text with what the database prints will report CHECK constraints and defaults as changed even when…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/postgresql-rewrites-your-check-constraints-which-schema-differences-are-real-drift-56k3

## Related notes
- [[2026-11-18-mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes]]
- [[2026-11-27-soft-delete-vs-archive-table-which-one-keeps-your-foreign-keys-working]]
- [[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
