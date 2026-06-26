---
title: '# I built a tool that found my LangGraph email agent could be hijacked to
  forward the entire inbox to an attacker'
date: '2026-06-26'
source: https://dev.to/jaleedahmad/-i-built-a-tool-that-found-my-langgraph-email-agent-could-be-hijacked-to-forward-the-entire-inbox-3ik7
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-04-agentic-ci-how-i-test-ai-workers-like-services-securely]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]'
- '[[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]'
- '[[2026-04-30-how-attackers-hijack-llm-agents-and-how-to-stop-them]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** TL;DR: I discovered that standard LLM email agents with tool access are highly vulnerable to indirect prompt injection. I built AgentBreak , an open-source workflow security scanner, to map out these attack paths and tes…

## What’s new and why it matters
TL;DR: I discovered that standard LLM email agents with tool access are highly vulnerable to indirect prompt injection. I built AgentBreak , an open-source workflow security scanner, to map out these attack paths and test them before they hit production. Here is how the exploit works and how to catch it. The setup Imagine a realistic email assistant agent built to help manage your inbox. It has six tools: fetch_emails (an EXTERNAL source that pulls unread emails via IMAP), web_search (an EXTERNAL source that scrapes the web for context), summarise_and_plan (an LLM node that decides what to do)…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/jaleedahmad/-i-built-a-tool-that-found-my-langgraph-email-agent-could-be-hijacked-to-forward-the-entire-inbox-3ik7

## Related notes
- [[2026-03-04-agentic-ci-how-i-test-ai-workers-like-services-securely]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-10-building-a-production-ready-agentic-ai-system-with-langgraph-and-mcp]]
- [[2026-05-03-i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made]]
- [[2026-04-30-how-attackers-hijack-llm-agents-and-how-to-stop-them]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
