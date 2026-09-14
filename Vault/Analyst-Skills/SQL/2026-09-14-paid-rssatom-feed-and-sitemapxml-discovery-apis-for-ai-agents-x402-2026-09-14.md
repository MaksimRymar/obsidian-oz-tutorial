---
title: Paid RSS/Atom feed and sitemap.xml discovery APIs for AI agents (x402, 2026-09-14)
date: '2026-09-14'
source: https://dev.to/hal_gobvan_16a285d49bda97/paid-rssatom-feed-and-sitemapxml-discovery-apis-for-ai-agents-x402-2026-09-14-3hco
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-13-building-paid-security-header-and-redirect-chain-audit-apis-for-ai-agents-x402-2026-09-13]]'
- '[[2026-09-05-cloudflares-securitytxt-404s-with-content-type-textplain]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-05-13-i-built-a-telegram-bot-that-earns-usdc-per-ai-query-free-to-try]]'
- '[[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
status: unread
---

> **TL;DR:** TL;DR Two new $0.0005-USDC x402 endpoints just shipped at https://epson-rpm-america-satisfy.trycloudflare.com — GET /api/feed?url=<URL> discovers RSS/Atom feeds (link-tag autodiscovery + path probe + first-10-entry parse…

## What’s new and why it matters
TL;DR Two new $0.0005-USDC x402 endpoints just shipped at https://epson-rpm-america-satisfy.trycloudflare.com — GET /api/feed?url=<URL> discovers RSS/Atom feeds (link-tag autodiscovery + path probe + first-10-entry parse) and GET /api/sitemap?url=<URL> finds sitemap.xml via robots.txt Sitemap: directives + path probes, recurses nested sitemap indexes, and returns up to 200 URLs with a top-path-section distribution. Why agents want these Most URL-metadata APIs stop at title/description/OG tags. AI agents doing preflight on a candidate URL need three extra signals before they commit to scraping:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hal_gobvan_16a285d49bda97/paid-rssatom-feed-and-sitemapxml-discovery-apis-for-ai-agents-x402-2026-09-14-3hco

## Related notes
- [[2026-09-13-building-paid-security-header-and-redirect-chain-audit-apis-for-ai-agents-x402-2026-09-13]]
- [[2026-09-05-cloudflares-securitytxt-404s-with-content-type-textplain]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-05-13-i-built-a-telegram-bot-that-earns-usdc-per-ai-query-free-to-try]]
- [[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
