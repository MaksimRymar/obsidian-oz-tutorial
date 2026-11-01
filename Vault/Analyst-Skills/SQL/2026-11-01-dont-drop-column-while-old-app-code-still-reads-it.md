---
title: Don't DROP COLUMN while old app code still reads it
date: '2026-11-01'
source: https://dev.to/labyrinthlab/dont-drop-column-while-old-app-code-still-reads-it-g7e
domain: SQL
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-10-15-the-4-kinds-of-alter-table-that-cause-production-incidents-and-a-5-minute-review-for-each]]'
- '[[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]'
- '[[2026-07-31-why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
status: unread
---

> **TL;DR:** Here is the failure. You clean up a schema: ALTER TABLE users DROP COLUMN legacy_status ; The migration applies. New code is fine. Mid-deploy, an old app instance (or a Sidekiq worker that hasn't restarted yet) still run…

## What’s new and why it matters
Here is the failure. You clean up a schema: ALTER TABLE users DROP COLUMN legacy_status ; The migration applies. New code is fine. Mid-deploy, an old app instance (or a Sidekiq worker that hasn't restarted yet) still runs a query that selects legacy_status . Rails may also have a cached schema that still lists the column. Requests start failing with "column does not exist" until every process has the new code and a fresh schema cache. This is not a theoretical edge case. GitLab's "Avoiding downtime in migrations" guide opens the "Dropping columns" section with the same point: running processes…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/labyrinthlab/dont-drop-column-while-old-app-code-still-reads-it-g7e

## Related notes
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-10-15-the-4-kinds-of-alter-table-that-cause-production-incidents-and-a-5-minute-review-for-each]]
- [[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]
- [[2026-07-31-why-ai-keeps-inventing-columns-that-dont-exist-and-how-to-stop-it]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
