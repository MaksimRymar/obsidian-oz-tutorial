---
title: Pydantic AI keeps one growing message list per run — and re-sends the whole
  thing every step
date: '2026-08-22'
source: https://dev.to/wartzarbee/pydantic-ai-keeps-one-growing-message-list-per-run-and-re-sends-the-whole-thing-every-step-4o7b
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]'
- '[[2026-05-08-i-built-an-ai-agent-that-does-osint-investigations-from-your-terminal]]'
- '[[2026-07-30-langchain-for-absolute-beginners---part-6-debugging-observing-agents-with-langsmith]]'
- '[[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]'
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
status: unread
---

> **TL;DR:** Pydantic AI gives you a clean, typed agent: define an Agent , hand it tools, call agent.run(...) , and it loops — model call, tool call, model call — until it produces a validated result. The typed ergonomics are great.…

## What’s new and why it matters
Pydantic AI gives you a clean, typed agent: define an Agent , hand it tools, call agent.run(...) , and it loops — model call, tool call, model call — until it produces a validated result. The typed ergonomics are great. What the quickstart doesn't spell out is what the model receives on each pass of that loop. I read the run graph ( pydantic_ai_slim/pydantic_ai/_agent_graph.py on main ) to find out. The mechanism is structural, and it's the same shape I found in the OpenAI Agents SDK and smolagents. One list, appended twice per turn Each run holds a single mutable conversation list on its stat…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wartzarbee/pydantic-ai-keeps-one-growing-message-list-per-run-and-re-sends-the-whole-thing-every-step-4o7b

## Related notes
- [[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]
- [[2026-05-08-i-built-an-ai-agent-that-does-osint-investigations-from-your-terminal]]
- [[2026-07-30-langchain-for-absolute-beginners---part-6-debugging-observing-agents-with-langsmith]]
- [[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
