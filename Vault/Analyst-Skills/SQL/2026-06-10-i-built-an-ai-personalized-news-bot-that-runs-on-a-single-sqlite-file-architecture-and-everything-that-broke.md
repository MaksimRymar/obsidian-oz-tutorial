---
title: I built an AI-personalized news bot that runs on a single SQLite file — architecture
  and everything that broke
date: '2026-06-10'
source: https://dev.to/grigoriyraze/i-built-an-ai-personalized-news-bot-that-runs-on-a-single-sqlite-file-architecture-and-everything-1o5n
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]'
- '[[2026-06-09-how-i-messed-up-ai-streaming-and-how-you-can-avoid-it]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-04-21-what-surprised-me-about-building-a-python-rag-pipeline-with-open-source-llms]]'
status: unread
---

> **TL;DR:** I built an AI-personalized news bot that runs on a single SQLite file — architecture and everything that broke TL;DR — @futur_e_news_bot . A bilingual (EN/RU) Telegram news feed. AI removes duplicates, clusters one event…

## What’s new and why it matters
I built an AI-personalized news bot that runs on a single SQLite file — architecture and everything that broke TL;DR — @futur_e_news_bot . A bilingual (EN/RU) Telegram news feed. AI removes duplicates, clusters one event into one card, translates, and tunes the feed to your reactions. Stack: aiogram, local ONNX embeddings, sqlite-vec instead of pgvector , a chain of free LLMs via OpenRouter, one worker on Fly.io. It started at ~$5/month — and broke in three interesting ways I'll walk through. I wanted a news feed without two things: duplicates (the same event from five outlets with five headli…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/grigoriyraze/i-built-an-ai-personalized-news-bot-that-runs-on-a-single-sqlite-file-architecture-and-everything-1o5n

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]
- [[2026-06-09-how-i-messed-up-ai-streaming-and-how-you-can-avoid-it]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-04-21-what-surprised-me-about-building-a-python-rag-pipeline-with-open-source-llms]]
