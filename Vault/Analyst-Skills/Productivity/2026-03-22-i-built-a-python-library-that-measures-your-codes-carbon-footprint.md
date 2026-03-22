---
title: I Built a Python Library That Measures Your Code's Carbon Footprint
date: '2026-03-22'
source: https://dev.to/zwony/i-built-a-python-library-that-measures-your-codes-carbon-footprint-4b91
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-03-04-predict-house-prices-with-python-a-beginners-machine-learning-guide]]'
- '[[2026-03-15-i-built-the-first-open-source-fp8-linear-solver-in-python-2-3x-faster-than-cublas]]'
- '[[2026-02-22-python-geospatial-analysis-5-practical-techniques-to-master-location-data-today]]'
- '[[2026-03-22-day-1-of-my-90-days-ai-journey-setting-up-the-perfect-environment]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]'
status: unread
---

> **TL;DR:** The Problem My machine learning scripts run for hours. One day I got curious — how much CO₂ am I actually emitting while training models? I searched for a simple Python library to measure this. Nothing fit. So I built on…

## What’s new and why it matters
The Problem My machine learning scripts run for hours. One day I got curious — how much CO₂ am I actually emitting while training models? I searched for a simple Python library to measure this. Nothing fit. So I built one. Introducing EcoTrace EcoTrace is a lightweight Python library that measures the carbon footprint of your functions using real-time CPU and GPU utilization sampling. pip install ecotrace How It Works from ecotrace import EcoTrace eco = EcoTrace ( region_code = " US " ) @eco.track def train_model (): return sum ( i * i for i in range ( 10 ** 6 )) train_model () # [EcoTrace] Fu…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zwony/i-built-a-python-library-that-measures-your-codes-carbon-footprint-4b91

## Related notes
- [[2026-03-04-predict-house-prices-with-python-a-beginners-machine-learning-guide]]
- [[2026-03-15-i-built-the-first-open-source-fp8-linear-solver-in-python-2-3x-faster-than-cublas]]
- [[2026-02-22-python-geospatial-analysis-5-practical-techniques-to-master-location-data-today]]
- [[2026-03-22-day-1-of-my-90-days-ai-journey-setting-up-the-perfect-environment]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]
