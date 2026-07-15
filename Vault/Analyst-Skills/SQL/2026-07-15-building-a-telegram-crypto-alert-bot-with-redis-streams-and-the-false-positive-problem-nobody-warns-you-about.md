---
title: Building a Telegram crypto-alert bot with Redis Streams — and the false-positive
  problem nobody warns you about
date: '2026-07-15'
source: https://dev.to/serhiibogomaz/building-a-telegram-crypto-alert-bot-with-redis-streams-and-the-false-positive-problem-nobody-ane
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]'
- '[[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]'
- '[[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-wins-in-2026]]'
status: unread
---

> **TL;DR:** I've been building a side project for the last few months — a Telegram bot that watches crypto prices and pings you when something you care about happens (price crosses a threshold, a coin hits a new ATH, volume spikes,…

## What’s new and why it matters
I've been building a side project for the last few months — a Telegram bot that watches crypto prices and pings you when something you care about happens (price crosses a threshold, a coin hits a new ATH, volume spikes, whatever). Nothing groundbreaking on the surface, but getting it reliable turned into a much more interesting engineering problem than I expected. Wanted to write up the parts that actually taught me something. Stack: Python 3.12, aiogram 3 for the bot layer, PostgreSQL for storage, Redis for everything hot-path, Docker for deployment. The pipeline Market data comes in from Coi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/serhiibogomaz/building-a-telegram-crypto-alert-bot-with-redis-streams-and-the-false-positive-problem-nobody-ane

## Related notes
- [[2026-07-01-one-big-table-vs-the-star-schema-i-think-everyones-arguing-about-the-wrong-thing]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-21-i-spent-6-months-obsessing-over-mt5-bot-logic-heres-what-finally-clicked]]
- [[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]
- [[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-wins-in-2026]]
