---
title: I turned a Claude Code-only web reader into a normal MCP server
date: '2026-07-07'
source: https://dev.to/flyingsquirrel0419/i-turned-a-claude-code-only-web-reader-into-a-normal-mcp-server-2i9l
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]'
- '[[2026-06-23-how-one-abstraction-tamed-ai-integration-chaos]]'
- '[[2026-03-07-web2api-turning-websites-into-rest-apis-and-mcp-tools]]'
- '[[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
status: unread
---

> **TL;DR:** I kept running into the same problem while building with agents: The page is public. A browser can read it. But my agent gets blocked, redirected, rate-limited, or handed a shell of HTML with no useful content. There was…

## What’s new and why it matters
I kept running into the same problem while building with agents: The page is public. A browser can read it. But my agent gets blocked, redirected, rate-limited, or handed a shell of HTML with no useful content. There was already a fun project in this space: insane-search . It is clever, aggressive, and useful, but the original workflow is centered around Claude Code. I wanted the same kind of public-web resilience as a regular MCP server, so any MCP-compatible client could call it. That became unlimited-search . flyingsquirrel0419 / unlimited-search MCP server and CLI for reading public web pa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/flyingsquirrel0419/i-turned-a-claude-code-only-web-reader-into-a-normal-mcp-server-2i9l

## Related notes
- [[2026-04-02-how-to-turn-any-webpage-into-structured-data-for-your-llm]]
- [[2026-06-23-how-one-abstraction-tamed-ai-integration-chaos]]
- [[2026-03-07-web2api-turning-websites-into-rest-apis-and-mcp-tools]]
- [[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
