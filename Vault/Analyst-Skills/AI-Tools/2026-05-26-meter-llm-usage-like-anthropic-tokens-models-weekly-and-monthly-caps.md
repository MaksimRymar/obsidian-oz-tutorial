---
title: Meter LLM usage like Anthropic — tokens, models, weekly and monthly caps
date: '2026-05-26'
source: https://dev.to/0x180db/meter-llm-usage-like-anthropic-tokens-models-weekly-and-monthly-caps-4302
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
- '[[2026-04-19-stop-collapsing-your-data-why-window-functions-are-a-game-changer]]'
status: unread
---

> **TL;DR:** Anthropic and OpenAI count what every customer uses down to the token, broken out by model and token type, and turn those counts into daily, weekly, and monthly caps without adding inference latency. If you're building o…

## What’s new and why it matters
Anthropic and OpenAI count what every customer uses down to the token, broken out by model and token type, and turn those counts into daily, weekly, and monthly caps without adding inference latency. If you're building on top of their APIs, you end up solving the same problem on your side. If you're building something like them, you solve it for everyone at once. Here's one way to do it in Python, using Unimeter (an open-source metering engine) and a working example. Every snippet below comes from runnable code in unimeter/llm-token-metering ; the file paths in the snippets match the paths in…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/0x180db/meter-llm-usage-like-anthropic-tokens-models-weekly-and-monthly-caps-4302

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
- [[2026-04-19-stop-collapsing-your-data-why-window-functions-are-a-game-changer]]
