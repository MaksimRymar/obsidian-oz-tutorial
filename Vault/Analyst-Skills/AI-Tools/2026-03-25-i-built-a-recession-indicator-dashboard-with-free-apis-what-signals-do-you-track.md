---
title: I Built a Recession Indicator Dashboard With Free APIs — What Signals Do You
  Track?
date: '2026-03-25'
source: https://dev.to/0012303/i-built-a-recession-indicator-dashboard-with-free-apis-what-signals-do-you-track-4h3o
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]'
- '[[2026-02-27-how-to-build-a-competitive-intelligence-tool-that-reveals-any-companys-tech-stack]]'
- '[[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]'
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
status: unread
---

> **TL;DR:** I've been obsessed with economic data APIs lately, and I ended up building a simple recession probability dashboard using completely free data sources. Here's what I'm tracking: The Signals 1. Yield Curve Inversion (FRED…

## What’s new and why it matters
I've been obsessed with economic data APIs lately, and I ended up building a simple recession probability dashboard using completely free data sources. Here's what I'm tracking: The Signals 1. Yield Curve Inversion (FRED: T10Y2Y) When the 10-year Treasury yield drops below the 2-year yield, it has preceded every US recession since 1955. Currently: the curve has been inverted for months. import requests FRED_KEY = " your_key " def get_latest ( series_id ): url = " https://api.stlouisfed.org/fred/series/observations " params = { " series_id " : series_id , " api_key " : FRED_KEY , " file_type "…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/0012303/i-built-a-recession-indicator-dashboard-with-free-apis-what-signals-do-you-track-4h3o

## Related notes
- [[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]
- [[2026-02-27-how-to-build-a-competitive-intelligence-tool-that-reveals-any-companys-tech-stack]]
- [[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
