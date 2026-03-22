---
title: Moving an NPB Prediction System to BigQuery — BQML and Cloud Run on the Free
  Tier
date: '2026-03-22'
source: https://dev.to/yasumorishima/moving-an-npb-prediction-system-to-bigquery-bqml-and-cloud-run-on-the-free-tier-4lb4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]'
- '[[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]'
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-19-solving-use-machine-learning-apis-on-google-cloud-challenge-lab-a-complete-guide]]'
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
status: unread
---

> **TL;DR:** Background I've been running an NPB (Japanese professional baseball) player performance prediction project for over a year. → Previous articles: Why Marcel Beat LightGBM: Building an NPB Player Performance Prediction Sys…

## What’s new and why it matters
Background I've been running an NPB (Japanese professional baseball) player performance prediction project for over a year. → Previous articles: Why Marcel Beat LightGBM: Building an NPB Player Performance Prediction System Annual Auto-Retraining for NPB Baseball Predictions with GitHub Actions The setup was: GitHub Actions fetches data → trains models → saves CSVs → Streamlit displays results. Data lived in CSVs, the API ran on a Raspberry Pi 5 Docker container, and analysis was done in local Python. I added Google BigQuery to centralize the data, run SQL analysis, compare BQML accuracy again…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yasumorishima/moving-an-npb-prediction-system-to-bigquery-bqml-and-cloud-run-on-the-free-tier-4lb4

## Related notes
- [[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]
- [[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-19-solving-use-machine-learning-apis-on-google-cloud-challenge-lab-a-complete-guide]]
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
