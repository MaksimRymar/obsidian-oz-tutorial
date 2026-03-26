---
title: httpx Is What requests Should Have Been — Async, HTTP/2, and Better Defaults
date: '2026-03-26'
source: https://dev.to/0012303/httpx-is-what-requests-should-have-been-async-http2-and-better-defaults-31g8
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-03-01-async-python-made-simple-a-practical-guide-to-asyncio]]'
- '[[2026-03-25-nasa-has-20-free-apis-asteroids-mars-photos-exoplanets-and-more-no-signup]]'
- '[[2026-03-16-pay-per-request-apis-from-python-skip-the-api-key-pay-with-usdc-instead]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]'
- '[[2026-03-02-python-asyncio-for-web-scraping-speed-up-10x]]'
status: unread
---

> **TL;DR:** I stopped using the requests library 2 years ago. httpx does everything requests does, plus async, HTTP/2, and better defaults. Here is why and how to switch. Install pip install httpx Drop-in replacement. Most requests…

## What’s new and why it matters
I stopped using the requests library 2 years ago. httpx does everything requests does, plus async, HTTP/2, and better defaults. Here is why and how to switch. Install pip install httpx Drop-in replacement. Most requests code works with zero changes. The Basics import httpx # GET request (identical to requests) resp = httpx . get ( " https://httpbin.org/get " ) print ( resp . status_code ) # 200 print ( resp . json ()) # POST with JSON resp = httpx . post ( " https://httpbin.org/post " , json = { " key " : " value " }) # Headers resp = httpx . get ( " https://api.github.com/user " , headers = {…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/0012303/httpx-is-what-requests-should-have-been-async-http2-and-better-defaults-31g8

## Related notes
- [[2026-03-01-async-python-made-simple-a-practical-guide-to-asyncio]]
- [[2026-03-25-nasa-has-20-free-apis-asteroids-mars-photos-exoplanets-and-more-no-signup]]
- [[2026-03-16-pay-per-request-apis-from-python-skip-the-api-key-pay-with-usdc-instead]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]
- [[2026-03-02-python-asyncio-for-web-scraping-speed-up-10x]]
