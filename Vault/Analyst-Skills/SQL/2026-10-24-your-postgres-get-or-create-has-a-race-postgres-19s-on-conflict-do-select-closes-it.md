---
title: Your Postgres Get-or-Create Has a Race. Postgres 19's ON CONFLICT DO SELECT
  Closes It
date: '2026-10-24'
source: https://dev.to/gabrielanhaia/your-postgres-get-or-create-has-a-race-postgres-19s-on-conflict-do-select-closes-it-720
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]'
- '[[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]'
- '[[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]'
- '[[2026-10-25-sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids]]'
- '[[2026-10-17-your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe]]'
- '[[2026-10-18-let-ast-grep-do-the-rename-hand-claude-code-only-the-files-it-couldnt]]'
status: unread
---

> **TL;DR:** Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and o…

## What’s new and why it matters
Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and other AI coding tools Me: xgabriel.com | GitHub Two requests to tag an article postgres arrive a few milliseconds apart. Both look up the tag. Neither finds it. Both insert it. One gets an id back. The other gets SQLSTATE 23505 , unique_violation , and your API returns a 500 for a request that did nothing wrong. Get-or-create is the most boring query in your codebase, and the ob…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gabrielanhaia/your-postgres-get-or-create-has-a-race-postgres-19s-on-conflict-do-select-closes-it-720

## Related notes
- [[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]
- [[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]
- [[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]
- [[2026-10-25-sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids]]
- [[2026-10-17-your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe]]
- [[2026-10-18-let-ast-grep-do-the-rename-hand-claude-code-only-the-files-it-couldnt]]
