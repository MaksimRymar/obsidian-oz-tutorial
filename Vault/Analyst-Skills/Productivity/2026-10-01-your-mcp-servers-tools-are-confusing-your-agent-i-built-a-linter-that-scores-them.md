---
title: Your MCP server's tools are confusing your agent. I built a linter that scores
  them.
date: '2026-10-01'
source: https://dev.to/haoli/your-mcp-servers-tools-are-confusing-your-agent-i-built-a-linter-that-scores-them-4j4d
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-13-your-claude-code-and-cursor-agents-have-amnesia-heres-the-fix]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
status: unread
---

> **TL;DR:** Over on r/mcp, a recurring complaint from people wiring up their first servers goes something like: "I wired up 4–5 MCP servers and I still can't design one from scratch. When is something a tool vs a resource? Why does…

## What’s new and why it matters
Over on r/mcp, a recurring complaint from people wiring up their first servers goes something like: "I wired up 4–5 MCP servers and I still can't design one from scratch. When is something a tool vs a resource? Why does my agent keep calling the wrong thing?" That confusion is almost never a transport problem — it's a design problem. Tools with no description. Names like handle_data . List endpoints that dump everything with no pagination. delete_* tools that never hint at confirmation. Bad tool design wastes context and confuses agents, and nobody was checking for it statically. So I built mc…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/haoli/your-mcp-servers-tools-are-confusing-your-agent-i-built-a-linter-that-scores-them-4j4d

## Related notes
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-13-your-claude-code-and-cursor-agents-have-amnesia-heres-the-fix]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
