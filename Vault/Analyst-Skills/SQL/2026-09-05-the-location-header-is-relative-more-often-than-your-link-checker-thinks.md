---
title: The Location header is relative more often than your link checker thinks
date: '2026-09-05'
source: https://dev.to/devil_scrapes/the-location-header-is-relative-more-often-than-your-link-checker-thinks-j09
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-26-your-site-is-bleeding-seo-over-dead-links-heres-a-10-minute-fix]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** Quick answer httpbin.org/redirect/2 sends you through two hops. Both Location headers are relative : http://httpbin.org/redirect/2 -> 302 Location: /relative-redirect/1 http://httpbin.org/relative-redirect/1 -> 302 Locat…

## What’s new and why it matters
Quick answer httpbin.org/redirect/2 sends you through two hops. Both Location headers are relative : http://httpbin.org/redirect/2 -> 302 Location: /relative-redirect/1 http://httpbin.org/relative-redirect/1 -> 302 Location: /get http://httpbin.org/get -> 200 If your redirect-chaser treats Location as an absolute URL, hop one is already broken. If it resolves relative URLs against the original URL instead of the current hop, you'll survive this chain and silently break on a cross-host one. Location is allowed to be almost anything 🔁 RFC 7231 permits Location to be a full URI, an absolute path,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/the-location-header-is-relative-more-often-than-your-link-checker-thinks-j09

## Related notes
- [[2026-08-26-your-site-is-bleeding-seo-over-dead-links-heres-a-10-minute-fix]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-31-a-passing-check-is-a-claim-about-what-ran-not-whats-true]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
