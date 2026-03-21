---
title: Stop Parsing HTML — 7 Websites That Give You JSON If You Ask Nicely
date: '2026-03-20'
source: https://dev.to/__8ef7243a4f/stop-parsing-html-7-websites-that-give-you-json-if-you-ask-nicely-58lh
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-20-scraping-hacker-news-in-2026-complete-guide-algolia-api-date-filters]]'
- '[[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]'
- '[[2026-02-28-how-to-detect-energy-sentiment-shifts-with-the-pulsebit-api-python]]'
- '[[2026-03-02-python-asyncio-for-web-scraping-speed-up-10x]]'
- '[[2026-03-02-web-scraping-vs-api-when-to-use-each-with-examples]]'
- '[[2026-02-24-stop-writing-css-selectors-that-break---extract-web-data-with-plain-english-using-ai]]'
status: unread
---

> **TL;DR:** Most web scraping tutorials start with BeautifulSoup or Cheerio. But many popular websites already return structured JSON — you just need to know how to ask. 1. Reddit Append .json to any URL: https://www.reddit.com/r/we…

## What’s new and why it matters
Most web scraping tutorials start with BeautifulSoup or Cheerio. But many popular websites already return structured JSON — you just need to know how to ask. 1. Reddit Append .json to any URL: https://www.reddit.com/r/webdev.json https://www.reddit.com/r/python/top.json?t=week 2. YouTube (Innertube API) fetch ( " https://www.youtube.com/youtubei/v1/search " , { method : " POST " , body : JSON . stringify ({ context : { client : { clientName : " WEB " , clientVersion : " 2.20240101 " } }, query : " python tutorial " }) }); 3. Hacker News (Algolia) https://hn.algolia.com/api/v1/search?query=pyth…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/__8ef7243a4f/stop-parsing-html-7-websites-that-give-you-json-if-you-ask-nicely-58lh

## Related notes
- [[2026-03-20-scraping-hacker-news-in-2026-complete-guide-algolia-api-date-filters]]
- [[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]
- [[2026-02-28-how-to-detect-energy-sentiment-shifts-with-the-pulsebit-api-python]]
- [[2026-03-02-python-asyncio-for-web-scraping-speed-up-10x]]
- [[2026-03-02-web-scraping-vs-api-when-to-use-each-with-examples]]
- [[2026-02-24-stop-writing-css-selectors-that-break---extract-web-data-with-plain-english-using-ai]]
