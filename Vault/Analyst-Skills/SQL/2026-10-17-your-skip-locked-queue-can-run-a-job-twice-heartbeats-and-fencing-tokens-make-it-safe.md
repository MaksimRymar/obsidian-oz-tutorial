---
title: Your SKIP LOCKED Queue Can Run a Job Twice. Heartbeats and Fencing Tokens Make
  It Safe
date: '2026-10-17'
source: https://dev.to/gabrielanhaia/your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe-34l4
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]'
- '[[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-09-29-one-long-select-one-alter-table-and-every-query-behind-them]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** Book: Event-Driven Architecture Pocket Guide Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship w…

## What’s new and why it matters
Book: Event-Driven Architecture Pocket Guide Also by me: Thinking in Go (2-book series) — Complete Guide to Go Programming + Hexagonal Architecture in Go My project: Hermes IDE | GitHub — an IDE for developers who ship with Claude Code and other AI coding tools Me: xgabriel.com | GitHub Say your receipt job renders a PDF and emails it. It usually takes 20 seconds, and the worker's lease on the job is 30. Then one morning the PDF service is slow, the job takes 45 seconds, and a customer gets two receipts. Nothing crashed and nothing was logged: two workers ran the same job at once, each doing e…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/gabrielanhaia/your-skip-locked-queue-can-run-a-job-twice-heartbeats-and-fencing-tokens-make-it-safe-34l4

## Related notes
- [[2026-10-15-vacuum-full-locks-your-table-the-whole-time-postgres-19s-repack-concurrently-doesnt]]
- [[2026-06-13-soft-delete-vs-archive-table-the-choice-that-haunts-your-queries]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-09-29-one-long-select-one-alter-table-and-every-query-behind-them]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
