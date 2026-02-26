---
title: Your Chatbot Recommends Products You Don't Sell
date: '2026-02-26'
source: https://dev.to/rosen_hristov/your-chatbot-recommends-products-you-dont-sell-3jnl
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]'
- '[[2026-02-22-python-geospatial-analysis-5-practical-techniques-to-master-location-data-today]]'
- '[[2026-02-23-why-your-ai-agent-forgets-everything-and-how-to-fix-it]]'
- '[[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
status: unread
---

> **TL;DR:** I was testing my product agent on a demo store that sells electronics. I typed "do you have leather jackets?" The agent searched, got zero results, and instead of admitting the store doesn't carry jackets, it generated p…

## What’s new and why it matters
I was testing my product agent on a demo store that sells electronics. I typed "do you have leather jackets?" The agent searched, got zero results, and instead of admitting the store doesn't carry jackets, it generated product recommendations from its training data. Product names, prices, descriptions that weren't in the store. This is what happens when a ReAct agent with a search tool has no concept of what the store actually sells. It searches, gets nothing useful, and fills the gap with whatever the LLM thinks a helpful response should contain. I tried prompt engineering first. "Only recomm…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rosen_hristov/your-chatbot-recommends-products-you-dont-sell-3jnl

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]
- [[2026-02-22-python-geospatial-analysis-5-practical-techniques-to-master-location-data-today]]
- [[2026-02-23-why-your-ai-agent-forgets-everything-and-how-to-fix-it]]
- [[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
