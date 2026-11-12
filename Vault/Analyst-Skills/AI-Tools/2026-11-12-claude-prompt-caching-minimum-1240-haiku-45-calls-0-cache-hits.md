---
title: 'Claude Prompt Caching Minimum: 1,240 Haiku 4.5 Calls, 0 Cache Hits'
date: '2026-11-12'
source: https://dev.to/ji_ai/claude-prompt-caching-minimum-1240-haiku-45-calls-0-cache-hits-9ph
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
status: unread
---

> **TL;DR:** I moved a scoring job from Sonnet 4.5 to Haiku 4.5 to cut its cost by two thirds. A week later the bill had dropped, but nowhere near as much as my spreadsheet promised. The cause was sitting in every response I'd logged…

## What’s new and why it matters
I moved a scoring job from Sonnet 4.5 to Haiku 4.5 to cut its cost by two thirds. A week later the bill had dropped, but nowhere near as much as my spreadsheet promised. The cause was sitting in every response I'd logged: cache_read_input_tokens: 0 . All 1,240 calls. No error. No warning. The cache_control marker was still on the system prompt. I had hit the Claude prompt caching minimum: Haiku 4.5 won't cache a prefix shorter than 4,096 tokens, and mine was 3,180. TL;DR Claude prompt caching has a minimum cacheable prefix length that depends on the model . Below it, cache_control is silently…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ji_ai/claude-prompt-caching-minimum-1240-haiku-45-calls-0-cache-hits-9ph

## Related notes
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
