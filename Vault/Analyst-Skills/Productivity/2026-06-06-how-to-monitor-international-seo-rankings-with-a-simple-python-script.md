---
title: How to Monitor International SEO Rankings with a Simple Python Script
date: '2026-06-06'
source: https://dev.to/kevincarroll85/how-to-monitor-international-seo-rankings-with-a-simple-python-script-5cl7
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-11-how-i-built-a-defi-yield-dashboard-in-50-lines-of-python]]'
- '[[2026-05-29-tracking-keyword-rankings-with-python-csv-a-lightweight-seo-experiment]]'
- '[[2026-03-02-build-a-website-health-monitor-in-50-lines-of-python]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-03-08-build-a-website-tech-stack-scanner-in-python-under-50-lines]]'
- '[[2026-06-04-how-to-handle-location-spoofing-for-accurate-local-seo-testing]]'
status: unread
---

> **TL;DR:** Need to check if your site is ranking for a specific keyword in different countries? I wrote a quick Python script that uses the SERPSpur API to check rankings across multiple locations: python import requests API_KEY =…

## What’s new and why it matters
Need to check if your site is ranking for a specific keyword in different countries? I wrote a quick Python script that uses the SERPSpur API to check rankings across multiple locations: python import requests API_KEY = "your_api_key_here" def check_rankings(domain, keyword, locations): results = {} for location in locations: response = requests.get( " https://api.serspur.com/v1/search ", headers={"Authorization": f"Bearer {API_KEY}"}, params={"q": keyword, "location": location, "num": 100} ) data = response.json() for i, result in enumerate(data['organic_results'], 1): if domain in result['li…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kevincarroll85/how-to-monitor-international-seo-rankings-with-a-simple-python-script-5cl7

## Related notes
- [[2026-04-11-how-i-built-a-defi-yield-dashboard-in-50-lines-of-python]]
- [[2026-05-29-tracking-keyword-rankings-with-python-csv-a-lightweight-seo-experiment]]
- [[2026-03-02-build-a-website-health-monitor-in-50-lines-of-python]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-03-08-build-a-website-tech-stack-scanner-in-python-under-50-lines]]
- [[2026-06-04-how-to-handle-location-spoofing-for-accurate-local-seo-testing]]
