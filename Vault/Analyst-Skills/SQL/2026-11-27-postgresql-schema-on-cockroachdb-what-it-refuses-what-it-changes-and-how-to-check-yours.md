---
title: 'PostgreSQL Schema on CockroachDB: What It Refuses, What It Changes, and How
  to Check Yours'
date: '2026-11-27'
source: https://dev.to/tbson87/postgresql-schema-on-cockroachdb-what-it-refuses-what-it-changes-and-how-to-check-yours-33p0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-11-27-natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference]]'
- '[[2026-11-18-mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A PostgreSQL schema rarely runs on CockroachDB unchanged. CockroachDB v26.3 has no range types, money ,…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: A PostgreSQL schema rarely runs on CockroachDB unchanged. CockroachDB v26.3 has no range types, money , xml or point , no C collation, no DEFERRABLE foreign keys, and no BRIN, SP-GiST or EXCLUDE . It also changes what it accepts: integer becomes 64-bit, and a table created with serial gets 19-digit ids, past what JavaScript can hold exactly. Read the schema for these before moving any data. CockroachDB accepts most of a PostgreSQL schema, refuses a specific list of types, indexes…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/postgresql-schema-on-cockroachdb-what-it-refuses-what-it-changes-and-how-to-check-yours-33p0

## Related notes
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-11-27-natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference]]
- [[2026-11-18-mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
