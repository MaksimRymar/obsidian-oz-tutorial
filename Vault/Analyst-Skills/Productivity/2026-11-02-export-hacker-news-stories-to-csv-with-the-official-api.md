---
title: Export Hacker News stories to CSV with the official API
date: '2026-11-02'
source: https://dev.to/dannnne84/export-hacker-news-stories-to-csv-with-the-official-api-1j6e
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-07-18-how-to-scrape-gleif-lei-free-no-code-guide-2026]]'
- '[[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]'
- '[[2026-10-12-espn-scores-scraper-a-game-that-has-not-started-still-shows-0-0]]'
- '[[2026-07-13-how-to-scrape-hacker-news-who-is-hiring-free-no-code-guide-2026]]'
- '[[2026-07-13-how-to-scrape-habitacliacom-property-free-no-code-guide-2026]]'
- '[[2026-07-13-how-to-scrape-numbeo-free-no-code-guide-2026]]'
status: unread
---

> **TL;DR:** Hacker News has a free, official API. You don't need to scrape the website. This post shows how to pull the top stories into a CSV file, filter them by keyword, and keep a feed running. How the API works Hacker News publ…

## What’s new and why it matters
Hacker News has a free, official API. You don't need to scrape the website. This post shows how to pull the top stories into a CSV file, filter them by keyword, and keep a feed running. How the API works Hacker News publishes its data through a Firebase-hosted API at https://hacker-news.firebaseio.com/v0/ . Two calls cover most needs: topstories.json returns up to 500 story ids. newstories.json , beststories.json , askstories.json , showstories.json and jobstories.json work the same way. item/<id>.json returns one story: title, link, author, score, comment count and time. The API documentation…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dannnne84/export-hacker-news-stories-to-csv-with-the-official-api-1j6e

## Related notes
- [[2026-07-18-how-to-scrape-gleif-lei-free-no-code-guide-2026]]
- [[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]
- [[2026-10-12-espn-scores-scraper-a-game-that-has-not-started-still-shows-0-0]]
- [[2026-07-13-how-to-scrape-hacker-news-who-is-hiring-free-no-code-guide-2026]]
- [[2026-07-13-how-to-scrape-habitacliacom-property-free-no-code-guide-2026]]
- [[2026-07-13-how-to-scrape-numbeo-free-no-code-guide-2026]]
