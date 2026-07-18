---
title: Five schema-design habits that look harmless in a migration file — unbounded
  VAR
date: '2026-07-17'
source: https://dev.to/philip_mcclarence_2ef9475/five-schema-design-habits-that-look-harmless-in-a-migration-file-unbounded-var-3d93
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-05-23-create-table-alter-table-in-sql-schema-design-for-data-engineers]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
- '[[2026-03-06-5-database-design-mistakes-i-keep-seeing-and-how-to-catch-them-early]]'
- '[[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** Five schema mistakes I keep finding in migration files. Each one zero alarms, zero errors, and starts costing you real pain once tables cross a few million rows. Here’s the quick list—then a deep dive into why they hurt…

## What’s new and why it matters
Five schema mistakes I keep finding in migration files. Each one zero alarms, zero errors, and starts costing you real pain once tables cross a few million rows. Here’s the quick list—then a deep dive into why they hurt and exactly how to fix them. For a visual whiteboard walk‑through of how these patterns degrade storage and memory at the hardware level, see the full session on the MyDBA YouTube channel . TL;DR — The 5 Mistakes and Their Fixes Mistake Why it hurts at scale The 5‑Minute Fix Unbounded VARCHAR / TEXT Large column values can cause out‑of‑line TOAST storage, potentially affecting…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/five-schema-design-habits-that-look-harmless-in-a-migration-file-unbounded-var-3d93

## Related notes
- [[2026-05-23-create-table-alter-table-in-sql-schema-design-for-data-engineers]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
- [[2026-03-06-5-database-design-mistakes-i-keep-seeing-and-how-to-catch-them-early]]
- [[2026-05-11-five-sql-patterns-ai-agents-get-wrong-and-how-to-fix-them]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
