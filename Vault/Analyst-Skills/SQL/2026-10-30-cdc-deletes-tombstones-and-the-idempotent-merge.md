---
title: CDC Deletes, Tombstones and the Idempotent MERGE
date: '2026-10-30'
source: https://dev.to/pipelinewhiteboard/cdc-deletes-tombstones-and-the-idempotent-merge-3cde
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
status: unread
---

> **TL;DR:** Order 1042 was deleted at 14:10. At 15:00 it's back in the warehouse, marked shipped . Nobody re-created it. A retried batch did. This is Part 4 of CDC in Production . In Part 3 we caught silent data loss and repaired it…

## What’s new and why it matters
Order 1042 was deleted at 14:10. At 15:00 it's back in the warehouse, marked shipped . Nobody re-created it. A retried batch did. This is Part 4 of CDC in Production . In Part 3 we caught silent data loss and repaired it by re-sending changes. Crashes re-send changes too. So this post covers the order CDC events really arrive in, how deletes and tombstones work, and a Snowflake MERGE that gets the right answer even when an event shows up twice, or late. Prefer to watch? Here's the 7-minute video version with animated diagrams: Video link: CDC Deletes, Tombstones and the Idempotent MERGE The or…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pipelinewhiteboard/cdc-deletes-tombstones-and-the-idempotent-merge-3cde

## Related notes
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-10-29-isolation-levels-how-the-last-item-in-stock-gets-sold-twice]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
