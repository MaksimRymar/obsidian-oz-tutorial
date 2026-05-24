---
title: 'Free prediction market API for AI agents: Kalshi + Polymarket [70571]'
date: '2026-05-24'
source: https://dev.to/rileycraig14/free-prediction-market-api-for-ai-agents-kalshi-polymarket-70571-6of
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
related:
- '[[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-04-17-the-ai-agent-economy-needs-payment-rails-heres-what-i-built]]'
- '[[2026-03-25-nasa-has-20-free-apis-asteroids-mars-photos-exoplanets-and-more-no-signup]]'
- '[[2026-04-27-arbitrage-between-prediction-markets-with-python]]'
- '[[2026-04-20-i-built-an-mcp-server-for-my-crypto-trading-signal-api-heres-how-and-why]]'
status: unread
---

> **TL;DR:** import requests r = requests . get ( ' https://nexus-agent-xa12.onrender.com/v1/signals?symbol=FED ' ) print ( r . json ()) # {'signal':'BULLISH','confidence':73,'kalshi_pct':73.0} No API key. No account. Returns live Ka…

## What’s new and why it matters
import requests r = requests . get ( ' https://nexus-agent-xa12.onrender.com/v1/signals?symbol=FED ' ) print ( r . json ()) # {'signal':'BULLISH','confidence':73,'kalshi_pct':73.0} No API key. No account. Returns live Kalshi and Polymarket odds. BTC, ETH, FED, CPI, GDP signals MCP: {"mcpServers":{"nexus":{"url":"https://nexus-agent-xa12.onrender.com/mcp"}}} Paid arb endpoint: https://nexus-agent-xa12.onrender.com/arb/check ($0.01 USDC x402)

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rileycraig14/free-prediction-market-api-for-ai-agents-kalshi-polymarket-70571-6of

## Related notes
- [[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-04-17-the-ai-agent-economy-needs-payment-rails-heres-what-i-built]]
- [[2026-03-25-nasa-has-20-free-apis-asteroids-mars-photos-exoplanets-and-more-no-signup]]
- [[2026-04-27-arbitrage-between-prediction-markets-with-python]]
- [[2026-04-20-i-built-an-mcp-server-for-my-crypto-trading-signal-api-heres-how-and-why]]
