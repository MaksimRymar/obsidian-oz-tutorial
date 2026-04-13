---
title: 'The Dory Agent: LangGraph''s Typed State Graph vs. AutoGen''s Event-Driven
  Memory Collapse for Your Fast.ai ML Stack'
date: '2026-04-13'
source: https://dev.to/kowshik_jallipalli_a7e0a5/the-dory-agent-langgraphs-typed-state-graph-vs-autogens-event-driven-memory-collapse-for-your-3bkm
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-29-built-an-open-source-reliability-layer-for-ai-agents-three-tools-all-live-zero-infrastructure-cost]]'
status: unread
---

> **TL;DR:** We've all built it. An AutoGen multi-agent pipeline that works beautifully in your Jupyter notebook, survives three demo runs, and then silently forgets it was halfway through a training evaluation loop the moment a netw…

## What’s new and why it matters
We've all built it. An AutoGen multi-agent pipeline that works beautifully in your Jupyter notebook, survives three demo runs, and then silently forgets it was halfway through a training evaluation loop the moment a network blip interrupts the event bus. The agents keep firing. The conversation history keeps growing. The state? Gone. And no one catches it for forty-seven inference calls. That's not a bug in your code. That's the architectural philosophy made concrete. AutoGen treats agent interaction as conversation. LangGraph treats it as a typed state machine. These are not interchangeable o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kowshik_jallipalli_a7e0a5/the-dory-agent-langgraphs-typed-state-graph-vs-autogens-event-driven-memory-collapse-for-your-3bkm

## Related notes
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-29-built-an-open-source-reliability-layer-for-ai-agents-three-tools-all-live-zero-infrastructure-cost]]
