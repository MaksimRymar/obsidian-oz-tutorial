---
title: Catching money bugs with ledger invariants, not error logs
date: '2026-08-10'
source: https://dev.to/shipmindlabs/catching-money-bugs-with-ledger-invariants-not-error-logs-3o4l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
status: unread
---

> **TL;DR:** A payout that credits the wrong sub-account returns HTTP 200. Nothing throws, the worker acknowledges the message, the error dashboards stay green, and the discrepancy surfaces days later when someone reconciles a bank s…

## What’s new and why it matters
A payout that credits the wrong sub-account returns HTTP 200. Nothing throws, the worker acknowledges the message, the error dashboards stay green, and the discrepancy surfaces days later when someone reconciles a bank statement by hand. That gap — between "the code ran without errors" and "the money is where it should be" — is where the hardest incidents in payment systems live. Retries, partial failures, and provider callbacks arriving out of order all produce states that are individually plausible and collectively wrong. Exception tracking cannot see them, because there is no exception. We…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shipmindlabs/catching-money-bugs-with-ledger-invariants-not-error-logs-3o4l

## Related notes
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
