---
title: 'Agent-Written Down Migrations or Human Recovery Runbooks: A Rehearsal-First
  Debate'
date: '2026-09-14'
source: https://dev.to/dataio_4921/agent-written-down-migrations-or-human-recovery-runbooks-a-rehearsal-first-debate-4jcf
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]'
- '[[2026-09-09-diagnostic-findings-or-auto-rewrites-a-gate-for-sql-review-agents]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** Consider a composite of the failure reports that keep circulating in Postgres incident threads, rather than a logged incident from my own systems. A migration adds a column and a backfill, an AI reviewer approves the up-…

## What’s new and why it matters
Consider a composite of the failure reports that keep circulating in Postgres incident threads, rather than a logged incident from my own systems. A migration adds a column and a backfill, an AI reviewer approves the up-path, and nobody authors the down-path at all. Three hours later the backfill is still running, the lock queue is growing, and the only rollback plan left is last night's base backup. The interesting failure is not that the model was wrong; it is that nobody defined who owned the reversal before the migration started. That gap is what this post argues about, in the same debate…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataio_4921/agent-written-down-migrations-or-human-recovery-runbooks-a-rehearsal-first-debate-4jcf

## Related notes
- [[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]
- [[2026-09-09-diagnostic-findings-or-auto-rewrites-a-gate-for-sql-review-agents]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
