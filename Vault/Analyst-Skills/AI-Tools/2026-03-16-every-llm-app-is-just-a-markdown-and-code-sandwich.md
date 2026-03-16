---
title: Every LLM App Is Just a Markdown-and-Code Sandwich
date: '2026-03-16'
source: https://dev.to/shimo4228/every-llm-app-is-just-a-markdown-and-code-sandwich-213j
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
status: unread
---

> **TL;DR:** I reimplemented the insight feature of my custom agent using a local 9B model, and the exact same structure that powers Claude Code emerged. An LLM agent's behavior can be defined by natural language instructions written…

## What’s new and why it matters
I reimplemented the insight feature of my custom agent using a local 9B model, and the exact same structure that powers Claude Code emerged. An LLM agent's behavior can be defined by natural language instructions written in Markdown files. Code is just the skeleton that parses the LLM's output and executes it safely. — I wrote that in the previous article while building an agent on Qwen 9B. What I hadn't realized was that the same principle applies to Claude Code, unchanged . This article traces what became visible during the process of reverting a broken implementation and redesigning from sc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/shimo4228/every-llm-app-is-just-a-markdown-and-code-sandwich-213j

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
