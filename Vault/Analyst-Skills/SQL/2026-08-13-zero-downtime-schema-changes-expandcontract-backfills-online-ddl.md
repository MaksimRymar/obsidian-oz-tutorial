---
title: 'Zero-Downtime Schema Changes: Expand/Contract, Backfills & Online DDL'
date: '2026-08-13'
source: https://dev.to/gowthampotureddi/zero-downtime-schema-changes-expandcontract-backfills-online-ddl-c92
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
status: unread
---

> **TL;DR:** zero-downtime schema changes are the difference between shipping a NOT NULL column on a Friday afternoon and a 40-minute outage that pages the whole on-call rotation — and they are the single operation that separates eng…

## What’s new and why it matters
zero-downtime schema changes are the difference between shipping a NOT NULL column on a Friday afternoon and a 40-minute outage that pages the whole on-call rotation — and they are the single operation that separates engineers who have actually run a migration against a busy multi-billion-row table from those who have only ever ALTER -ed a laptop database with ten rows in it. Every column you add, every type you widen, every constraint you tighten, every column you rename or drop has to reach production while the application keeps reading and writing at full throughput, while a rolling deploy…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/zero-downtime-schema-changes-expandcontract-backfills-online-ddl-c92

## Related notes
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
