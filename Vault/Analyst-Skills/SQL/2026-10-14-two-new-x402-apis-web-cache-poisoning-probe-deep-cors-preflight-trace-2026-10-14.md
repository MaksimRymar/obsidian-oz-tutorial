---
title: 'Two new x402 APIs: web-cache-poisoning probe + deep CORS preflight trace (2026-10-14)'
date: '2026-10-14'
source: https://dev.to/hal_gobvan_16a285d49bda97/two-new-x402-apis-web-cache-poisoning-probe-deep-cors-preflight-trace-2026-10-14-1gee
domain: SQL
relevance: 🔴
tags:
- '#sql'
related:
- '[[2026-09-13-building-paid-security-header-and-redirect-chain-audit-apis-for-ai-agents-x402-2026-09-13]]'
- '[[2026-10-11-two-new-x402-apis-for-ai-agents-live-ocsp-stapling-responder-probe-live-smtp-starttls-opportunistic-tls-audit-2026-10-11]]'
- '[[2026-10-09-two-new-x402-apis-for-ai-agents-webauthnpasskey-policy-audit-ai-crawler-trainingretrieval-policy-2026-10-09-cycle-117]]'
- '[[2026-09-15-microdata-rdfa-extractor-csp-parser-apis-for-ai-agents-x402-00005call]]'
- '[[2026-10-07-two-new-x402-apis-for-ai-agents-bimi-vmc-email-auth-validator-agent-tool-call-card-generator-2026-10-07-cycle-105]]'
- '[[2026-09-14-paid-rssatom-feed-and-sitemapxml-discovery-apis-for-ai-agents-x402-2026-09-14]]'
status: unread
---

> **TL;DR:** Two new $0.0005 USDC x402 endpoints shipped today in the URL Metadata API catalog. /api/cache-poisoning-vulnerability Active probe for the well-known web-cache-poisoning vector class. Sends 5 unkeyed-header variants (X-F…

## What’s new and why it matters
Two new $0.0005 USDC x402 endpoints shipped today in the URL Metadata API catalog. /api/cache-poisoning-vulnerability Active probe for the well-known web-cache-poisoning vector class. Sends 5 unkeyed-header variants (X-Forwarded-Host + X-Original-URL + X-Forwarded-Prefix + X-Host + X-Forwarded-Server + X-Forwarded-For + X-Forwarded-Proto + X-Original-Host + X-Rewrite-URL), 4 cachebuster-query probes (cb + nocache + utm_source + gclid), and 4 web-cache-deception path probes (robots.txt + .css + .js + .png). Compares body-hash against a baseline fetch and flags any divergence without matching Va…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/hal_gobvan_16a285d49bda97/two-new-x402-apis-web-cache-poisoning-probe-deep-cors-preflight-trace-2026-10-14-1gee

## Related notes
- [[2026-09-13-building-paid-security-header-and-redirect-chain-audit-apis-for-ai-agents-x402-2026-09-13]]
- [[2026-10-11-two-new-x402-apis-for-ai-agents-live-ocsp-stapling-responder-probe-live-smtp-starttls-opportunistic-tls-audit-2026-10-11]]
- [[2026-10-09-two-new-x402-apis-for-ai-agents-webauthnpasskey-policy-audit-ai-crawler-trainingretrieval-policy-2026-10-09-cycle-117]]
- [[2026-09-15-microdata-rdfa-extractor-csp-parser-apis-for-ai-agents-x402-00005call]]
- [[2026-10-07-two-new-x402-apis-for-ai-agents-bimi-vmc-email-auth-validator-agent-tool-call-card-generator-2026-10-07-cycle-105]]
- [[2026-09-14-paid-rssatom-feed-and-sitemapxml-discovery-apis-for-ai-agents-x402-2026-09-14]]
