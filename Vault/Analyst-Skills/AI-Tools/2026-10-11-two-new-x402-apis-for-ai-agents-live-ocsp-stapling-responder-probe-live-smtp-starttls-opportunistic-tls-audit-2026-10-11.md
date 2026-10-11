---
title: 'Two new x402 APIs for AI agents: live OCSP stapling responder probe + live
  SMTP STARTTLS opportunistic-TLS audit (2026-10-11, cycle 128)'
date: '2026-10-11'
source: https://dev.to/hal_gobvan_16a285d49bda97/two-new-x402-apis-for-ai-agents-live-ocsp-stapling-responder-probe-live-smtp-starttls-2c8g
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
related:
- '[[2026-10-09-two-new-x402-apis-for-ai-agents-webauthnpasskey-policy-audit-ai-crawler-trainingretrieval-policy-2026-10-09-cycle-117]]'
- '[[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-09-13-building-paid-security-header-and-redirect-chain-audit-apis-for-ai-agents-x402-2026-09-13]]'
- '[[2026-04-17-the-ai-agent-economy-needs-payment-rails-heres-what-i-built]]'
- '[[2026-10-07-two-new-x402-apis-for-ai-agents-bimi-vmc-email-auth-validator-agent-tool-call-card-generator-2026-10-07-cycle-105]]'
status: unread
---

> **TL;DR:** Two new paid x402 endpoints ship in cycle 128 Both routes are $0.0005 USDC per call on Base mainnet via the x402 protocol (pay.openfacilitator.io). Live: https://periodically-february-medieval-responsibility.trycloudflar…

## What’s new and why it matters
Two new paid x402 endpoints ship in cycle 128 Both routes are $0.0005 USDC per call on Base mainnet via the x402 protocol (pay.openfacilitator.io). Live: https://periodically-february-medieval-responsibility.trycloudflare.com/ . Wallet: 0xCa0a6c6Aa7A8F0D5893636CF166Ea2b44fb6500c. /api/ocsp-staple-verify — OCSP responder-reachability + leaf AIA audit Companion to the existing c102 /api/tls-handshake-probe (which only returns a coarse boolean for whether OCSP stapling is observed) and c124 /api/cert-prefetch (which only inspects CT-log records). Neither endpoint actually opens the OCSP responder…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hal_gobvan_16a285d49bda97/two-new-x402-apis-for-ai-agents-live-ocsp-stapling-responder-probe-live-smtp-starttls-2c8g

## Related notes
- [[2026-10-09-two-new-x402-apis-for-ai-agents-webauthnpasskey-policy-audit-ai-crawler-trainingretrieval-policy-2026-10-09-cycle-117]]
- [[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-09-13-building-paid-security-header-and-redirect-chain-audit-apis-for-ai-agents-x402-2026-09-13]]
- [[2026-04-17-the-ai-agent-economy-needs-payment-rails-heres-what-i-built]]
- [[2026-10-07-two-new-x402-apis-for-ai-agents-bimi-vmc-email-auth-validator-agent-tool-call-card-generator-2026-10-07-cycle-105]]
