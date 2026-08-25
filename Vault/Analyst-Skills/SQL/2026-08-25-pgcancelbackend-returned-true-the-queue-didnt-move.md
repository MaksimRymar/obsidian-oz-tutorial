---
title: pg_cancel_backend() returned true. The queue didn't move.
date: '2026-08-25'
source: https://dev.to/hitoshi1964/pgcancelbackend-returned-true-the-queue-didnt-move-4921
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
status: unread
---

> **TL;DR:** Ten sessions are stuck. You skip the slow-query hunt, do the hard part properly, and find the one session at the front of the queue — the one holding a lock that everyone else is waiting on. You press cancel. Postgres sa…

## What’s new and why it matters
Ten sessions are stuck. You skip the slow-query hunt, do the hard part properly, and find the one session at the front of the queue — the one holding a lock that everyone else is waiting on. You press cancel. Postgres says t . Nothing happens. Not "nothing happens yet." Nothing happens at all. The session is still there, the locks are still held, and the nine sessions behind it are exactly where they were. The call succeeded and did nothing, which is a worse outcome than failing, because a failure would have told you to try something else. Cancel cancels a query . That session isn't running on…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hitoshi1964/pgcancelbackend-returned-true-the-queue-didnt-move-4921

## Related notes
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-12-sql-foundations-start-to-finish]]
