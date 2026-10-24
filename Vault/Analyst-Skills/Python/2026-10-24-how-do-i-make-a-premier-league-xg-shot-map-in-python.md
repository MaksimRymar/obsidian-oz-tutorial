---
title: How do I make a Premier League xG shot map in Python?
date: '2026-10-24'
source: https://dev.to/noahowsh/how-do-i-make-a-premier-league-xg-shot-map-in-python-pen
domain: Python
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tutorial'
related:
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]'
- '[[2026-09-26-python-pandas-dataframe-a-beginners-guide]]'
- '[[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
status: unread
---

> **TL;DR:** Every located shot a club took in a season, with player, outcome, body part, expected goals and pitch coordinates, plus totals by zone. Code verified October 10, 2026. It takes one call to get_shot_map, 10 credits. The c…

## What’s new and why it matters
Every located shot a club took in a season, with player, outcome, body part, expected goals and pitch coordinates, plus totals by zone. Code verified October 10, 2026. It takes one call to get_shot_map, 10 credits. The call team takes an abbreviation, a name or an id from list_teams. Season 2025 is 2025-26. Pass against: true to see the shots a club conceded. import requests import pandas as pd API_KEY = " YOUR_API_KEY " resp = requests . post ( " https://mcp.strikerapi.com/v1/get_shot_map " , headers = { " x-api-key " : API_KEY }, json = { " team " : " ARS " , " season " : 2025 , }, timeout =…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/noahowsh/how-do-i-make-a-premier-league-xg-shot-map-in-python-pen

## Related notes
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]
- [[2026-09-26-python-pandas-dataframe-a-beginners-guide]]
- [[2026-09-10-openai-compatible-is-a-spectrum-not-a-boolean-heres-an-11-check-conformance-suite]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
