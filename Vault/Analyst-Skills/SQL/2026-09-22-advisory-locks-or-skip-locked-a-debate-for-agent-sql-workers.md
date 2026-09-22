---
title: 'Advisory Locks or SKIP LOCKED: A Debate for Agent SQL Workers'
date: '2026-09-22'
source: https://dev.to/dataio_4921/advisory-locks-or-skip-locked-a-debate-for-agent-sql-workers-4fp4
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-16-parser-gates-or-runtime-guards-a-debate-for-agent-written-sql]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-13-single-pass-critique-or-repair-loop-a-debate-for-sql-review-agents]]'
- '[[2026-09-04-when-index-hit-stats-go-stale-two-positions-for-sql-review-agents]]'
- '[[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
status: unread
---

> **TL;DR:** The following reconstruction is a composite queue-worker failure, not a report from a named production tenant. A checkout worker queue stalled after midnight when three agent-written jobs targeted the same unpaid-order s…

## What’s new and why it matters
The following reconstruction is a composite queue-worker failure, not a report from a named production tenant. A checkout worker queue stalled after midnight when three agent-written jobs targeted the same unpaid-order slice. Each session selected candidate rows without a skip clause, then waited on locks that never yielded under replica lag. The parser accepted every statement, so the usual syntax gate never fired during the pre-promotion review. The on-call thread split into two durable camps with different promotion rules for the same queue table. One camp wanted named advisory locks so ove…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/dataio_4921/advisory-locks-or-skip-locked-a-debate-for-agent-sql-workers-4fp4

## Related notes
- [[2026-09-16-parser-gates-or-runtime-guards-a-debate-for-agent-written-sql]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-13-single-pass-critique-or-repair-loop-a-debate-for-sql-review-agents]]
- [[2026-09-04-when-index-hit-stats-go-stale-two-positions-for-sql-review-agents]]
- [[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
