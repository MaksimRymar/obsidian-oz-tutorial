---
title: I built an independent search engine—and the results were interesting
date: '2026-06-06'
source: https://dev.to/splotdev/i-built-an-independent-search-engine-and-the-results-were-interesting-1a9g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]'
- '[[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]'
- '[[2026-03-12-learning-python-was-a-life-changing-experience]]'
- '[[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-saves-you-money-in-2026]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-04-23-from-0-to-100-github-stars-with-a-python-cli-spoiler-its-not-as-easy-as-they-say]]'
status: unread
---

> **TL;DR:** A few months ago, I came across FrogFind , a retro search engine, and I decided that I wanted to try my hand at making one, too. I first started with the crawler, carefully planning out a simple single threaded Python re…

## What’s new and why it matters
A few months ago, I came across FrogFind , a retro search engine, and I decided that I wanted to try my hand at making one, too. I first started with the crawler, carefully planning out a simple single threaded Python requests bot using SQLite3 that accommodated robots.txt. This was particularly difficult—I had barely any experience in the field of search engine creation, and its subcategories. After the crawler was the webapp, which was relatively easy, because of my experience with Flask. I used Redis for rate limit storage, and various algorithms to do the searching for me. I shoved my craw…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/splotdev/i-built-an-independent-search-engine-and-the-results-were-interesting-1a9g

## Related notes
- [[2026-04-08-i-built-a-bot-that-answers-github-discussions-using-free-ai-models-heres-what-i-learned]]
- [[2026-02-20-how-i-built-an-advanced-sql-tutorial-and-self-hosted-it-on-my-own-nas]]
- [[2026-03-12-learning-python-was-a-life-changing-experience]]
- [[2026-06-02-deepseek-vs-qwen-vs-kimi-vs-glm-which-chinese-ai-model-actually-saves-you-money-in-2026]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-04-23-from-0-to-100-github-stars-with-a-python-cli-spoiler-its-not-as-easy-as-they-say]]
