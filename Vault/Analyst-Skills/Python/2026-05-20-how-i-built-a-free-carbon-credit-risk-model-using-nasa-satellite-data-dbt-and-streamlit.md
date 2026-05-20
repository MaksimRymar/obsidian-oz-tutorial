---
title: How I built a free carbon credit risk model using NASA satellite data, dbt,
  and Streamlit
date: '2026-05-20'
source: https://dev.to/likithasree_yarabarla/how-i-built-a-free-carbon-credit-risk-model-using-nasa-satellite-data-dbt-and-streamlit-4ap6
domain: Python
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-28-how-to-test-python-315-code-with-pytest-80-and-coverage-74]]'
- '[[2026-05-09-i-built-a-python-dashboard-to-monitor-my-cement-plant-in-real-time]]'
- '[[2026-04-26-ship-your-python-project-in-minutes-for-free-with-streamlit]]'
- '[[2026-04-16-what-i-learned-building-an-mcp-server-for-a-130k-node-knowledge-graph]]'
- '[[2026-04-09-i-built-a-70k-security-bounty-pipeline-with-ai-heres-the-exact-workflow]]'
- '[[2026-05-19-i-built-an-open-source-llm-eval-framework-as-a-bca-student-hallucination-detection-red-teaming-regression-tracking]]'
status: unread
---

> **TL;DR:** I spent 3 weeks building an open-source pipeline that scores permanence risk for every blue carbon project on Verra registry. Here's the stack: → NASA FIRMS API — live satellite fire alerts → World Bank API — 9 years of…

## What’s new and why it matters
I spent 3 weeks building an open-source pipeline that scores permanence risk for every blue carbon project on Verra registry. Here's the stack: → NASA FIRMS API — live satellite fire alerts → World Bank API — 9 years of deforestation data → dbt + DuckDB — data modeling and testing → Streamlit — deployed dashboard → GitHub Actions — CI on every push The tricky parts: NASA FIRMS uses MAP_KEY not bearer token World Bank WGI indicators changed endpoint Merging Verra IDs (numeric) with Berkeley IDs (VCS1234 format) required string parsing Live dashboard: ( https://likitha-blue-carbon.streamlit.app/…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/likithasree_yarabarla/how-i-built-a-free-carbon-credit-risk-model-using-nasa-satellite-data-dbt-and-streamlit-4ap6

## Related notes
- [[2026-04-28-how-to-test-python-315-code-with-pytest-80-and-coverage-74]]
- [[2026-05-09-i-built-a-python-dashboard-to-monitor-my-cement-plant-in-real-time]]
- [[2026-04-26-ship-your-python-project-in-minutes-for-free-with-streamlit]]
- [[2026-04-16-what-i-learned-building-an-mcp-server-for-a-130k-node-knowledge-graph]]
- [[2026-04-09-i-built-a-70k-security-bounty-pipeline-with-ai-heres-the-exact-workflow]]
- [[2026-05-19-i-built-an-open-source-llm-eval-framework-as-a-bca-student-hallucination-detection-red-teaming-regression-tracking]]
