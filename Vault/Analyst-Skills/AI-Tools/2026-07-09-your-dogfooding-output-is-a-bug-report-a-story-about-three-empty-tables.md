---
title: Your dogfooding output IS a bug report, a story about three empty tables
date: '2026-07-09'
source: https://dev.to/saravananj2294/your-dogfooding-output-is-a-bug-report-a-story-about-three-empty-tables-4b1n
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-04-30-your-mcp-servers-are-flying-blind-heres-how-to-fix-it]]'
- '[[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]'
- '[[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]'
status: unread
---

> **TL;DR:** I ship world-model-mcp — a temporal knowledge graph MCP server that gives AI coding agents (Claude Code, Cursor, Copilot Chat, etc.) durable memory across sessions. It captures facts about your codebase, learned constrai…

## What’s new and why it matters
I ship world-model-mcp — a temporal knowledge graph MCP server that gives AI coding agents (Claude Code, Cursor, Copilot Chat, etc.) durable memory across sessions. It captures facts about your codebase, learned constraints from your corrections, and lifecycle events from every coding session. A month after v0.11 shipped, I ran the graph on the world-model-mcp repo itself — dogfooded it and snapshotted what it captured. The numbers looked like this: 608 facts. 600 entities. 3 constraints. That should have been a headline: my own memory layer captured a rich picture of its own codebase. Except…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/saravananj2294/your-dogfooding-output-is-a-bug-report-a-story-about-three-empty-tables-4b1n

## Related notes
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-04-30-your-mcp-servers-are-flying-blind-heres-how-to-fix-it]]
- [[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]
- [[2026-06-10-i-built-a-tool-that-generates-api-docs-from-your-source-code---no-annotations-no-server-running-no-swagger-config]]
