---
title: How I Built a 4-Bot Telegram AI Engine (<1.6GB OCI ARM64) with Redis Lua USD
  Budget Locks & Gemini Flash-Lite
date: '2026-11-27'
source: https://dev.to/akuma_vencent_d5795f5572f/how-i-built-a-4-bot-telegram-ai-engine-16gb-oci-arm64-with-redis-lua-usd-budget-locks-gemini-7j3
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-08-15-build-a-token-ledger-before-you-burn-through-a-free-model-tier]]'
- '[[2026-05-15-5-crypto-security-signals-in-one-api-call-wallet-risk-token-honeypots-sim-swap-and-more]]'
- '[[2026-03-08-build-a-real-time-news-aggregator-with-python-rss-and-telegram-in-under-100-lines]]'
status: unread
---

> **TL;DR:** If you build production Telegram bots powered by modern LLMs, you hit two brutal walls almost immediately: Runaway token bills — one free-tier user spamming a 50-page PDF, a cache-miss stampede on a hot token address, or…

## What’s new and why it matters
If you build production Telegram bots powered by modern LLMs, you hit two brutal walls almost immediately: Runaway token bills — one free-tier user spamming a 50-page PDF, a cache-miss stampede on a hot token address, or a cron job repeatedly triaging rejected feed items can quietly burn through $50–$200/month. Infrastructure sprawl — spinning up a separate server, database, and worker per bot turns side projects into an expensive ops nightmare. Over the last few weeks, I built and deployed a 4-bot Telegram AI production matrix running on a single Oracle Cloud ARM64 box — with the core 5-conta…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/akuma_vencent_d5795f5572f/how-i-built-a-4-bot-telegram-ai-engine-16gb-oci-arm64-with-redis-lua-usd-budget-locks-gemini-7j3

## Related notes
- [[2026-10-08-my-ai-agent-script-almost-burned-through-a-25-budget-in-one-afternoon-heres-the-10-line-python-fix]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-08-15-build-a-token-ledger-before-you-burn-through-a-free-model-tier]]
- [[2026-05-15-5-crypto-security-signals-in-one-api-call-wallet-risk-token-honeypots-sim-swap-and-more]]
- [[2026-03-08-build-a-real-time-news-aggregator-with-python-rss-and-telegram-in-under-100-lines]]
