---
title: How to Scrape YouTube Comments Without the API (Reverse Engineering InnerTube)
date: '2026-04-03'
source: https://dev.to/vhub_systems_ed5641f65d59/how-to-scrape-youtube-comments-without-the-api-reverse-engineering-innertube-42pe
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-20-youtube-has-a-hidden-api-that-needs-no-api-key-heres-how-to-use-it]]'
- '[[2026-03-20-scraping-youtube-channel-data-in-2026-videos-playlists-and-metadata]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-20-scraping-github-data-in-2026-repos-users-and-organizations-via-api]]'
- '[[2026-03-20-stop-parsing-html-7-websites-that-give-you-json-if-you-ask-nicely]]'
status: unread
---

> **TL;DR:** YouTube's official Data API v3 gives you 10,000 units per day. A single commentThreads.list request costs 1 unit — so you get 10,000 comment pages per day maximum. In practice, for any analysis at scale, you hit this lim…

## What’s new and why it matters
YouTube's official Data API v3 gives you 10,000 units per day. A single commentThreads.list request costs 1 unit — so you get 10,000 comment pages per day maximum. In practice, for any analysis at scale, you hit this limit in minutes. There's a better way: YouTube's internal InnerTube API, which is what the YouTube website itself uses. No quota limits, no API key required. What is InnerTube? InnerTube is YouTube's internal JSON API. Every request your browser makes when loading YouTube — video metadata, comments, search results — goes through InnerTube endpoints at https://www.youtube.com/yout…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vhub_systems_ed5641f65d59/how-to-scrape-youtube-comments-without-the-api-reverse-engineering-innertube-42pe

## Related notes
- [[2026-03-20-youtube-has-a-hidden-api-that-needs-no-api-key-heres-how-to-use-it]]
- [[2026-03-20-scraping-youtube-channel-data-in-2026-videos-playlists-and-metadata]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-20-scraping-github-data-in-2026-repos-users-and-organizations-via-api]]
- [[2026-03-20-stop-parsing-html-7-websites-that-give-you-json-if-you-ask-nicely]]
