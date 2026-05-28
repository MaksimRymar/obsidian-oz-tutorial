---
title: I built an MCP server that gives AI persistent memory of your SQL database
date: '2026-05-28'
source: https://dev.to/surajkgoyal/i-built-an-mcp-server-that-gives-ai-persistent-memory-of-your-sql-database-3d2a
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-03-23-ai-safe-mcp-server-for-sql]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-04-16-what-i-learned-building-an-mcp-server-for-a-130k-node-knowledge-graph]]'
- '[[2026-04-02-im-an-ai-agent-that-built-its-own-training-data-pipeline]]'
status: unread
---

> **TL;DR:** A while ago I tried to build a local coding assistant. I downloaded Qwen3, fired it up on my MacBook with 16GB of RAM, and within a day realized the output quality was nowhere close to Claude or GPT-5. The model could fi…

## What’s new and why it matters
A while ago I tried to build a local coding assistant. I downloaded Qwen3, fired it up on my MacBook with 16GB of RAM, and within a day realized the output quality was nowhere close to Claude or GPT-5. The model could fit . It just couldn't compete . So I changed the question. If I can't make the model smarter on my hardware, can I make what I feed it smarter? Where the tokens actually go I started watching where my Claude / Cursor / Copilot sessions actually spent their tokens. The surprise: most of it wasn't reasoning. It was lookup . Every fresh chat about my company's database re-discovere…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/surajkgoyal/i-built-an-mcp-server-that-gives-ai-persistent-memory-of-your-sql-database-3d2a

## Related notes
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-03-23-ai-safe-mcp-server-for-sql]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-04-16-what-i-learned-building-an-mcp-server-for-a-130k-node-knowledge-graph]]
- [[2026-04-02-im-an-ai-agent-that-built-its-own-training-data-pipeline]]
