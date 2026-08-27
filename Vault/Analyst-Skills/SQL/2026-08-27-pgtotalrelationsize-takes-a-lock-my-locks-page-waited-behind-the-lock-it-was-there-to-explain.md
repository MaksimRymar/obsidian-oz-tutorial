---
title: pg_total_relation_size() takes a lock. My locks page waited behind the lock
  it was there to explain.
date: '2026-08-27'
source: https://dev.to/hitoshi1964/pgtotalrelationsize-takes-a-lock-my-locks-page-waited-behind-the-lock-it-was-there-to-1475
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
status: unread
---

> **TL;DR:** An ALTER TABLE is waiting on an idle transaction. Ten sessions are queued behind it. You open the tool that exists to tell you which session to kill — and the page never returns. That was cli2ui, three weeks ago, on my o…

## What’s new and why it matters
An ALTER TABLE is waiting on an idle transaction. Ten sessions are queued behind it. You open the tool that exists to tell you which session to kill — and the page never returns. That was cli2ui, three weeks ago, on my own machine. The Locks panel itself was fine: it answered in 0.02 seconds. What never came back was the page on the way to it. The overview and the Health panel both show table sizes, and table sizes come from pg_total_relation_size() and pg_table_size() . Those functions open the relation they measure. Opening a relation takes ACCESS SHARE . And ACCESS SHARE queues behind the A…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/hitoshi1964/pgtotalrelationsize-takes-a-lock-my-locks-page-waited-behind-the-lock-it-was-there-to-1475

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
