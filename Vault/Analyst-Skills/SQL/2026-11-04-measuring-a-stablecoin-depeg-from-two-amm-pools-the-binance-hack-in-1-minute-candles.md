---
title: 'Measuring a stablecoin depeg from two AMM pools: the Binance hack in 1-minute
  candles'
date: '2026-11-04'
source: https://dev.to/stargatezone/measuring-a-stablecoin-depeg-from-two-amm-pools-the-binance-hack-in-1-minute-candles-4kbk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-10-23-vibe-trading-hit-36k-stars-in-six-months-i-read-the-repo-so-you-dont-have-to]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-04-24-the-five-most-important-columns-to-add-to-every-database-table]]'
status: unread
---

> **TL;DR:** There is no USDT/USDC market in our dataset, yet on October 29, 2026 we can say USDT traded at 0.9054 USDC on Ethereum at 21:09 UTC. This post shows how: read the cross rate through a third asset, keep the candles honest…

## What’s new and why it matters
There is no USDT/USDC market in our dataset, yet on October 29, 2026 we can say USDT traded at 0.9054 USDC on Ethereum at 21:09 UTC. This post shows how: read the cross rate through a third asset, keep the candles honest, and know what the number does and does not mean. All numbers come from our own observer, which records Binance trades and every swap of 23 BTC and ETH markets in Ethereum pools (Uniswap v2/v3/v4, SushiSwap, Curve, Balancer, Fluid, DODO) into 1m…1d candles. The trick: a cross rate through ETH Two pools in the same protocol, same base asset, different stablecoins: P_usdc = clos…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/stargatezone/measuring-a-stablecoin-depeg-from-two-amm-pools-the-binance-hack-in-1-minute-candles-4kbk

## Related notes
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-10-23-vibe-trading-hit-36k-stars-in-six-months-i-read-the-repo-so-you-dont-have-to]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-04-24-the-five-most-important-columns-to-add-to-every-database-table]]
