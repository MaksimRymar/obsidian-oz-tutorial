---
title: What's new in Data Preprocessor 1.5.x — R codegen, Robust Scaler, and a deadlock
  post-mortem
date: '2026-05-25'
source: https://dev.to/keenchris/whats-new-in-data-preprocessor-15x-r-codegen-robust-scaler-and-a-deadlock-post-mortem-kb9
domain: Python
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-06-pydantic-ai-tutorial-how-i-build-type-safe-ai-agents-that-actually-work-in-production]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-20-i-tracked-every-llm-api-call-for-a-week-65-were-unnecessary]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]'
- '[[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]'
status: unread
---

> **TL;DR:** It's been a few months since I last wrote about Data Preprocessor, the IntelliJ plugin I built to stop re-writing the same pandas preprocessing scripts every project. The 1.5.x series has landed a real R codegen path, a…

## What’s new and why it matters
It's been a few months since I last wrote about Data Preprocessor, the IntelliJ plugin I built to stop re-writing the same pandas preprocessing scripts every project. The 1.5.x series has landed a real R codegen path, a more honest outlier-resistant normalizer, and one genuinely embarrassing deadlock that I want to talk about openly because the lesson is useful. tl;dr on what the plugin does You load a CSV, Excel, or JSON file inside your JetBrains IDE. The plugin profiles every column (type, null count, mean/median/std, mode, unique count). You build a pipeline visually — drop nulls, fill wit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/keenchris/whats-new-in-data-preprocessor-15x-r-codegen-robust-scaler-and-a-deadlock-post-mortem-kb9

## Related notes
- [[2026-04-06-pydantic-ai-tutorial-how-i-build-type-safe-ai-agents-that-actually-work-in-production]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-20-i-tracked-every-llm-api-call-for-a-week-65-were-unnecessary]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-15-why-i-as-someone-who-likes-mysql-now-want-to-recommend-postgresql]]
- [[2026-04-08-how-building-a-streaming-sql-api-in-nodejs-changed-my-approach-to-real-time-data]]
