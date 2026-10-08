---
title: I locked my test criteria before running them. My trading bot failed.
date: '2026-10-08'
source: https://dev.to/botgauntlet/i-locked-my-test-criteria-before-running-them-my-trading-bot-failed-n4n
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]'
- '[[2026-04-21-sql-window-functions-and-ctes]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** I built a Python paper-trading bot for crypto spot markets. The backtest looked fine. Then I tested it the strict way, and it fell apart. This is what the strict way looks like, and what it found. The rule: lock the crit…

## What’s new and why it matters
I built a Python paper-trading bot for crypto spot markets. The backtest looked fine. Then I tested it the strict way, and it fell apart. This is what the strict way looks like, and what it found. The rule: lock the criteria before you look Before each test I write down the hypothesis, the data, the metric and the pass/fail thresholds. I hash the file (sha256). The test script refuses to run if the hash does not match. After that I get one run. No tweaking the threshold after seeing the result. It sounds bureaucratic. It is the only thing that stopped me from fooling myself, because I tried a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/botgauntlet/i-locked-my-test-criteria-before-running-them-my-trading-bot-failed-n4n

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-04-21-i-build-custom-trading-bots-for-deriv-and-mt4mt5-heres-what-that-actually-looks-like]]
- [[2026-04-21-sql-window-functions-and-ctes]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
