---
title: Session 4 summary
date: '2026-06-22'
source: https://dev.to/hvdineshbabu/session-4-summary-28in
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-03-29-ca-34-atomicity-reliable-wallet-transfer-system-acid]]'
- '[[2026-03-28-assignment-34]]'
- '[[2026-03-10-joins-window-functions]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-02-sql-joins-explained-case-example]]'
- '[[2026-05-12-sql-transactions-and-write-conflicts]]'
status: unread
---

> **TL;DR:** In the last session a few different concepts were taught: ACID properties SQL transaction modes with demonstration on different levels Redis caching My understanding of these concepts are as follows: 1. ACID properties:…

## What’s new and why it matters
In the last session a few different concepts were taught: ACID properties SQL transaction modes with demonstration on different levels Redis caching My understanding of these concepts are as follows: 1. ACID properties: We were taught about atomicity and isolation. So atomicity simply means that either a transaction occurs or it doesn't. There shouldn't be any intermediate results for a transaction. For example, let us consider a transaction whereby a transfer of money is occuring from one bank account to another, if the debit occurs from the sender's account but fails at a point before credit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hvdineshbabu/session-4-summary-28in

## Related notes
- [[2026-03-29-ca-34-atomicity-reliable-wallet-transfer-system-acid]]
- [[2026-03-28-assignment-34]]
- [[2026-03-10-joins-window-functions]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-02-sql-joins-explained-case-example]]
- [[2026-05-12-sql-transactions-and-write-conflicts]]
