---
title: Docker Hub's API 403s Chrome and 200s Firefox — same URL, same second
date: '2026-09-05'
source: https://dev.to/devil_scrapes/docker-hubs-api-403s-chrome-and-200s-firefox-same-url-same-second-3md9
domain: SQL
relevance: 🟡
tags:
- '#library'
- '#python'
- '#sql'
related:
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]'
- '[[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-02-your-agent-request-touches-12-containers-only-one-of-them-runs-a-model]]'
status: unread
---

> **TL;DR:** Quick answer Docker Hub's public /v2 REST API returns HTTP 403 to a Chrome TLS fingerprint and HTTP 200 to a Firefox one — same URL, same IP, same second. No auth, no rate limit, no bot score. Just the fingerprint. If yo…

## What’s new and why it matters
Quick answer Docker Hub's public /v2 REST API returns HTTP 403 to a Chrome TLS fingerprint and HTTP 200 to a Firefox one — same URL, same IP, same second. No auth, no rate limit, no bot score. Just the fingerprint. If your Docker Hub client is failing with a Cloudflare "Just a moment..." page, you probably don't have an IP problem. You have a chrome problem. The assumption that was wrong 🐳 When we spec'd the Docker Hub Images & Tags Scraper , the Open Questions section said, in writing: Docker Hub's public /v2 API needs no anti-bot evasion. Reasonable. It's a public, keyless, documented REST A…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/docker-hubs-api-403s-chrome-and-200s-firefox-same-url-same-second-3md9

## Related notes
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-29-why-your-sql-server-database-is-slow-and-how-to-fix-it]]
- [[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-02-your-agent-request-touches-12-containers-only-one-of-them-runs-a-model]]
