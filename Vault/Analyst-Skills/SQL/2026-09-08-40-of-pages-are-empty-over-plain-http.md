---
title: 40% of pages are empty over plain HTTP
date: '2026-09-08'
source: https://dev.to/extractdata/40-of-pages-are-empty-over-plain-http-lip
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-04-17-the-quote-as-ceiling-billing-pattern]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
status: unread
---

> **TL;DR:** 40.6% of popular landing pages need JavaScript to show you anything useful. That is from State of Web Access , an audit Zyte (where I work) ran on 11,100 landing pages. The test was blunt. Fetch the page over plain HTTP,…

## What’s new and why it matters
40.6% of popular landing pages need JavaScript to show you anything useful. That is from State of Web Access , an audit Zyte (where I work) ran on 11,100 landing pages. The test was blunt. Fetch the page over plain HTTP, fetch it again in a headless browser, and if rendering grew the meaningful HTML by more than half, count it as JavaScript-dependent. On the pages that failed the test, rendering added 140,923 bytes on average. Three quarters of the final HTML did not exist until a browser ran the scripts. Restaurants and airlines top the list at 66%, travel at 65%. The report calls this archit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/extractdata/40-of-pages-are-empty-over-plain-http-lip

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-04-17-the-quote-as-ceiling-billing-pattern]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
