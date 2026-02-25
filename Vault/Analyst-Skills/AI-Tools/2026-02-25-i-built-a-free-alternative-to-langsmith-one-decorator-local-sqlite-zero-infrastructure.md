---
title: I built a free alternative to LangSmith — one decorator, local SQLite, zero
  infrastructure
date: '2026-02-25'
source: https://dev.to/jarradbermingham/i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure-2ink
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]'
- '[[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]'
- '[[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-02-22-agent-memory-a-zero-dependency-memory-system-for-ai-agents]]'
status: unread
---

> **TL;DR:** LangSmith wants $400/month. Helicone needs you to proxy your AI traffic through their servers. Both require accounts, API keys, and sending your data to someone else's cloud. I just wanted to know what my AI agents were…

## What’s new and why it matters
LangSmith wants $400/month. Helicone needs you to proxy your AI traffic through their servers. Both require accounts, API keys, and sending your data to someone else's cloud. I just wanted to know what my AI agents were costing me. So I built bifrost-monitor — a Python decorator that tracks every AI call locally. No accounts. No infrastructure. No data leaving your machine. Here's the full setup: from bifrost_monitor import monitor @monitor ( name = " support-agent " , model = " claude-sonnet-4-6 " ) async def handle_ticket ( ticket ): response = await client . messages . create (...) return r…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jarradbermingham/i-built-a-free-alternative-to-langsmith-one-decorator-local-sqlite-zero-infrastructure-2ink

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-02-23-my-aws-lambda-runs-faster-than-yours-heres-how-to-optimize-lambda-cold-starts-with-snapstart]]
- [[2026-02-22-i-built-an-ai-system-that-generates-trading-signals-across-4-stock-markets-heres-how]]
- [[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-02-22-agent-memory-a-zero-dependency-memory-system-for-ai-agents]]
