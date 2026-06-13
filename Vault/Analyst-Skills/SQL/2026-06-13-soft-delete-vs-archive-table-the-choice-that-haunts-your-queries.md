---
title: 'Soft Delete vs Archive Table: The Choice That Haunts Your Queries'
date: '2026-06-13'
source: https://dev.to/gabrielanhaia/soft-delete-vs-archive-table-the-choice-that-haunts-your-queries-2n8k
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-06-08-retention-cohort-analysis-with-plain-sql]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]'
- '[[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]'
status: unread
---

> **TL;DR:** Book: Database Playbook: Choosing the Right Store for Every System You Build Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub —…

## What’s new and why it matters
Book: Database Playbook: Choosing the Right Store for Every System You Build Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and other AI coding tools Me: xgabriel.com | GitHub Someone on your team added a deleted_at column three years ago. It felt safe. Nothing gets destroyed, an accidental delete is one UPDATE away from recovery, and the product manager who asked for "undo" stopped asking. Now every query in the codebase carries the same tail: AND del…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gabrielanhaia/soft-delete-vs-archive-table-the-choice-that-haunts-your-queries-2n8k

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-06-08-retention-cohort-analysis-with-plain-sql]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]
- [[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]
