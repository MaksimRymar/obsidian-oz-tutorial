---
title: Building a Political Donor Tracker with FEC Campaign Finance Data
date: '2026-03-27'
source: https://dev.to/agenthustler/building-a-political-donor-tracker-with-fec-campaign-finance-data-1en2
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-08-build-a-website-tech-stack-scanner-in-python-under-50-lines]]'
- '[[2026-03-20-scraping-github-data-in-2026-repos-users-and-organizations-via-api]]'
- '[[2026-03-20-scraping-hacker-news-in-2026-complete-guide-algolia-api-date-filters]]'
- '[[2026-03-25-nasa-has-20-free-apis-asteroids-mars-photos-exoplanets-and-more-no-signup]]'
- '[[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]'
- '[[2026-03-17-linkedin-scraping-in-2026-api-benchmarks-legal-risks-and-what-actually-works]]'
status: unread
---

> **TL;DR:** Campaign finance data is public by law. The FEC publishes every donation over $200 to federal candidates. This data powers investigative journalism, civic tech, and political research. Here's how to build a donor trackin…

## What’s new and why it matters
Campaign finance data is public by law. The FEC publishes every donation over $200 to federal candidates. This data powers investigative journalism, civic tech, and political research. Here's how to build a donor tracking system. FEC Data Sources Bulk data : Downloadable CSV files updated nightly API : REST API at api.open.fec.gov (free API key required) Website : fec.gov with searchable database Using the FEC API import requests import time from collections import defaultdict class FECTracker : BASE_URL = " https://api.open.fec.gov/v1 " def __init__ ( self , api_key ): self . api_key = api_ke…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/agenthustler/building-a-political-donor-tracker-with-fec-campaign-finance-data-1en2

## Related notes
- [[2026-03-08-build-a-website-tech-stack-scanner-in-python-under-50-lines]]
- [[2026-03-20-scraping-github-data-in-2026-repos-users-and-organizations-via-api]]
- [[2026-03-20-scraping-hacker-news-in-2026-complete-guide-algolia-api-date-filters]]
- [[2026-03-25-nasa-has-20-free-apis-asteroids-mars-photos-exoplanets-and-more-no-signup]]
- [[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]
- [[2026-03-17-linkedin-scraping-in-2026-api-benchmarks-legal-risks-and-what-actually-works]]
