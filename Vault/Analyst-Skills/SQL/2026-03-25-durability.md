---
title: Durability
date: '2026-03-25'
source: https://dev.to/jarvish_/durability-19mm
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-25-idempotency-situation]]'
- '[[2026-03-25-isolation]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-25-visualizing-lock-chains-find-the-root-blocker-in-seconds]]'
- '[[2026-03-25-consistency]]'
- '[[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]'
status: unread
---

> **TL;DR:** SELECT * FROM accounts ; Begin by looking at the current balances so there is a clear idea of the starting point. This makes it easier to confirm later whether the transfer actually went through and stayed saved. BEGIN ;…

## What’s new and why it matters
SELECT * FROM accounts ; Begin by looking at the current balances so there is a clear idea of the starting point. This makes it easier to confirm later whether the transfer actually went through and stayed saved. BEGIN ; UPDATE accounts SET balance = balance - 300 WHERE name = 'Alice' ; UPDATE accounts SET balance = balance + 300 WHERE name = 'Bob' ; COMMIT ; Both updates are wrapped inside a transaction so they execute together. The commit finalizes the change, making it permanent instead of temporary. SELECT * FROM accounts ; Immediately checking after commit helps confirm that the transfer…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jarvish_/durability-19mm

## Related notes
- [[2026-03-25-idempotency-situation]]
- [[2026-03-25-isolation]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-25-visualizing-lock-chains-find-the-root-blocker-in-seconds]]
- [[2026-03-25-consistency]]
- [[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]
