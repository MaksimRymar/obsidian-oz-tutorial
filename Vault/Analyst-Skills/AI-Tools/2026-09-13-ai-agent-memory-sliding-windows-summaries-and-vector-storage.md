---
title: 'AI Agent Memory: Sliding Windows, Summaries, and Vector Storage'
date: '2026-09-13'
source: https://dev.to/gokulnathp/ai-agent-memory-sliding-windows-summaries-and-vector-storage-4mo9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#presentations'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]'
- '[[2026-03-15-why-ai-agents-forget-everything-and-how-we-fixed-it]]'
- '[[2026-04-05-ai-memory-is-broken-we-built-one-that-forgets]]'
- '[[2026-04-23-ai-agent-memory-in-2026-mem0-vs-zep-vs-letta-vs-cognee-a-practical-guide]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
status: unread
---

> **TL;DR:** The agent we built in Post #4 has one big problem — the moment the script ends, it forgets everything. Next time you run it, it starts from zero. No memory of past conversations, no retained facts, nothing. For a quick e…

## What’s new and why it matters
The agent we built in Post #4 has one big problem — the moment the script ends, it forgets everything. Next time you run it, it starts from zero. No memory of past conversations, no retained facts, nothing. For a quick experiment that's fine. For anything you'd actually use, it's a dealbreaker. Memory is what makes an assistant feel like it knows you over time. Three kinds of memory There are three different ways to give an agent memory, and they serve different purposes. Short-term memory is what we've been using all along — the messages list. It's fast and immediate, but it only lasts for th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gokulnathp/ai-agent-memory-sliding-windows-summaries-and-vector-storage-4mo9

## Related notes
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-02-22-give-your-ai-agent-long-term-memory-with-sqlite-and-ollama]]
- [[2026-03-15-why-ai-agents-forget-everything-and-how-we-fixed-it]]
- [[2026-04-05-ai-memory-is-broken-we-built-one-that-forgets]]
- [[2026-04-23-ai-agent-memory-in-2026-mem0-vs-zep-vs-letta-vs-cognee-a-practical-guide]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
