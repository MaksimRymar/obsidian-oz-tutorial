---
title: 'Tracking Keyword Rankings with Python + CSV: A Lightweight SEO Experiment'
date: '2026-05-29'
source: https://dev.to/emma-watson3/tracking-keyword-rankings-with-python-csv-a-lightweight-seo-experiment-2nlc
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-25-i-built-a-recession-indicator-dashboard-with-free-apis-what-signals-do-you-track]]'
- '[[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]'
- '[[2026-04-11-how-i-built-a-defi-yield-dashboard-in-50-lines-of-python]]'
- '[[2026-03-21-web-scraping-with-python-vs-nodejs-which-should-you-choose-in-2026]]'
- '[[2026-05-14-python-web-scraping-extract-data-from-any-website-in-2024]]'
- '[[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]'
status: unread
---

> **TL;DR:** I've been experimenting with a lightweight approach to track keyword ranking changes using Python and a simple CSV file. Here's the gist: python import csv import requests from datetime import datetime def check_ranking(…

## What’s new and why it matters
I've been experimenting with a lightweight approach to track keyword ranking changes using Python and a simple CSV file. Here's the gist: python import csv import requests from datetime import datetime def check_ranking(keyword, url): # Simplified ranking check - actual implementation would use search API # This is just a placeholder return {'keyword': keyword, 'url': url, 'rank': 5, 'date': datetime.now().isoformat()} def update_tracker(csv_path, keywords): with open(csv_path, 'a', newline='') as csvfile: writer = csv.DictWriter(csvfile, fieldnames=['keyword', 'url', 'rank', 'date']) if csvfi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/emma-watson3/tracking-keyword-rankings-with-python-csv-a-lightweight-seo-experiment-2nlc

## Related notes
- [[2026-03-25-i-built-a-recession-indicator-dashboard-with-free-apis-what-signals-do-you-track]]
- [[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]
- [[2026-04-11-how-i-built-a-defi-yield-dashboard-in-50-lines-of-python]]
- [[2026-03-21-web-scraping-with-python-vs-nodejs-which-should-you-choose-in-2026]]
- [[2026-05-14-python-web-scraping-extract-data-from-any-website-in-2024]]
- [[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]
