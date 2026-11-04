---
title: Postgres 19 Turns JIT Off by Default. Find the Queries That Were Paying for
  It
date: '2026-11-04'
source: https://dev.to/gabrielanhaia/postgres-19-turns-jit-off-by-default-find-the-queries-that-were-paying-for-it-ljm
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]'
- '[[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]'
- '[[2026-11-02-your-agents-add-foreign-key-stalls-writes-on-two-tables-not-valid-then-validate]]'
- '[[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]'
- '[[2026-10-25-sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids]]'
- '[[2026-10-24-your-postgres-get-or-create-has-a-race-postgres-19s-on-conflict-do-select-closes-it]]'
status: unread
---

> **TL;DR:** Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and o…

## What’s new and why it matters
Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and other AI coding tools Me: xgabriel.com | GitHub A couple of extra INSERTs land in a table. The planner's cost estimate for a query that used to finish in a few milliseconds creeps over 100,000. Now Postgres compiles that query with LLVM before running it, and most of its runtime goes to compilation. Nobody changed the query. That scenario comes almost word for word from the comm…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gabrielanhaia/postgres-19-turns-jit-off-by-default-find-the-queries-that-were-paying-for-it-ljm

## Related notes
- [[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]
- [[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]
- [[2026-11-02-your-agents-add-foreign-key-stalls-writes-on-two-tables-not-valid-then-validate]]
- [[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]
- [[2026-10-25-sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids]]
- [[2026-10-24-your-postgres-get-or-create-has-a-race-postgres-19s-on-conflict-do-select-closes-it]]
