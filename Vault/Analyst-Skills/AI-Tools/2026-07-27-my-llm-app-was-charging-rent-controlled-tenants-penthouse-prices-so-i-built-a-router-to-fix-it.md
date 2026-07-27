---
title: My LLM App Was Charging Rent-Controlled Tenants Penthouse Prices — So I Built
  a Router to Fix It
date: '2026-07-27'
source: https://dev.to/ayushsinghtomar/my-llm-app-was-charging-rent-controlled-tenants-penthouse-prices-so-i-built-a-router-to-fix-it-38cl
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]'
- '[[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
status: unread
---

> **TL;DR:** Every LLM app I've built has the same expensive habit: one model, every request. "What is FastAPI?" and "compare these five architectures in depth" go to the same endpoint, at the same price. That's fine right up until y…

## What’s new and why it matters
Every LLM app I've built has the same expensive habit: one model, every request. "What is FastAPI?" and "compare these five architectures in depth" go to the same endpoint, at the same price. That's fine right up until you look at the bill — you're paying big-model rates for questions a much smaller model answers just as well. So I built a router that sits in front of two models and decides which one actually earns the request. Live demo: llm-cost-router.streamlit.app Repo: github.com/ayush-s-tomar/llm-cost-router What it does Ask it anything. It classifies the question, then routes it to one…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ayushsinghtomar/my-llm-app-was-charging-rent-controlled-tenants-penthouse-prices-so-i-built-a-router-to-fix-it-38cl

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-07-18-building-my-first-real-database-what-a-weekend-sql-assignment-taught-me-about-postgres-and-git]]
- [[2026-07-24-you-dont-need-a-backend-to-store-form-submissions-you-need-a-place-to-ask-how-many]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
