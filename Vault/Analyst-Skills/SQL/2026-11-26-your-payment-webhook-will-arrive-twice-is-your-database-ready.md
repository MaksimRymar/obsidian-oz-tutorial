---
title: Your payment webhook will arrive twice. Is your database ready?
date: '2026-11-26'
source: https://dev.to/isaactony/your-payment-webhook-will-arrive-twice-is-your-database-ready-1f1k
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]'
- '[[2026-11-17-ora-00054-resource-busy-find-the-session-and-know-which-ddl-will-wait]]'
status: unread
---

> **TL;DR:** Every payment provider retries webhooks. If your endpoint is slow, times out, or returns anything other than a 2xx, the provider sends the same event again. Sometimes it sends it again even when you did everything right,…

## What’s new and why it matters
Every payment provider retries webhooks. If your endpoint is slow, times out, or returns anything other than a 2xx, the provider sends the same event again. Sometimes it sends it again even when you did everything right, because the response got lost on the way back. So at some point your handler will receive the same payment twice. The usual defence looks like this. if not db . exists ( "SELECT 1 FROM credits WHERE event_id = ?" , event . id ) : db . execute ( "INSERT INTO credits ..." ) It works in every test, and it works in production most of the time. It fails when the two deliveries arri…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/isaactony/your-payment-webhook-will-arrive-twice-is-your-database-ready-1f1k

## Related notes
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-09-28-how-i-stream-row-changes-out-of-sqlite-without-touching-the-app-reading-the-wal]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-11-18-two-hallucination-tests-you-can-run-before-you-pay-for-a-judge-model]]
- [[2026-11-17-ora-00054-resource-busy-find-the-session-and-know-which-ddl-will-wait]]
