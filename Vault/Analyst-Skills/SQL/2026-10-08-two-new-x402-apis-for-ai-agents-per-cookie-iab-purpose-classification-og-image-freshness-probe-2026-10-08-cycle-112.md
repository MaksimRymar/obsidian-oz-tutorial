---
title: 'Two new x402 APIs for AI agents: per-cookie IAB purpose classification + OG
  image freshness probe (2026-10-08, cycle 112)'
date: '2026-10-08'
source: https://dev.to/hal_gobvan_16a285d49bda97/two-new-x402-apis-for-ai-agents-per-cookie-iab-purpose-classification-og-image-freshness-probe-5d6j
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-13-building-paid-security-header-and-redirect-chain-audit-apis-for-ai-agents-x402-2026-09-13]]'
- '[[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-10-07-two-new-x402-apis-for-ai-agents-bimi-vmc-email-auth-validator-agent-tool-call-card-generator-2026-10-07-cycle-105]]'
- '[[2026-03-13-i-built-a-screenshot-metadata-api-that-extracts-50-fields-from-any-url]]'
- '[[2026-05-29-building-helix-an-open-source-visual-identity-mapper-that-cuts-the-noise]]'
status: unread
---

> **TL;DR:** Two new paid x402 APIs for AI agents that need finer-grained web intelligence than the existing catalog provides. /api/cookie-purpose-classification ($0.0005) What it does: Captures every Set-Cookie from a page response…

## What’s new and why it matters
Two new paid x402 APIs for AI agents that need finer-grained web intelligence than the existing catalog provides. /api/cookie-purpose-classification ($0.0005) What it does: Captures every Set-Cookie from a page response + every inline document.cookie= write in the page's JavaScript, then classifies each cookie by NAME heuristics mapped to IAB TCF v2.2 purposes (1=Store/access, 2=Personalization, 3=Ad selection, 4=Content selection, 5=Measurement). 10 vendor fingerprints recognized by name: _ga / _gid / _gat / _gcl* → Google Analytics _fbp / _fbc / fr → Facebook Pixel _gcl_au / aw* / _uet* → Go…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/hal_gobvan_16a285d49bda97/two-new-x402-apis-for-ai-agents-per-cookie-iab-purpose-classification-og-image-freshness-probe-5d6j

## Related notes
- [[2026-09-13-building-paid-security-header-and-redirect-chain-audit-apis-for-ai-agents-x402-2026-09-13]]
- [[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-10-07-two-new-x402-apis-for-ai-agents-bimi-vmc-email-auth-validator-agent-tool-call-card-generator-2026-10-07-cycle-105]]
- [[2026-03-13-i-built-a-screenshot-metadata-api-that-extracts-50-fields-from-any-url]]
- [[2026-05-29-building-helix-an-open-source-visual-identity-mapper-that-cuts-the-noise]]
