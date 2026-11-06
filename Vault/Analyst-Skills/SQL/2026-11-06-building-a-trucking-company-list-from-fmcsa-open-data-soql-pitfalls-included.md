---
title: Building a Trucking Company List From FMCSA Open Data (SoQL Pitfalls Included)
date: '2026-11-06'
source: https://dev.to/dedicated_crest/building-a-trucking-company-list-from-fmcsa-open-data-soql-pitfalls-included-4jo9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-04-reading-medium-articles-by-tag-author-and-publication-with-rss-and-where-it-stops]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]'
status: unread
---

> **TL;DR:** Disclosure: I'm Ben, and I built the Apify Actor mentioned later in this post. I charge per result for it. The tutorial part uses only free public data. Freight insurance agents, factoring companies, ELD and fuel-card se…

## What’s new and why it matters
Disclosure: I'm Ben, and I built the Apify Actor mentioned later in this post. I charge per result for it. The tutorial part uses only free public data. Freight insurance agents, factoring companies, ELD and fuel-card sellers, and brokers looking for capacity all need the same thing: a list of trucking companies with a phone number and fleet size. People pay for those lists, but the source behind most of them is free. Every US interstate carrier files an MCS-150 with FMCSA, and US DOT publishes the result as open data, refreshed daily. Here's how to query it yourself, and what tripped me up. T…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dedicated_crest/building-a-trucking-company-list-from-fmcsa-open-data-soql-pitfalls-included-4jo9

## Related notes
- [[2026-11-04-reading-medium-articles-by-tag-author-and-publication-with-rss-and-where-it-stops]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-10-15-the-list-shows-two-numbers-so-the-query-digs-them-out-of-the-json-instead-of-loading-a-hundred-attempts]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]
