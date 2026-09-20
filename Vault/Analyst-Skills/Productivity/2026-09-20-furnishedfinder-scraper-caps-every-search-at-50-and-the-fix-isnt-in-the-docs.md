---
title: 'FurnishedFinder Scraper: caps every search at 50, and the fix isn''t in the
  docs'
date: '2026-09-20'
source: https://dev.to/devil_scrapes/furnishedfinder-scraper-caps-every-search-at-50-and-the-fix-isnt-in-the-docs-2ke4
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#productivity'
- '#tool'
related:
- '[[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]'
- '[[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]'
status: unread
---

> **TL;DR:** Quick answer FurnishedFinder's public search API hard-caps every response at exactly 50 listings — confirmed across 6 of 6 test metros, regardless of viewport size or density — and there is no page , cursor , after , off…

## What’s new and why it matters
Quick answer FurnishedFinder's public search API hard-caps every response at exactly 50 listings — confirmed across 6 of 6 test metros, regardless of viewport size or density — and there is no page , cursor , after , offset , limit , or first argument on the search field to page past it. The obvious GraphQL fix — a $loc: SearchRequestLocationInput! variable, the type name the API's own field-error introspection implies should exist — returns a clean 400 Unknown type . The query that actually works passes the location filter as an inline literal in the query text , not a variable at all. We til…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/devil_scrapes/furnishedfinder-scraper-caps-every-search-at-50-and-the-fix-isnt-in-the-docs-2ke4

## Related notes
- [[2026-09-17-no-introspection-no-allowlist-reconstructing-whatnots-graphql-queries-from-a-compiled-ast]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]
- [[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]
