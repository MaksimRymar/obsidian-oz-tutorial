---
title: 'Postgres Let Two Rows Through a Unique Index: The glibc Collation Trap After
  an OS Upgrade'
date: '2026-10-05'
source: https://dev.to/libme/postgres-let-two-rows-through-a-unique-index-the-glibc-collation-trap-after-an-os-upgrade-3ad6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
status: unread
---

> **TL;DR:** If a unique index suddenly tolerates duplicates, or WHERE email = ... misses a row that a sequential scan finds, the index is sorted by collation rules that no longer match what your OS provides. That happens when the C…

## What’s new and why it matters
If a unique index suddenly tolerates duplicates, or WHERE email = ... misses a row that a sequential scan finds, the index is sorted by collation rules that no longer match what your OS provides. That happens when the C library's sort order changes — most famously in glibc 2.28 — and it is not a Postgres bug, a replication bug, or a bad disk. The fix is to rebuild every index on a text column, then tell Postgres which collation version it is now running against. I hit this after the most boring change imaginable: bumping a Docker base image from Debian 10 to Debian 12 for a staging database. T…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/libme/postgres-let-two-rows-through-a-unique-index-the-glibc-collation-trap-after-an-os-upgrade-3ad6

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
