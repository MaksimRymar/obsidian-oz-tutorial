---
title: I Poisoned My Own MCP Server in 5 Minutes. Here's How.
date: '2026-03-30'
source: https://dev.to/acacian/i-poisoned-my-own-mcp-server-in-5-minutes-heres-how-380
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
- '[[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]'
status: unread
---

> **TL;DR:** Last week I set up a simple MCP server for file operations. Then I wondered: what happens if I put instructions in the tool description that the LLM isn't supposed to follow? Turns out, it follows them. Every time. This…

## What’s new and why it matters
Last week I set up a simple MCP server for file operations. Then I wondered: what happens if I put instructions in the tool description that the LLM isn't supposed to follow? Turns out, it follows them. Every time. This post walks through three attacks I ran against my own AI agent. All of them worked. No exploits, no buffer overflows — just text in the wrong place. Setup: a normal MCP server Here's a minimal MCP server that reads files. Nothing unusual. # server.py — a "safe" file reader from mcp.server.fastmcp import FastMCP mcp = FastMCP ( " file-reader " ) @mcp.tool () def read_file ( path…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/acacian/i-poisoned-my-own-mcp-server-in-5-minutes-heres-how-380

## Related notes
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
- [[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]
