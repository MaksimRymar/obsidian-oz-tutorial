---
title: 'Amazon Interview Question: Design a Delayed Job Scheduler (Timers, Leases,
  and Exactly-Once Execution)'
date: '2026-09-23'
source: https://dev.to/emilywoodsnyc/amazon-interview-question-design-a-delayed-job-scheduler-timers-leases-and-exactly-once-20en
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]'
status: unread
---

> **TL;DR:** Every candidate can write the first version of this in about thirty seconds. new Thread(() -> { Thread.sleep(delayMillis); runJob(job); }).start(); That code is correct in the narrowest possible sense. It also falls over…

## What’s new and why it matters
Every candidate can write the first version of this in about thirty seconds. new Thread(() -> { Thread.sleep(delayMillis); runJob(job); }).start(); That code is correct in the narrowest possible sense. It also falls over at roughly 10,000 jobs, forgets everything the moment the process restarts, and runs a job twice the instant you add a second machine. Working out why, in that order, is the entire interview. The prompt itself sounds fairly modest on the surface. Schedule a job to run at some future time, allow it to be cancelled, and survive at scale. Underneath that sits a timing problem, a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/emilywoodsnyc/amazon-interview-question-design-a-delayed-job-scheduler-timers-leases-and-exactly-once-20en

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-08-charge-wait-time-to-the-same-job]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-06-05-your-postgres-is-failing-quietly-7-sql-checks-that-catch-it-before-grafana-does]]
