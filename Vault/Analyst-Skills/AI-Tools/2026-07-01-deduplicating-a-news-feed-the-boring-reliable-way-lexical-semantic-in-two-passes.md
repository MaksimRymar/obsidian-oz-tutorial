---
title: 'Deduplicating a news feed the boring, reliable way: lexical + semantic in
  two passes'
date: '2026-07-01'
source: https://dev.to/aicode_32cae40a1e284567b8/deduplicating-a-news-feed-the-boring-reliable-way-lexical-semantic-in-two-passes-49fn
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]'
- '[[2026-05-08-your-first-automated-python-script-that-validates-and-runs-itself]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-20-building-a-production-rag-pipeline-architecture-decisions-that-matter]]'
status: unread
---

> **TL;DR:** If you build anything that ingests news — an aggregator, a newsletter automation, a Telegram channel pipeline — you hit the same wall fast: the same story shows up five times, worded differently every time. Reuters, a lo…

## What’s new and why it matters
If you build anything that ingests news — an aggregator, a newsletter automation, a Telegram channel pipeline — you hit the same wall fast: the same story shows up five times, worded differently every time. Reuters, a local outlet, two blogs, and an official press release all describe one event. Your feed doesn't need five posts about it. It needs one. The naive fix is to hash the headline or the URL and skip repeats. That fails immediately, because near-duplicates are the whole problem. "Central bank holds rate at 16%" and "Regulator keeps key rate unchanged at 16 percent" are the same story…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aicode_32cae40a1e284567b8/deduplicating-a-news-feed-the-boring-reliable-way-lexical-semantic-in-two-passes-49fn

## Related notes
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-04-11-7-free-defi-apis-every-developer-should-know-in-2026-with-code-examples]]
- [[2026-05-08-your-first-automated-python-script-that-validates-and-runs-itself]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-20-building-a-production-rag-pipeline-architecture-decisions-that-matter]]
