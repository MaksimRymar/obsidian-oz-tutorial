---
title: CA 37 – Durability (ACID)
date: '2026-03-29'
source: https://dev.to/mohammed_azim_j/ca-37-durability-acid-n7e
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-25-durability]]'
- '[[2026-03-25-idempotency-situation]]'
- '[[2026-03-25-consistency]]'
- '[[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]'
- '[[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]'
- '[[2026-03-25-isolation]]'
status: unread
---

> **TL;DR:** This one is about Durability, means once data is saved (commit), it should not disappear even if system crashes. First I checked initial data: SELECT * FROM accounts ; Alice -> 1000 Bob -> 500 Then I did a transfer: BEGI…

## What’s new and why it matters
This one is about Durability, means once data is saved (commit), it should not disappear even if system crashes. First I checked initial data: SELECT * FROM accounts ; Alice -> 1000 Bob -> 500 Then I did a transfer: BEGIN ; UPDATE accounts SET balance = balance - 300 WHERE name = 'Alice' ; UPDATE accounts SET balance = balance + 300 WHERE name = 'Bob' ; COMMIT ; After commit I checked again: SELECT * FROM accounts ; Alice -> 700 Bob -> 800 So transfer done. Now imagine system crash or restart. After reconnecting I ran same query again: SELECT * FROM accounts ; Still: Alice -> 700 Bob -> 800 So…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohammed_azim_j/ca-37-durability-acid-n7e

## Related notes
- [[2026-03-25-durability]]
- [[2026-03-25-idempotency-situation]]
- [[2026-03-25-consistency]]
- [[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]
- [[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]
- [[2026-03-25-isolation]]
