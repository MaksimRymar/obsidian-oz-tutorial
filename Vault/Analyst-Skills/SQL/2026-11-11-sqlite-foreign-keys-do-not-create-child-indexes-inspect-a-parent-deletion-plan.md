---
title: 'SQLite foreign keys do not create child indexes: inspect a parent deletion
  plan'
date: '2026-11-11'
source: https://dev.to/hirodeath/sqlite-foreign-keys-do-not-create-child-indexes-inspect-a-parent-deletion-plan-1lm7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]'
- '[[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]'
- '[[2026-11-06-how-to-read-a-sql-server-execution-plan-beginners-guide]]'
- '[[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]'
- '[[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
status: unread
---

> **TL;DR:** Writing REFERENCES parent(id) in SQLite did not automatically create an index on the child's reference column. Referential-integrity checks still worked, but finding children during a parent deletion used a SCAN. The exi…

## What’s new and why it matters
Writing REFERENCES parent(id) in SQLite did not automatically create an index on the child's reference column. Referential-integrity checks still worked, but finding children during a parent deletion used a SCAN. The existence of a foreign key and the access path used to find referencing children need separate checks. This experiment compared index lists and an actual DELETE plan in SQLite 3.53.1. Enable foreign keys and inspect the index lists Each condition used a fresh in-memory database through Python's sqlite3 module. The connection enabled autocommit, and foreign_keys was turned ON outsi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hirodeath/sqlite-foreign-keys-do-not-create-child-indexes-inspect-a-parent-deletion-plan-1lm7

## Related notes
- [[2026-10-03-replacing-deep-offset-pagination-in-d1-rows-read-and-inserts-between-pages]]
- [[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]
- [[2026-11-06-how-to-read-a-sql-server-execution-plan-beginners-guide]]
- [[2026-08-12-can-you-run-hybrid-search-on-one-database-yes-heres-how-cratedb-does-it]]
- [[2026-10-24-how-to-find-missing-ids-between-two-lists-and-get-the-sql-for-free]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
