---
title: 'HN Job Exporter: Automate Real-Time Hacker News Job Tracking'
date: '2026-05-11'
source: https://dev.to/intellitools/hn-job-exporter-automate-real-time-hacker-news-job-tracking-275n
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-05-11-hn-job-scraper-pro-real-time-hacker-news-job-data-automation]]'
- '[[2026-04-05-how-to-extract-google-maps-data-with-python-script]]'
- '[[2026-05-09-generate-html-reports-with-python-in-10-lines-of-code]]'
- '[[2026-04-03-how-to-automate-fvwm-perl-to-python-converter-with-python]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-18-how-i-automate-my-freelance-workflow-with-python]]'
status: unread
---

> **TL;DR:** import requests from bs4 import BeautifulSoup import csv def fetch_hn_jobs ( page = 0 ): url = f ' https://news.ycombinator.com/jobs?show=story&sort=votes&desc=1&page= { page } ' headers = { ' User-Agent ' : ' Mozilla/5.…

## What’s new and why it matters
import requests from bs4 import BeautifulSoup import csv def fetch_hn_jobs ( page = 0 ): url = f ' https://news.ycombinator.com/jobs?show=story&sort=votes&desc=1&page= { page } ' headers = { ' User-Agent ' : ' Mozilla/5.0 ' } response = requests . get ( url , headers = headers ) soup = BeautifulSoup ( response . text , ' html.parser ' ) jobs = [] for item in soup . select ( ' .story ' ): title = item . select_one ( ' a.storylink ' ). text . strip () link = item . select_one ( ' a.storylink ' )[ ' href ' ] company = item . select_one ( ' .subtext a ' ). text . strip () jobs . append (( company…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/intellitools/hn-job-exporter-automate-real-time-hacker-news-job-tracking-275n

## Related notes
- [[2026-05-11-hn-job-scraper-pro-real-time-hacker-news-job-data-automation]]
- [[2026-04-05-how-to-extract-google-maps-data-with-python-script]]
- [[2026-05-09-generate-html-reports-with-python-in-10-lines-of-code]]
- [[2026-04-03-how-to-automate-fvwm-perl-to-python-converter-with-python]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-18-how-i-automate-my-freelance-workflow-with-python]]
