---
title: Apple's app review RSS feed is empty now — here's what the App Store itself
  uses
date: '2026-09-27'
source: https://dev.to/chorelet/apples-app-review-rss-feed-is-empty-now-heres-what-the-app-store-itself-uses-37m8
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-09-11-every-tennis-match-with-15-bookmakers-form-and-head-to-head-in-one-json-row]]'
- '[[2026-09-24-how-to-get-tesco-prices-with-an-api-in-2026]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-02-workdays-job-api-tells-you-there-are-2000-jobs-then-says-0-on-page-two]]'
status: unread
---

> **TL;DR:** For years the way to read App Store reviews without being the app's owner was one URL: https://itunes.apple.com/us/rss/customerreviews/id=310633997/sortBy=mostRecent/page=1/json It still answers 200 OK . It just doesn't…

## What’s new and why it matters
For years the way to read App Store reviews without being the app's owner was one URL: https://itunes.apple.com/us/rss/customerreviews/id=310633997/sortBy=mostRecent/page=1/json It still answers 200 OK . It just doesn't return any reviews any more. import requests r = requests . get ( " https://itunes.apple.com/us/rss/customerreviews/ " " id=310633997/sortBy=mostRecent/page=1/json " , timeout = 30 ) print ( r . status_code , " entry " in r . json ()[ " feed " ]) # 200 False I checked Skype ( 284862083 ), WhatsApp ( 310633997 ) and YouTube ( 544007664 ) in both us and gb , from a home connectio…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/chorelet/apples-app-review-rss-feed-is-empty-now-heres-what-the-app-store-itself-uses-37m8

## Related notes
- [[2026-08-20-apify-store-scraper-market-intelligence-on-every-public-actor-in-2026]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-09-11-every-tennis-match-with-15-bookmakers-form-and-head-to-head-in-one-json-row]]
- [[2026-09-24-how-to-get-tesco-prices-with-an-api-in-2026]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-02-workdays-job-api-tells-you-there-are-2000-jobs-then-says-0-on-page-two]]
