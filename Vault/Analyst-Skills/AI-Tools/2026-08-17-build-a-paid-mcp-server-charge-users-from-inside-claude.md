---
title: 'Build a paid MCP server: charge users from inside Claude'
date: '2026-08-17'
source: https://dev.to/ai_services_f9c382bdb33b9/build-a-paid-mcp-server-charge-users-from-inside-claude-275a
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
related:
- '[[2026-06-14-vietqr-payments-for-ai-agentsno-stripe-setup]]'
- '[[2026-06-25-agent-native-payments-building-idempotent-checkout-flows-with-agentpay]]'
- '[[2026-04-20-try-asqav-in-30-seconds]]'
- '[[2026-05-05-build-an-mcp-server-in-python-in-15-minutes]]'
- '[[2026-07-28-your-mcp-servers-search-is-bad-ranking-embeddings-and-what-each-one-fixes]]'
- '[[2026-06-30-building-a-weather-mcp-server-with-python]]'
status: unread
---

> **TL;DR:** Overview AgentPay VN lets your AI agent collect VietQR payments without ever holding the money. pip install agentpay-vn from agentpay.client import AsyncAgentPayClient , await_settlement async with AsyncAgentPayClient (…

## What’s new and why it matters
Overview AgentPay VN lets your AI agent collect VietQR payments without ever holding the money. pip install agentpay-vn from agentpay.client import AsyncAgentPayClient , await_settlement async with AsyncAgentPayClient ( ' ap_live_xxx ' ) as c : pr = await c . create_payment_request ( amount = 50_000 , description = ' Order #1 ' ) # send pr['checkout_url'] to the user r = await await_settlement ( c , pr [ ' id ' ], timeout = 120 ) The QR points at your own bank account; AgentPay only confirms settlement. Links GitHub: https://github.com/phuocdu/agentpay-vn Docs: https://agentpay.servicesai.vn/v…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ai_services_f9c382bdb33b9/build-a-paid-mcp-server-charge-users-from-inside-claude-275a

## Related notes
- [[2026-06-14-vietqr-payments-for-ai-agentsno-stripe-setup]]
- [[2026-06-25-agent-native-payments-building-idempotent-checkout-flows-with-agentpay]]
- [[2026-04-20-try-asqav-in-30-seconds]]
- [[2026-05-05-build-an-mcp-server-in-python-in-15-minutes]]
- [[2026-07-28-your-mcp-servers-search-is-bad-ranking-embeddings-and-what-each-one-fixes]]
- [[2026-06-30-building-a-weather-mcp-server-with-python]]
