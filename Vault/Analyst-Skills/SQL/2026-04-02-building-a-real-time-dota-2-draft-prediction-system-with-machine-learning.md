---
title: Building a Real-Time Dota 2 Draft Prediction System with Machine Learning
date: '2026-04-02'
source: https://dev.to/t9mple_0d32462141e31abf09/building-a-real-time-dota-2-draft-prediction-system-with-machine-learning-4n39
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-03-04-predict-house-prices-with-python-a-beginners-machine-learning-guide]]'
- '[[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]'
- '[[2026-03-06-5-database-design-mistakes-i-keep-seeing-and-how-to-catch-them-early]]'
- '[[2026-03-05-building-an-ai-prediction-api-with-fastapi-lessons-from-an-open-source-project]]'
status: unread
---

> **TL;DR:** I built an AI system that watches live Dota 2 pro matches and predicts which team will win based purely on the draft. Here's how it works under the hood. The Problem Dota 2 has 127 heroes. A Captain's Mode draft produces…

## What’s new and why it matters
I built an AI system that watches live Dota 2 pro matches and predicts which team will win based purely on the draft. Here's how it works under the hood. The Problem Dota 2 has 127 heroes. A Captain's Mode draft produces roughly 10^15 possible combinations. Analysts spend years building intuition about which drafts work — I wanted to see if a model could learn those patterns from data. Architecture Live Match → Draft Detection → Feature Engineering → XGBoost + DraftNet → Prediction + SHAP Explanation The system runs 24/7 on Railway (Python/FastAPI). When a professional draft completes, it dete…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/t9mple_0d32462141e31abf09/building-a-real-time-dota-2-draft-prediction-system-with-machine-learning-4n39

## Related notes
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-03-04-predict-house-prices-with-python-a-beginners-machine-learning-guide]]
- [[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]
- [[2026-03-06-5-database-design-mistakes-i-keep-seeing-and-how-to-catch-them-early]]
- [[2026-03-05-building-an-ai-prediction-api-with-fastapi-lessons-from-an-open-source-project]]
