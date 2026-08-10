---
title: I Backtested a Macro Scenario Classifier. The Signal Was Backwards.
date: '2026-08-10'
source: https://dev.to/473185670/i-backtested-a-macro-scenario-classifier-the-signal-was-backwards-2pb
domain: Python
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#presentations'
- '#python'
- '#tool'
related:
- '[[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]'
- '[[2026-06-24-how-i-stopped-bleeding-money-on-ai-apis-a-freelancers-guide]]'
- '[[2026-05-20-building-ai-market-briefings-in-python-with-the-charlie-api]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-06-09-pandas-vs-sql-when-to-use-each]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
status: unread
---

> **TL;DR:** I spent two weeks building a classifier that sorts ISM Manufacturing PMI releases into "GOLDILOCKS" (growth without overheating) and "CONTRACTION" (economy shrinking) scenarios. The textbook hypothesis: GOLDILOCKS predic…

## What’s new and why it matters
I spent two weeks building a classifier that sorts ISM Manufacturing PMI releases into "GOLDILOCKS" (growth without overheating) and "CONTRACTION" (economy shrinking) scenarios. The textbook hypothesis: GOLDILOCKS predicts positive S&P 500 forward returns, CONTRACTION predicts negative ones. The backtest showed the exact opposite. CONTRACTION releases produced higher forward S&P 500 returns than GOLDILOCKS at every horizon I tested -- and the sign test confirms this is not noise (p < 10^-13 at 42 days). The setup ISM Manufacturing PMI is a monthly survey of ~300 supply managers; above 50 = exp…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/473185670/i-backtested-a-macro-scenario-classifier-the-signal-was-backwards-2pb

## Related notes
- [[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]
- [[2026-06-24-how-i-stopped-bleeding-money-on-ai-apis-a-freelancers-guide]]
- [[2026-05-20-building-ai-market-briefings-in-python-with-the-charlie-api]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-06-09-pandas-vs-sql-when-to-use-each]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
