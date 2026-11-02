---
title: Your Agent's ADD FOREIGN KEY Stalls Writes on Two Tables. NOT VALID, Then VALIDATE
date: '2026-11-02'
source: https://dev.to/gabrielanhaia/your-agents-add-foreign-key-stalls-writes-on-two-tables-not-valid-then-validate-586e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]'
- '[[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]'
- '[[2026-10-17-your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe]]'
- '[[2026-10-24-your-postgres-get-or-create-has-a-race-postgres-19s-on-conflict-do-select-closes-it]]'
- '[[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]'
- '[[2026-10-25-sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids]]'
status: unread
---

> **TL;DR:** Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and o…

## What’s new and why it matters
Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and other AI coding tools Me: xgabriel.com | GitHub Checkout writes hang in the middle of a deploy. The only change in that deploy is the migration your coding agent wrote when you asked it to link orders to customers, and it looked textbook: ALTER TABLE orders ADD FOREIGN KEY (customer_id) REFERENCES customers (id); . Per the PostgreSQL 18 ALTER TABLE docs , ADD FOREIGN KEY takes a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gabrielanhaia/your-agents-add-foreign-key-stalls-writes-on-two-tables-not-valid-then-validate-586e

## Related notes
- [[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]
- [[2026-10-19-an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it]]
- [[2026-10-17-your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe]]
- [[2026-10-24-your-postgres-get-or-create-has-a-race-postgres-19s-on-conflict-do-select-closes-it]]
- [[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]
- [[2026-10-25-sentry-and-mandrill-both-went-down-when-postgres-ran-out-of-transaction-ids]]
