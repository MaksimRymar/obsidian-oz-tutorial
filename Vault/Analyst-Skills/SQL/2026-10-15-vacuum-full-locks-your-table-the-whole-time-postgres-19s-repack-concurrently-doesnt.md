---
title: VACUUM FULL Locks Your Table the Whole Time. Postgres 19's REPACK CONCURRENTLY
  Doesn't
date: '2026-10-15'
source: https://dev.to/gabrielanhaia/vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt-186
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
- '[[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]'
- '[[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]'
- '[[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]'
- '[[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]'
status: unread
---

> **TL;DR:** Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and o…

## What’s new and why it matters
Book: Database Playbook Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and other AI coding tools Me: xgabriel.com | GitHub You deleted 80% of a 200-million-row table and the disk didn't notice. Autovacuum ran. The file stayed the same size. The built-in way to hand that space back has been VACUUM FULL (or its sibling CLUSTER ). It takes an ACCESS EXCLUSIVE lock and holds it for the entire rewrite, so every read and write on the table waits until it's d…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gabrielanhaia/vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt-186

## Related notes
- [[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]
- [[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]
- [[2026-09-08-postgres-autovacuum-isnt-keeping-up-diagnosing-bloat-long-transactions-and-wraparound-warnings]]
- [[2026-10-15-sql-joins-explained-with-one-tiny-dataset-plus-5-interview-questions]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-10-sql-indexes-explained-for-people-who-just-got-yelled-at-by-a-slow-dashboard]]
