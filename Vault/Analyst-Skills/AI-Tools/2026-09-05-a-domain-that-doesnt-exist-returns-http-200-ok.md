---
title: A domain that doesn't exist returns HTTP 200 OK
date: '2026-09-05'
source: https://dev.to/devil_scrapes/a-domain-that-doesnt-exist-returns-http-200-ok-1omo
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
status: unread
---

> **TL;DR:** Quick answer Query a domain that does not exist over DNS-over-HTTPS and you get HTTP 200 OK . The failure is in the JSON body, as "Status": 3 . If your DoH client checks response.raise_for_status() and moves on, every no…

## What’s new and why it matters
Quick answer Query a domain that does not exist over DNS-over-HTTPS and you get HTTP 200 OK . The failure is in the JSON body, as "Status": 3 . If your DoH client checks response.raise_for_status() and moves on, every nonexistent domain in your list looks like a successful lookup that happened to return no records. Which is also exactly what a real domain with no MX record looks like. DoH is a transport, not a result 🌐 This is the mental model that fixes it. cloudflare-dns.com/dns-query is not a REST API that answers questions about domains. It is DNS wrapped in HTTP , and the two layers repor…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/a-domain-that-doesnt-exist-returns-http-200-ok-1omo

## Related notes
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
