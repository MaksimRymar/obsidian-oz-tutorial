---
title: How I Built an MCP Server That Combines Hunter.io and Apollo for B2B Lead Enrichment
date: '2026-06-30'
source: https://dev.to/alekseypanf/how-i-built-an-mcp-server-that-combines-hunterio-and-apollo-for-b2b-lead-enrichment-lnk
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-04-30-your-mcp-servers-are-flying-blind-heres-how-to-fix-it]]'
- '[[2026-03-08-i-built-a-rest-api-generator-in-python-so-you-never-mock-an-endpoint-again]]'
- '[[2026-05-17-devmcp-context-a-simple-ai-memory-layer-for-your-agent]]'
- '[[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]'
- '[[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]'
status: unread
---

> **TL;DR:** AI agents are powerful, but without real data they're just confident bullshitters. You can plug Claude into a CRM and ask "find me leads in fintech with 50-200 employees" all day, and it'll make stuff up. Until you give…

## What’s new and why it matters
AI agents are powerful, but without real data they're just confident bullshitters. You can plug Claude into a CRM and ask "find me leads in fintech with 50-200 employees" all day, and it'll make stuff up. Until you give it tools that actually fetch data. That's what MCP servers are for. And that's what I built. This post walks through b2b-enrichment-mcp, an open-source MCP server I shipped recently. It combines two B2B data APIs (Hunter.io for emails, Apollo.io for company info) into a single tool layer that Claude can use directly. The whole thing is async Python, FastMCP, MIT licensed, and r…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alekseypanf/how-i-built-an-mcp-server-that-combines-hunterio-and-apollo-for-b2b-lead-enrichment-lnk

## Related notes
- [[2026-04-30-your-mcp-servers-are-flying-blind-heres-how-to-fix-it]]
- [[2026-03-08-i-built-a-rest-api-generator-in-python-so-you-never-mock-an-endpoint-again]]
- [[2026-05-17-devmcp-context-a-simple-ai-memory-layer-for-your-agent]]
- [[2026-04-20-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-04-27-i-built-a-pay-per-call-trading-signal-api-for-ai-agents]]
- [[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]
