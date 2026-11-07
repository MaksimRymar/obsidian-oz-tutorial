---
title: CREATE INDEX CONCURRENTLY Failed. The INVALID Index It Left Can Still Tax Every
  Write
date: '2026-11-07'
source: https://dev.to/gabrielanhaia/create-index-concurrently-failed-the-invalid-index-it-left-can-still-tax-every-write-2fnl
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]'
- '[[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]'
- '[[2026-11-02-your-agents-add-foreign-key-stalls-writes-on-two-tables-not-valid-then-validate]]'
- '[[2026-11-04-postgres-19-turns-jit-off-by-default-find-the-queries-that-were-paying-for-it]]'
- '[[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]'
- '[[2026-10-25-sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids]]'
status: unread
---

> **TL;DR:** Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and o…

## What’s new and why it matters
Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and other AI coding tools Me: xgabriel.com | GitHub You ask your coding agent for a unique index on users.email . It writes CREATE UNIQUE INDEX CONCURRENTLY , which is the right call on a live table. The deploy fails. The agent reruns the migration, gets told the index already exists, adds IF NOT EXISTS , and CI goes green. Weeks later someone runs \d users and sees the word INVALID…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gabrielanhaia/create-index-concurrently-failed-the-invalid-index-it-left-can-still-tax-every-write-2fnl

## Related notes
- [[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]
- [[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]
- [[2026-11-02-your-agents-add-foreign-key-stalls-writes-on-two-tables-not-valid-then-validate]]
- [[2026-11-04-postgres-19-turns-jit-off-by-default-find-the-queries-that-were-paying-for-it]]
- [[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]
- [[2026-10-25-sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids]]
