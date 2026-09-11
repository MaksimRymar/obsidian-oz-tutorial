---
title: How stale is company registry data? Measuring lag against the Companies House
  API
date: '2026-09-11'
source: https://dev.to/openregistry/how-stale-is-company-registry-data-measuring-lag-against-the-companies-house-api-1egn
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]'
status: unread
---

> **TL;DR:** We build OpenRegistry, a live registry API. This post was written with AI assistance. Every company-data product is either a live query or a copy. Copies are fine until the thing you care about changes after the copy was…

## What’s new and why it matters
We build OpenRegistry, a live registry API. This post was written with AI assistance. Every company-data product is either a live query or a copy. Copies are fine until the thing you care about changes after the copy was taken. This post shows how to measure that gap for UK companies yourself, using the free Companies House API, and what we saw when we tried it on four companies. Why freshness matters Know-your-business (KYB) checks ask simple questions: does this company exist, is it active, and who runs it? The answers change. Picture a supplier-onboarding check on a Thursday. The director w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/openregistry/how-stale-is-company-registry-data-measuring-lag-against-the-companies-house-api-1egn

## Related notes
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-08-20-build-a-50-line-harness-to-test-whether-a-free-model-endpoint-can-fix-broken-json]]
