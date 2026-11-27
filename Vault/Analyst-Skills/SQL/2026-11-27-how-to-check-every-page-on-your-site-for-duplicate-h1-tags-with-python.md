---
title: How to Check Every Page on Your Site for Duplicate H1 Tags with Python
date: '2026-11-27'
source: https://dev.to/evgeniikaya/how-to-check-every-page-on-your-site-for-duplicate-h1-tags-with-python-47mm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-07-01-how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export]]'
- '[[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** When we audited all 199 content URLs on our site, we did not start with Search Console. We started with the HTML the server actually sends, and with a short checklist for each page. One of the simplest checks on that lis…

## What’s new and why it matters
When we audited all 199 content URLs on our site, we did not start with Search Console. We started with the HTML the server actually sends, and with a short checklist for each page. One of the simplest checks on that list is also one of the easiest to skip: how many H1 headings does this page have? You want one. A template can add a second without anyone typing it, and once that happens it tends to happen on every page that uses the same template. Here is the small script we used to find that, and to see whether the extras shared a class, which usually means one template fix rather than a page…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/evgeniikaya/how-to-check-every-page-on-your-site-for-duplicate-h1-tags-with-python-47mm

## Related notes
- [[2026-10-25-a-free-python-script-to-audit-your-sites-on-page-seo-titles-meta-h1s-broken-links]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-07-01-how-to-write-a-python-script-that-finds-cannibalized-queries-in-a-search-console-export]]
- [[2026-11-18-google-maps-rank-tracker-check-your-google-maps-ranking-from-every-street-around-you]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
