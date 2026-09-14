---
title: Modeling Bitcoin volatility with a Markov-switching model
date: '2026-09-14'
source: https://dev.to/aethanlee/modeling-bitcoin-volatility-with-a-markov-switching-model-5a6o
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-i-couldnt-afford-an-a100-so-i-built-a-surgical-weight-editor-in-rust]]'
- '[[2026-08-20-i-built-an-ai-that-trades-crypto-using-evolutionary-algorithms-heres-what-i-learned]]'
- '[[2026-04-14-stock-recommendation-system-using-anthropic-mcp-and-python]]'
- '[[2026-06-09-sql-pattern-series-4-the-moving-sum-pattern]]'
- '[[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]'
- '[[2026-05-17-devmcp-context-a-simple-ai-memory-layer-for-your-agent]]'
status: unread
---

> **TL;DR:** A Bitcoin price chart shows the path prices took. For this report, I wanted to estimate how the volatility of daily returns changed along that path. I used a Markov-switching model and built the visual report in OWL Comp…

## What’s new and why it matters
A Bitcoin price chart shows the path prices took. For this report, I wanted to estimate how the volatility of daily returns changed along that path. I used a Markov-switching model and built the visual report in OWL Compose. The report includes state probabilities, a transition matrix and a comparison between two-state and three-state specifications. Explore the full report . Start with returns and a fixed cutoff The input is Binance Spot BTCUSDT daily OHLCV data, using completed UTC candles through September 13, 2026. Daily returns are calculated as: 100 * ln(close_today / close_yesterday) I…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aethanlee/modeling-bitcoin-volatility-with-a-markov-switching-model-5a6o

## Related notes
- [[2026-03-30-i-couldnt-afford-an-a100-so-i-built-a-surgical-weight-editor-in-rust]]
- [[2026-08-20-i-built-an-ai-that-trades-crypto-using-evolutionary-algorithms-heres-what-i-learned]]
- [[2026-04-14-stock-recommendation-system-using-anthropic-mcp-and-python]]
- [[2026-06-09-sql-pattern-series-4-the-moving-sum-pattern]]
- [[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]
- [[2026-05-17-devmcp-context-a-simple-ai-memory-layer-for-your-agent]]
