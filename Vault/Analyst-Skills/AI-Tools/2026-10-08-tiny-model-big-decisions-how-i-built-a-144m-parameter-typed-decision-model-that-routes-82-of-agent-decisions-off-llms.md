---
title: Tiny model. Big decisions. — How I built a 144M-parameter typed decision model
  that routes 82% of agent decisions off LLMs
date: '2026-10-08'
source: https://dev.to/perrylink/tiny-model-big-decisions-how-i-built-a-144m-parameter-typed-decision-model-that-routes-82-of-23fi
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-21-jev-system-one-models-fast-decision-making-for-ai-agents]]'
- '[[2026-03-28-how-to-add-reputation-scoring-to-your-langchain-agent-in-5-lines]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-09-27-i-built-a-registry-for-system-one-models-heres-what-i-learned-comparing-all-of-them]]'
- '[[2026-04-14-build-your-own-second-brain-rag-powered-knowledge-tools-that-never-leave-your-machine]]'
- '[[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]'
status: unread
---

> **TL;DR:** Tiny model. Big decisions. — How I built a 144M-parameter typed decision model that routes 82% of agent decisions off LLMs Or: why your agent's "should I run this command?" does not need a 70B chat model. Every agentic w…

## What’s new and why it matters
Tiny model. Big decisions. — How I built a 144M-parameter typed decision model that routes 82% of agent decisions off LLMs Or: why your agent's "should I run this command?" does not need a 70B chat model. Every agentic workflow I build hits the same wall: the interesting logic is 10 lines, and the other 90% is a language model deciding "allow or deny?", "which tool?", "pass or escalate?" — thousands of times a day, at chat-model prices and chat-model latency. So I built the opposite of a chatbot: Phocinae-Largha-150M-v1 , a 144.3M-parameter typed decision model. It cannot generate text. It tak…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/perrylink/tiny-model-big-decisions-how-i-built-a-144m-parameter-typed-decision-model-that-routes-82-of-23fi

## Related notes
- [[2026-09-21-jev-system-one-models-fast-decision-making-for-ai-agents]]
- [[2026-03-28-how-to-add-reputation-scoring-to-your-langchain-agent-in-5-lines]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-09-27-i-built-a-registry-for-system-one-models-heres-what-i-learned-comparing-all-of-them]]
- [[2026-04-14-build-your-own-second-brain-rag-powered-knowledge-tools-that-never-leave-your-machine]]
- [[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]
