---
title: Google crawled 230 pages of my site and indexed 2. Here is how I diagnosed
  it.
date: '2026-09-04'
source: https://dev.to/azorkai/google-crawled-230-pages-of-my-site-and-indexed-2-here-is-how-i-diagnosed-it-24i6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-26-your-site-is-bleeding-seo-over-dead-links-heres-a-10-minute-fix]]'
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** My marketing site has 230 URLs in its sitemaps. Google has indexed 2 of them. Not "pending". Not "blocked". Crawled, fetched successfully, canonical accepted, and then declined. This post is the diagnostic path I took, t…

## What’s new and why it matters
My marketing site has 230 URLs in its sitemaps. Google has indexed 2 of them. Not "pending". Not "blocked". Crawled, fetched successfully, canonical accepted, and then declined. This post is the diagnostic path I took, the two measurement mistakes I made along the way, and the Search Console API calls that finally produced a straight answer. The setup The site is a Vite + React SPA prerendered at build time by Puppeteer. Every route ships as a static HTML file with the content already in the markup, served by nginx. Not SSR, but for a crawler it is indistinguishable: the body arrives full. The…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/azorkai/google-crawled-230-pages-of-my-site-and-indexed-2-here-is-how-i-diagnosed-it-24i6

## Related notes
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-26-your-site-is-bleeding-seo-over-dead-links-heres-a-10-minute-fix]]
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
