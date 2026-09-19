---
title: Our scraper went 0-for-19 against Cloudflare. One boolean took it to 9-for-10.
date: '2026-09-19'
source: https://dev.to/devil_scrapes/our-scraper-went-0-for-19-against-cloudflare-one-boolean-took-it-to-9-for-10-2lac
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#tool'
related:
- '[[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-09-18-why-your-youtube-transcript-scraper-says-no-captions-found-on-a-video-that-has-captions]]'
status: unread
---

> **TL;DR:** Quick answer: our Upwork scraper cleared Cloudflare 4/4 on a laptop and then scored 0 out of 19 on the first nineteen cloud attempts. Nothing about Upwork changed in between. The fix was one boolean — geoip=True on the b…

## What’s new and why it matters
Quick answer: our Upwork scraper cleared Cloudflare 4/4 on a laptop and then scored 0 out of 19 on the first nineteen cloud attempts. Nothing about Upwork changed in between. The fix was one boolean — geoip=True on the browser — and the next ten attempts scored 9 . The full 2x2: bare cloud IP 0/7, residential proxy without geoip 0/12 , residential proxy with geoip 9/10 . Both conditions are required and neither one is sufficient. Why does a residential proxy alone score zero against Cloudflare? Because the proxy fixes your IP and says nothing about your browser, and Cloudflare compares the two…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/devil_scrapes/our-scraper-went-0-for-19-against-cloudflare-one-boolean-took-it-to-9-for-10-2lac

## Related notes
- [[2026-08-17-a-finished-scraper-sat-on-a-git-branch-for-19-days-nothing-noticed]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-09-18-why-your-youtube-transcript-scraper-says-no-captions-found-on-a-video-that-has-captions]]
