---
title: Atomicity
date: '2026-03-25'
source: https://dev.to/jarvish_/atomicity-anh
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-25-durability]]'
- '[[2026-03-25-idempotency-situation]]'
- '[[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]'
- '[[2026-03-25-isolation]]'
- '[[2026-03-25-consistency]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
status: unread
---

> **TL;DR:** Design a transaction to transfer money from one account to another (atomic operation) BEGIN ; UPDATE accounts SET balance = balance - 300 WHERE name = 'Alice' ; UPDATE accounts SET balance = balance + 300 WHERE name = 'B…

## What’s new and why it matters
Design a transaction to transfer money from one account to another (atomic operation) BEGIN ; UPDATE accounts SET balance = balance - 300 WHERE name = 'Alice' ; UPDATE accounts SET balance = balance + 300 WHERE name = 'Bob' ; COMMIT ; Both updates are wrapped inside one block so they either succeed together or not at all. This avoids any mismatch between sender and receiver balances. Check balances before and after successful transaction SELECT * FROM accounts ; Look at the balances before running the transfer to know the starting point. After commit, confirm both accounts changed correctly. I…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jarvish_/atomicity-anh

## Related notes
- [[2026-03-25-durability]]
- [[2026-03-25-idempotency-situation]]
- [[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]
- [[2026-03-25-isolation]]
- [[2026-03-25-consistency]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
