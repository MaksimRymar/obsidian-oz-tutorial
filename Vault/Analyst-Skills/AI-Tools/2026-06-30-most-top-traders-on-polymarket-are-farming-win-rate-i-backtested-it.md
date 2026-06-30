---
title: Most "top traders" on Polymarket are farming win rate. I backtested it.
date: '2026-06-30'
source: https://dev.to/ekocam/most-top-traders-on-polymarket-are-farming-win-rate-i-backtested-it-1b8j
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-09-pandas-vs-sql-when-to-use-each]]'
- '[[2026-04-17-the-quote-as-ceiling-billing-pattern]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
status: unread
---

> **TL;DR:** If you've looked at a "top traders" leaderboard on Polymarket and thought about copy-trading the top wallets, I have some bad news: a lot of those flawless 95%+ win-rate records are farmed, not earned. I pulled the on-ch…

## What’s new and why it matters
If you've looked at a "top traders" leaderboard on Polymarket and thought about copy-trading the top wallets, I have some bad news: a lot of those flawless 95%+ win-rate records are farmed, not earned. I pulled the on-chain data and backtested it, and the raw leaderboard turns out to be a pretty bad signal to copy. Here's the breakdown, with reproducible notebooks at the end. The farming trick It's simple. You only ever buy outcomes that are already basically decided, priced around 95-99c. Think of a market like "Will X happen?" sitting at 99c the day before it resolves. You put up 99c to make…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ekocam/most-top-traders-on-polymarket-are-farming-win-rate-i-backtested-it-1b8j

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-09-pandas-vs-sql-when-to-use-each]]
- [[2026-04-17-the-quote-as-ceiling-billing-pattern]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
