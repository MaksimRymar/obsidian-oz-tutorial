---
title: 'Case-Insensitive Email in PostgreSQL: citext, a lower() Index, or a Nondeterministic
  Collation?'
date: '2026-11-18'
source: https://dev.to/tbson87/case-insensitive-email-in-postgresql-citext-a-lower-index-or-a-nondeterministic-collation-a70
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
- '[[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]'
- '[[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]'
- '[[2026-10-20-round-tripping-tpc-ds-and-a-snowflake-feature-schema-through-a-database-diagram-what-snowflake-lost-and-what-we-fixed]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On PostgreSQL 18, put a nondeterministic collation on the email column: a plain UNIQUE , a plain WHERE e…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: On PostgreSQL 18, put a nondeterministic collation on the email column: a plain UNIQUE , a plain WHERE email = $1 , ON CONFLICT (email) and foreign keys all work, and LIKE now does too. A unique index on lower(email) only works for queries that also say lower() , and citext quietly turns case-sensitive when the parameter arrives typed as text . For a case-insensitive unique email on PostgreSQL 18, use a nondeterministic collation on the column. It is the only one of the three com…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/case-insensitive-email-in-postgresql-citext-a-lower-index-or-a-nondeterministic-collation-a70

## Related notes
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]
- [[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]
- [[2026-10-20-round-tripping-tpc-ds-and-a-snowflake-feature-schema-through-a-database-diagram-what-snowflake-lost-and-what-we-fixed]]
