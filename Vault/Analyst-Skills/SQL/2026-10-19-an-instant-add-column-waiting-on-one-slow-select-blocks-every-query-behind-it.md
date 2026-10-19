---
title: An Instant ADD COLUMN Waiting on One Slow SELECT Blocks Every Query Behind
  It
date: '2026-10-19'
source: https://dev.to/gabrielanhaia/an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it-367h
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]'
- '[[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]'
- '[[2026-10-17-your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe]]'
- '[[2026-10-18-let-ast-grep-do-the-rename-hand-claude-code-only-the-files-it-couldnt]]'
- '[[2026-09-29-one-long-select-one-alter-table-and-every-query-behind-them]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
status: unread
---

> **TL;DR:** Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and o…

## What’s new and why it matters
Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and other AI coding tools Me: xgabriel.com | GitHub Your migration adds one nullable column. That has always been a catalog change with no table rewrite, and since PostgreSQL 11 even a column with a constant default skips the rewrite. The ALTER TABLE docs say so directly: "In neither case is a rewrite of the table required." Then the deploy goes out and your API stops answering quer…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gabrielanhaia/an-instant-add-column-waiting-on-one-slow-select-blocks-every-query-behind-it-367h

## Related notes
- [[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]
- [[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]
- [[2026-10-17-your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe]]
- [[2026-10-18-let-ast-grep-do-the-rename-hand-claude-code-only-the-files-it-couldnt]]
- [[2026-09-29-one-long-select-one-alter-table-and-every-query-behind-them]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
