---
title: 'Natural Key vs Surrogate Key: Which One Should a Foreign Key Reference?'
date: '2026-11-27'
source: https://dev.to/tbson87/natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference-2l0i
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-11-18-mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]'
- '[[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]'
- '[[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]'
status: unread
---

> **TL;DR:** Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Point foreign keys at a surrogate id whenever the natural value can change, which covers SKUs, emails, u…

## What’s new and why it matters
Disclosure: I build Schemity , a desktop ERD tool - this post is from our blog and uses it for the examples. TL;DR: Point foreign keys at a surrogate id whenever the natural value can change, which covers SKUs, emails, usernames and product codes, and keep the natural value UNIQUE on its own table. A natural-key foreign key turns every rename into a rewrite of the child rows, including history that should have kept the old value. A natural key is a reasonable target only for a short, stable standard code, such as an ISO country or currency code. On MySQL a string foreign key must also share th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/tbson87/natural-key-vs-surrogate-key-which-one-should-a-foreign-key-reference-2l0i

## Related notes
- [[2026-11-18-mysql-utf8mb3-to-utf8mb4-what-convert-to-character-set-locks-refuses-and-silently-changes]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-11-03-mysql-alter-table-which-changes-lock-the-table-and-how-to-make-one-fail-instead-of-copying]]
- [[2026-11-11-mysql-enum-vs-check-constraint-which-value-list-changes-copy-the-table]]
- [[2026-10-21-sql-server-int-to-bigint-primary-key-four-ways-to-change-it-and-what-each-one-costs]]
