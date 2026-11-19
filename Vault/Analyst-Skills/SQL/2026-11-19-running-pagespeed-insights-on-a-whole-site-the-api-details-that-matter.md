---
title: 'Running PageSpeed Insights on a whole site: the API details that matter'
date: '2026-11-19'
source: https://dev.to/zachary_klein_a8078ed2a7f/running-pagespeed-insights-on-a-whole-site-the-api-details-that-matter-4lc8
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#presentations'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]'
- '[[2026-11-04-reading-medium-articles-by-tag-author-and-publication-with-rss-and-where-it-stops]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-11-07-audit-1000-websites-for-speed-seo-ai-crawler-access-and-domain-expiry-with-plain-python-no-scraping]]'
status: unread
---

> **TL;DR:** "Is there a tool to run PageSpeed Insights on all my pages at once?" comes up constantly in SEO and web dev forums. The answer is yes, Google gives you an API for exactly this. The harder part is everything around it: fi…

## What’s new and why it matters
"Is there a tool to run PageSpeed Insights on all my pages at once?" comes up constantly in SEO and web dev forums. The answer is yes, Google gives you an API for exactly this. The harder part is everything around it: finding the pages, staying inside quota, handling 40-second responses, and reading the results without being fooled by noise. These are my notes from building a bulk auditor on top of the PageSpeed Insights (PSI) and Chrome UX Report (CrUX) APIs. At the end there is the hosted version I published on Apify. Disclosure: I built it. The API call One audit is one GET: GET https : //w…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zachary_klein_a8078ed2a7f/running-pagespeed-insights-on-a-whole-site-the-api-details-that-matter-4lc8

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]
- [[2026-11-04-reading-medium-articles-by-tag-author-and-publication-with-rss-and-where-it-stops]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-11-07-audit-1000-websites-for-speed-seo-ai-crawler-access-and-domain-expiry-with-plain-python-no-scraping]]
