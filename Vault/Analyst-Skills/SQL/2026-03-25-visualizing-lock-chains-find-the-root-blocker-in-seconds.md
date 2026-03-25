---
title: 'Visualizing Lock Chains: Find the Root Blocker in Seconds'
date: '2026-03-25'
source: https://dev.to/philip_mcclarence_2ef9475/visualizing-lock-chains-find-the-root-blocker-in-seconds-1397
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-03-08-how-to-find-and-kill-long-running-queries-in-sql-server]]'
- '[[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-03-16-why-alembic-is-basically-git-for-your-database-and-why-you-need-it]]'
status: unread
---

> **TL;DR:** Visualizing Lock Chains: Find the Root Blocker in Seconds Every DBA has lived this nightmare at least once: you kill the session that appears to be blocking everything, and nothing improves. The chain just keeps growing.…

## What’s new and why it matters
Visualizing Lock Chains: Find the Root Blocker in Seconds Every DBA has lived this nightmare at least once: you kill the session that appears to be blocking everything, and nothing improves. The chain just keeps growing. The reason is that lock chains in PostgreSQL are not flat — they are trees, and you were cutting a branch instead of pulling the root. The Problem Session A is blocked. You check pg_locks and find Session B holds the conflicting lock. You terminate Session B, but Session A is still blocked. That is because Session B was also blocked — by Session C. Session C acquired an Access…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/visualizing-lock-chains-find-the-root-blocker-in-seconds-1397

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-03-08-how-to-find-and-kill-long-running-queries-in-sql-server]]
- [[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-03-16-why-alembic-is-basically-git-for-your-database-and-why-you-need-it]]
