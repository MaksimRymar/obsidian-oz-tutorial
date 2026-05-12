---
title: '"Cutting MCP token bloat by 12x: what happened when we packed 31 tools into
  one server"'
date: '2026-05-12'
source: https://dev.to/zoetaka38/cutting-mcp-token-bloat-by-12x-what-happened-when-we-packed-31-tools-into-one-server-4149
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]'
- '[[2026-04-03-your-ai-agent-just-deleted-something-it-shouldnt-have-heres-how-to-prevent-it]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-20-try-asqav-in-30-seconds]]'
- '[[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]'
status: unread
---

> **TL;DR:** Earlier this week @akshay_pachaar summarized a year of MCP-vs-CLI arguing into one sharp line: "The MCP vs CLI debate. For most of 2025, AI Engineers argued about it. The skeptics had real numbers: Playwright MCP eats 13…

## What’s new and why it matters
Earlier this week @akshay_pachaar summarized a year of MCP-vs-CLI arguing into one sharp line: "The MCP vs CLI debate. For most of 2025, AI Engineers argued about it. The skeptics had real numbers: Playwright MCP eats 13.7K tokens, Chrome DevTools MCP eats 18K. A 5-server setup burns 55K tokens before any work." He is right. Those numbers are the steady drumbeat against MCP as a delivery format. If your agent burns 55K tokens just advertising capabilities, the protocol starts to look like a tax. We just shipped a counter-data point. codens-mcp is a single Python package that exposes 31 tools a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zoetaka38/cutting-mcp-token-bloat-by-12x-what-happened-when-we-packed-31-tools-into-one-server-4149

## Related notes
- [[2026-04-06-i-built-an-open-source-finops-layer-for-genai-apis-real-time-usd-cost-per-otel-span-multi-tenant-isolation-zero-prompt-l]]
- [[2026-04-03-your-ai-agent-just-deleted-something-it-shouldnt-have-heres-how-to-prevent-it]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-20-try-asqav-in-30-seconds]]
- [[2026-03-02-five-things-that-break-in-production-that-anthropics-free-curriculum-skips]]
