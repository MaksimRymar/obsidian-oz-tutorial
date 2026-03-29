---
title: CA 36 – Isolation (ACID)
date: '2026-03-29'
source: https://dev.to/mohammed_azim_j/ca-36-isolation-acid-3bn
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#tool'
related:
- '[[2026-03-25-isolation]]'
- '[[2026-03-29-ca-37-durability-acid]]'
- '[[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]'
- '[[2026-03-25-atomicity]]'
- '[[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]'
- '[[2026-03-25-consistency]]'
status: unread
---

> **TL;DR:** This one was about Isolation, basically what happens when two people try to use the same account at the same time. I used two sessions (like opening two terminals). First I checked data: SELECT * FROM accounts; Alice ->…

## What’s new and why it matters
This one was about Isolation, basically what happens when two people try to use the same account at the same time. I used two sessions (like opening two terminals). First I checked data: SELECT * FROM accounts; Alice -> 1000 Bob -> 500 Now in Session 1: BEGIN; UPDATE accounts SET balance = balance - 800 WHERE name = 'Alice'; I did not commit yet. Now in Session 2, I tried: SELECT * FROM accounts WHERE name = 'Alice'; It still shows 1000, not 200. So uncommitted change is not visible → no dirty read. Then in Session 2 I tried to update: UPDATE accounts SET balance = balance - 300 WHERE name = '…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mohammed_azim_j/ca-36-isolation-acid-3bn

## Related notes
- [[2026-03-25-isolation]]
- [[2026-03-29-ca-37-durability-acid]]
- [[2026-03-25-atomicity---design-a-reliable-wallet-transfer-system-with-acid-guarantees]]
- [[2026-03-25-atomicity]]
- [[2026-03-26-design-a-reliable-wallet-transfer-system-with-acid-guarantees-pt---1-atomicity]]
- [[2026-03-25-consistency]]
