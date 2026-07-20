---
title: My trading system has a 73.5% win rate and loses money. Here is the diagnostic
  that found it.
date: '2026-07-20'
source: https://dev.to/northmark/my-trading-system-has-a-735-win-rate-and-loses-money-here-is-the-diagnostic-that-found-it-2faa
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-13-pc-workman-v172-i-built-a-driver-booster-competitor-from-scratch-fixes-monday-grind-blueprint-3]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
status: unread
---

> **TL;DR:** I spent a few days auditing a live FX system I built, over 16 years of history. The result was negative in a way I did not expect, and the diagnostic that found it is general enough to be worth writing up — it applies to…

## What’s new and why it matters
I spent a few days auditing a live FX system I built, over 16 years of history. The result was negative in a way I did not expect, and the diagnostic that found it is general enough to be worth writing up — it applies to any parameter search, not just trading. The setup 17 configurations, 4-hour entry bars, exits simulated on 1-hour bars, 2010-05-28 .. 2026-07-08 (16.1y), 7641 trades. Crucially I fed the unmodified production functions historical CSV instead of a live data feed, so the code path being tested is the code path that runs live. Bug 1: the simulation charged costs to the wrong plac…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/northmark/my-trading-system-has-a-735-win-rate-and-loses-money-here-is-the-diagnostic-that-found-it-2faa

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-13-pc-workman-v172-i-built-a-driver-booster-competitor-from-scratch-fixes-monday-grind-blueprint-3]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
