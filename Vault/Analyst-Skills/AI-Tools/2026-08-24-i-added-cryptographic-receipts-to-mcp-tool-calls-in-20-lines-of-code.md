---
title: I Added Cryptographic Receipts to MCP Tool Calls in 20 Lines of Code
date: '2026-08-24'
source: https://dev.to/correctover/i-added-cryptographic-receipts-to-mcp-tool-calls-in-20-lines-of-code-4h7o
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-06-12-why-your-ai-agent-logs-are-not-evidence-and-what-to-do-about-it]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
status: unread
---

> **TL;DR:** If you've built an MCP server, you know the drill: define a tool, write a handler, return a result. The SDK handles the protocol, the transport, the schema validation. It feels clean. It also means you have zero verifiab…

## What’s new and why it matters
If you've built an MCP server, you know the drill: define a tool, write a handler, return a result. The SDK handles the protocol, the transport, the schema validation. It feels clean. It also means you have zero verifiable evidence that what your handler returned is what the agent actually received — or that the arguments the agent passed are what your handler expected. I'm not here to scare you with supply chain horror stories. I want to show you a technique I've been using: attaching a cryptographically signed receipt to every MCP tool call. It catches argument tampering, response mutation,…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/correctover/i-added-cryptographic-receipts-to-mcp-tool-calls-in-20-lines-of-code-4h7o

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-06-12-why-your-ai-agent-logs-are-not-evidence-and-what-to-do-about-it]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
