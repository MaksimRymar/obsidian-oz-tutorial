---
title: Sentry and Mandrill Both Went Down When Postgres Ran Out of Transaction IDs
date: '2026-10-25'
source: https://dev.to/gabrielanhaia/sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids-f11
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]'
- '[[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]'
- '[[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]'
- '[[2026-10-17-your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe]]'
- '[[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]'
- '[[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]'
status: unread
---

> **TL;DR:** Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and o…

## What’s new and why it matters
Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and other AI coding tools Me: xgabriel.com | GitHub On Monday, July 20, 2015, Sentry was "down for most of the US working day" . Postgres had stopped accepting writes on purpose, and it would not take another one until a vacuum finished. Three and a half years later, at 05:35 UTC on February 4, 2019, one of the Postgres databases behind Mailchimp's transactional email service Mandri…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gabrielanhaia/sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids-f11

## Related notes
- [[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]
- [[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]
- [[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]
- [[2026-10-17-your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe]]
- [[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]
- [[2026-10-08-your-postgres-id-columns-will-run-out-of-numbers-heres-a-10-second-check-and-the-trap-that-hides-it]]
