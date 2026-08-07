---
title: I Queried 50 Company Profiles — Here's What I Learned About AMD
date: '2026-08-07'
source: https://dev.to/onizuka/i-queried-50-company-profiles-heres-what-i-learned-about-amd-21oe
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]'
- '[[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]'
status: unread
---

> **TL;DR:** webdev, #ai, #api, #discuss AMD just spent $390 million in stock to buy Taalas, a 35-person startup that etches AI models directly into silicon. The press release called it a "strategic move to accelerate inference perfo…

## What’s new and why it matters
webdev, #ai, #api, #discuss AMD just spent $390 million in stock to buy Taalas, a 35-person startup that etches AI models directly into silicon. The press release called it a "strategic move to accelerate inference performance." I didn't buy the phrase, so I wrote a script and pulled 50 company profiles to see what the data actually says. import os import requests API_KEY = os . environ . get ( " RAPIDAPI_KEY " ) BASE = " https://company-info1.p.rapidapi.com " HEADERS = { " X-RapidAPI-Key " : API_KEY , " X-RapidAPI-Host " : " company-info1.p.rapidapi.com " } def lookup ( domain ): url = f " {…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/onizuka/i-queried-50-company-profiles-heres-what-i-learned-about-amd-21oe

## Related notes
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-07-28-how-i-made-sure-you-cant-like-and-dislike-the-same-post-at-once]]
- [[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]
