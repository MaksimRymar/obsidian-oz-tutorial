---
title: How to Find the Postgres Indexes Your Planner Never Picks (I Found 20 of 51)
date: '2026-05-09'
source: https://dev.to/alimafana/postgres-tells-you-your-query-was-slow-not-which-index-was-wasted-171g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
status: unread
---

> **TL;DR:** TL;DR: Postgres has pg_stat_user_indexes . It tells you how many times each index was scanned. It does not tell you whether the slow query you're chasing actually used the index you added for it, or whether you're mainta…

## What’s new and why it matters
TL;DR: Postgres has pg_stat_user_indexes . It tells you how many times each index was scanned. It does not tell you whether the slow query you're chasing actually used the index you added for it, or whether you're maintaining indexes the planner never picks. I built a 3-file analyzer — a query wrapper, a logs table, a dashboard — and the first time I ran it against my own production database, 20 of my 51 indexes had never been scanned. 78% of my total index disk was being maintained for nothing. The Gap in Postgres's Stats Open pg_stat_user_indexes right now: SELECT indexrelname , idx_scan , i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alimafana/postgres-tells-you-your-query-was-slow-not-which-index-was-wasted-171g

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-24-stop-tuning-blind-query-observability-as-the-foundation-for-database-optimization]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
