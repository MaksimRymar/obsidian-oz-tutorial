---
title: I Built a Threat Intelligence Tool That Maps Malicious IPs in Real Time
date: '2026-03-14'
source: https://dev.to/shynsec/i-built-a-threat-intelligence-tool-that-maps-malicious-ips-in-real-time-1cjb
domain: Python
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]'
- '[[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-08-understanding-group-by-in-sql]]'
status: unread
---

> **TL;DR:** What I Built The Breadcrumb Engine is a Python tool that takes a list of IP addresses and plots them on an interactive dark-mode map, enriched with real-time threat intelligence from VirusTotal. Each IP is colour-coded b…

## What’s new and why it matters
What I Built The Breadcrumb Engine is a Python tool that takes a list of IP addresses and plots them on an interactive dark-mode map, enriched with real-time threat intelligence from VirusTotal. Each IP is colour-coded by risk level and the full dataset is exportable as CSV. 🟢 Green → 0–4% (Clean) 🟠 Orange → 5–14% (Suspicious) 🔴 Red → 15%+ (Malicious) The Stack Streamlit — web UI with zero frontend code Folium — interactive map rendering on a CartoDB dark basemap VirusTotal API — aggregates 90+ security vendor votes per IP ipinfo.io — HTTPS geolocation pandas — data handling and CSV export Wha…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/shynsec/i-built-a-threat-intelligence-tool-that-maps-malicious-ips-in-real-time-1cjb

## Related notes
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]
- [[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-08-understanding-group-by-in-sql]]
