---
title: My Comment-Reply Bot Hit a Wall the Docs Never Mentioned. That Wall Turned
  Out to Be a Security Feature.
date: '2026-07-19'
source: https://dev.to/enjoy_kumawat/my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-bjm
domain: Productivity
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#productivity'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]'
- '[[2026-02-24-week-12-i-built-my-own-payment-rails-in-an-afternoon]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]'
status: unread
---

> **TL;DR:** I run a small MCP server ( server.py in this repo) that already talks to the DEV.to API to publish articles — create_article POSTs to /api/articles with my key, works every time. So when I found, almost by accident, that…

## What’s new and why it matters
I run a small MCP server ( server.py in this repo) that already talks to the DEV.to API to publish articles — create_article POSTs to /api/articles with my key, works every time. So when I found, almost by accident, that 35 published articles had accumulated 20 unanswered comments (some six weeks old), the obvious next step looked like the same pattern: write a script, POST to some comments endpoint, done. I'd already automated writes to this API. Replying is just another write. It isn't. And the way I found out told me more about how DEV.to's API is actually designed than any docs page did. T…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/enjoy_kumawat/my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-bjm

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-02-28-ai-data-analysis-tools-i-actually-use-daily]]
- [[2026-02-24-week-12-i-built-my-own-payment-rails-in-an-afternoon]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]
