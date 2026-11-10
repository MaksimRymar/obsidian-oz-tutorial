---
title: Your Outbox Can Still Deliver Twice
date: '2026-11-10'
source: https://dev.to/smtasker-official/your-outbox-can-still-deliver-twice-14c7
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-11-01-put-the-workspace-check-inside-the-database-write]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]'
- '[[2026-11-09-who-kills-your-background-worker-and-how-soon-a-shutdown-test-plan]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
status: unread
---

> **TL;DR:** A receiver commits its work. The reply disappears. The sender sees a timeout and sends the same event again. An outbox can preserve the event through that sequence. It cannot, by itself, tell the receiver that the work a…

## What’s new and why it matters
A receiver commits its work. The reply disappears. The sender sees a timeout and sends the same event again. An outbox can preserve the event through that sequence. It cannot, by itself, tell the receiver that the work already happened. Here is a small reproduction with two SQLite databases and ten tests. The unsafe receiver adds two rows for one event. The receiver with an inbox adds one row and returns its stored receipt on the second delivery. This continues the previous example about recovering a lost response . That example kept a mutation and its operation receipt in one database. This t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/smtasker-official/your-outbox-can-still-deliver-twice-14c7

## Related notes
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-11-01-put-the-workspace-check-inside-the-database-write]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-09-09-sql-joins-in-postgresql-patients-doctors-and-the-rows-that-go-missing]]
- [[2026-11-09-who-kills-your-background-worker-and-how-soon-a-shutdown-test-plan]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
