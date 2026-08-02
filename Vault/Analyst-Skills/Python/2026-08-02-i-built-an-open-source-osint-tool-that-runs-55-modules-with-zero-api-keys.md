---
title: I built an open-source OSINT tool that runs 55 modules with zero API keys
date: '2026-08-02'
source: https://dev.to/flowthingy/i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys-1614
domain: Python
relevance: 🔴
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-01-i-built-an-osint-aggregator-that-queries-5-threat-intel-sources-in-one-command]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-03-30-ghostintel-v25-what-changed-since-i-first-posted-about-it]]'
- '[[2026-05-29-building-helix-an-open-source-visual-identity-mapper-that-cuts-the-noise]]'
- '[[2026-06-15-wayback-video-turn-any-sites-history-into-a-video]]'
status: unread
---

> **TL;DR:** Been learning web security for a while and kept jumping between different tools for every recon task so I just built my own. It's a Python script with a terminal menu. Give it a URL and it runs subdomains, directory brut…

## What’s new and why it matters
Been learning web security for a while and kept jumping between different tools for every recon task so I just built my own. It's a Python script with a terminal menu. Give it a URL and it runs subdomains, directory bruteforce, JS secret scanning, DNS, headers, SSL, CORS, Shodan, VirusTotal, email security, username search across 30 platforms, GitHub commit email mining. Spits out a report at the end automatically. No API keys needed for any of it. The JS secret detection took a while to get right. Pure regex gives too much noise so I added Shannon entropy scoring on top to filter out placehol…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/flowthingy/i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys-1614

## Related notes
- [[2026-05-01-i-built-an-osint-aggregator-that-queries-5-threat-intel-sources-in-one-command]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-03-30-ghostintel-v25-what-changed-since-i-first-posted-about-it]]
- [[2026-05-29-building-helix-an-open-source-visual-identity-mapper-that-cuts-the-noise]]
- [[2026-06-15-wayback-video-turn-any-sites-history-into-a-video]]
