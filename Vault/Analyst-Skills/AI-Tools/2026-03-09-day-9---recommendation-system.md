---
title: DAY 9 - Recommendation System
date: '2026-03-09'
source: https://dev.to/nexoperose/day-9-recommendation-system-4md7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-07-day-7---mlflow-tracking]]'
- '[[2026-03-08-day-8---batch-inference-pipeline]]'
- '[[2026-03-05-i-built-a-self-hosted-llm-observability-tool-for-ai-applications-logmera]]'
- '[[2026-03-07-28-tool-definitions-cutting-ai-agent-costs-with-sub-agent-splitting]]'
- '[[2026-03-06-stop-the-sugar-spikes-build-a-real-time-ai-glucose-coach-with-langgraph-cgm]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
status: unread
---

> **TL;DR:** Day 9 of Phase 2: AI System Building focused on implementing a collaborative filtering Recommendation System using ALS. User interactions were mapped into rating values (purchase = 3, cart = 2, view = 1) to simulate impl…

## What’s new and why it matters
Day 9 of Phase 2: AI System Building focused on implementing a collaborative filtering Recommendation System using ALS. User interactions were mapped into rating values (purchase = 3, cart = 2, view = 1) to simulate implicit feedback strength. An ALS model was trained on a controlled subset of users to prevent memory overflow in a shared/serverless environment. Initial attempts using StringIndexer caused model size overflow due to high cardinality. Numeric casting of user and product IDs resolved this issue. Training on the full dataset resulted in heap memory errors, so user sampling and prod…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nexoperose/day-9-recommendation-system-4md7

## Related notes
- [[2026-03-07-day-7---mlflow-tracking]]
- [[2026-03-08-day-8---batch-inference-pipeline]]
- [[2026-03-05-i-built-a-self-hosted-llm-observability-tool-for-ai-applications-logmera]]
- [[2026-03-07-28-tool-definitions-cutting-ai-agent-costs-with-sub-agent-splitting]]
- [[2026-03-06-stop-the-sugar-spikes-build-a-real-time-ai-glucose-coach-with-langgraph-cgm]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
