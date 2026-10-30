---
title: Get Google Trends 'Trending now' for any country with Python (RSS + a many-country
  shortcut)
date: '2026-10-30'
source: https://dev.to/hi_hphanthanh_41c4083/get-google-trends-trending-now-for-any-country-with-python-rss-a-many-country-shortcut-12kb
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-28-look-up-a-companys-lei-sec-filings-and-revenue-with-python-gleif-sec-edgar-no-api-key]]'
- '[[2026-10-12-espn-scores-scraper-a-game-that-has-not-started-still-shows-0-0]]'
- '[[2026-10-05-how-to-get-google-search-volume-for-a-list-of-keywords-without-a-google-ads-account]]'
- '[[2026-10-20-how-to-get-a-list-of-uk-companies-by-sic-code-and-postcode-no-api-key]]'
- '[[2026-09-27-normalizing-public-job-board-data-with-python]]'
- '[[2026-10-11-how-to-export-google-play-reviews-to-csv-for-any-app-and-country]]'
status: unread
---

> **TL;DR:** Content, SEO and newsroom teams often want one thing from Google Trends: what is spiking right now in a given country. Google has no official API for it, but the "Trending now" page is backed by a public RSS feed that ne…

## What’s new and why it matters
Content, SEO and newsroom teams often want one thing from Google Trends: what is spiking right now in a given country. Google has no official API for it, but the "Trending now" page is backed by a public RSS feed that needs no key, cookies or proxy. DIY: read the RSS feed # pip install requests import requests import xml.etree.ElementTree as ET NS = { " ht " : " https://trends.google.com/trending/rss " } def trending ( geo = " US " , n = 3 ): r = requests . get ( " https://trends.google.com/trending/rss " , params = { " geo " : geo }, headers = { " User-Agent " : " Mozilla/5.0 " }, timeout = 2…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hi_hphanthanh_41c4083/get-google-trends-trending-now-for-any-country-with-python-rss-a-many-country-shortcut-12kb

## Related notes
- [[2026-10-28-look-up-a-companys-lei-sec-filings-and-revenue-with-python-gleif-sec-edgar-no-api-key]]
- [[2026-10-12-espn-scores-scraper-a-game-that-has-not-started-still-shows-0-0]]
- [[2026-10-05-how-to-get-google-search-volume-for-a-list-of-keywords-without-a-google-ads-account]]
- [[2026-10-20-how-to-get-a-list-of-uk-companies-by-sic-code-and-postcode-no-api-key]]
- [[2026-09-27-normalizing-public-job-board-data-with-python]]
- [[2026-10-11-how-to-export-google-play-reviews-to-csv-for-any-app-and-country]]
