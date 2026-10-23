---
title: Add persistent memory to a LlamaIndex agent (Memory, memory blocks and a retriever)
date: '2026-10-23'
source: https://dev.to/memorysync_rafay/add-persistent-memory-to-a-llamaindex-agent-memory-memory-blocks-and-a-retriever-5h8m
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-20-how-to-add-long-term-memory-to-a-python-ai-agent-store-recall-forget-per-user]]'
- '[[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-15-give-your-chatbot-a-memory-in-google-colab-before-your-next-ai-interview]]'
- '[[2026-09-17-project-memory-is-not-chat-history-a-tiny-handoff-layer-for-ai-agents]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** Disclosure: I'm Mohammed, founder of MemorySync. I drafted this article with AI assistance and reviewed it for accuracy against the official MemorySync and LlamaIndex docs. The code is adapted from the docs and I haven't…

## What’s new and why it matters
Disclosure: I'm Mohammed, founder of MemorySync. I drafted this article with AI assistance and reviewed it for accuracy against the official MemorySync and LlamaIndex docs. The code is adapted from the docs and I haven't run it. LlamaIndex agents already have memory. Pass a Memory object to agent.run(..., memory=memory) and the agent gets a short-term chat buffer plus optional long-term "memory blocks". Two things surprise people when they try to make it remember a user across sessions: By default the Memory class uses an in-memory SQLite database, so the buffer is gone when the process restar…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/memorysync_rafay/add-persistent-memory-to-a-llamaindex-agent-memory-memory-blocks-and-a-retriever-5h8m

## Related notes
- [[2026-10-20-how-to-add-long-term-memory-to-a-python-ai-agent-store-recall-forget-per-user]]
- [[2026-06-09-why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-15-give-your-chatbot-a-memory-in-google-colab-before-your-next-ai-interview]]
- [[2026-09-17-project-memory-is-not-chat-history-a-tiny-handoff-layer-for-ai-agents]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
