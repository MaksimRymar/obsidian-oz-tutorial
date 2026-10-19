---
title: 'We Tested Shopify’s /products.json on 68 Stores: The Limits Tutorials Don’t
  Mention'
date: '2026-10-19'
source: https://dev.to/rslndev/we-tested-shopifys-productsjson-on-68-stores-the-limits-tutorials-dont-mention-1ofj
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-15-looking-for-a-multimarket-stock-api-pull-ashare-hong-kong-and-us-quotes-in-python]]'
- '[[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
status: unread
---

> **TL;DR:** Shopify merchants processed $378.4 billion in gross merchandise volume in 2025, and a large share of US direct-to-consumer brands sell through it. Most of those stores answer a simple request, /products.json , with their…

## What’s new and why it matters
Shopify merchants processed $378.4 billion in gross merchandise volume in 2025, and a large share of US direct-to-consumer brands sell through it. Most of those stores answer a simple request, /products.json , with their full public catalog in JSON. Tutorials explain the endpoint in two paragraphs. We wanted numbers, so we tested it on 68 brand domains. TL;DR 50 of 68 brand domains returned a usable catalog from /products.json . The rest blocked us, returned 404 or didn't answer a cross-origin request. No store ever returned more than 250 products per page , even when we asked for 500. There i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rslndev/we-tested-shopifys-productsjson-on-68-stores-the-limits-tutorials-dont-mention-1ofj

## Related notes
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-04-15-sql-limit-and-offset-paginate-your-query-results-like-a-pro]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-15-looking-for-a-multimarket-stock-api-pull-ashare-hong-kong-and-us-quotes-in-python]]
- [[2026-08-07-i-paged-a-table-with-no-order-by-and-lost-2797-rows]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
