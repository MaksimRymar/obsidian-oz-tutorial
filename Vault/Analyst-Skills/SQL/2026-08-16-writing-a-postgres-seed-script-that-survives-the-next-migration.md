---
title: Writing a Postgres Seed Script That Survives the Next Migration
date: '2026-08-16'
source: https://dev.to/mikh-shytsko/writing-a-postgres-seed-script-that-survives-the-next-migration-37a9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
- '[[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** TL;DR: A seed script is a SQL or code file ( seed.sql , seed.ts ) that inserts a known set of rows into a Postgres database after migrations run. A good one orders inserts by foreign key, stays idempotent with ON CONFLIC…

## What’s new and why it matters
TL;DR: A seed script is a SQL or code file ( seed.sql , seed.ts ) that inserts a known set of rows into a Postgres database after migrations run. A good one orders inserts by foreign key, stays idempotent with ON CONFLICT DO NOTHING , runs in a transaction, and resets sequences at the end. You're staring at an empty Postgres database - maybe it's a new project, maybe it's a contributor's first day, maybe a migration just nuked the dev DB and the existing seed file no longer applies cleanly. Either way, you're about to write or rewrite a postgres seed script, the file the README tells everyone…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mikh-shytsko/writing-a-postgres-seed-script-that-survives-the-next-migration-37a9

## Related notes
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
- [[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
