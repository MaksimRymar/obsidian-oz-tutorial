---
title: 'Bulk domain age, expiry and DNS audit in Python: RDAP with WHOIS fallback'
date: '2026-10-05'
source: https://dev.to/siftwright/bulk-domain-age-expiry-and-dns-audit-in-python-rdap-with-whois-fallback-5ah7
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-26-python-for-data-analytics-a-hands-on-field-guide]]'
- '[[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** A domain list is a surprisingly useful dataset. Which of your 500 customer domains expire this quarter? Which lead domains were registered last month (often a trust signal)? Which of your own domains have no DMARC record…

## What’s new and why it matters
A domain list is a surprisingly useful dataset. Which of your 500 customer domains expire this quarter? Which lead domains were registered last month (often a trust signal)? Which of your own domains have no DMARC record? All of it is public data, but getting it for a whole list means juggling RDAP, legacy WHOIS servers and DNS lookups. This tutorial uses one Apify Actor, Domain WHOIS & DNS Lookup , to turn a list of domains into clean JSON rows: registrar, creation and expiry dates, age, nameservers, plus MX, SPF and DMARC. I'm the maker, so the pricing is stated up front: $1 per 1,000 domain…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/siftwright/bulk-domain-age-expiry-and-dns-audit-in-python-rdap-with-whois-fallback-5ah7

## Related notes
- [[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-26-python-for-data-analytics-a-hands-on-field-guide]]
- [[2026-05-16-automated-domain-investing-with-hard-budget-walls-and-an-ai-council-that-has-to-agree-before-any-money-moves]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
