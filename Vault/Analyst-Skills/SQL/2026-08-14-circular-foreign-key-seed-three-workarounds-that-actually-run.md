---
title: 'Circular Foreign Key Seed: Three Workarounds That Actually Run'
date: '2026-08-14'
source: https://dev.to/mikh-shytsko/circular-foreign-key-seed-three-workarounds-that-actually-run-57ga
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-08-14-how-to-seed-a-neon-database-psql-prisma-drizzle]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** To seed two Postgres tables that reference each other, mark the foreign keys DEFERRABLE INITIALLY IMMEDIATE and wrap the inserts in a transaction that issues SET CONSTRAINTS ALL DEFERRED — Postgres then validates both FK…

## What’s new and why it matters
To seed two Postgres tables that reference each other, mark the foreign keys DEFERRABLE INITIALLY IMMEDIATE and wrap the inserts in a transaction that issues SET CONSTRAINTS ALL DEFERRED — Postgres then validates both FKs at COMMIT instead of after each row. -- both foreign keys must already be declared DEFERRABLE (see Workaround 1) BEGIN ; SET CONSTRAINTS ALL DEFERRED ; INSERT INTO organizations ( id , name , primary_owner_id ) VALUES ( 1 , 'Acme' , 1 ); INSERT INTO employees ( id , full_name , organization_id ) VALUES ( 1 , 'Ada' , 1 ); COMMIT ; A circular foreign key seed is the case where…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mikh-shytsko/circular-foreign-key-seed-three-workarounds-that-actually-run-57ga

## Related notes
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-08-14-how-to-seed-a-neon-database-psql-prisma-drizzle]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
