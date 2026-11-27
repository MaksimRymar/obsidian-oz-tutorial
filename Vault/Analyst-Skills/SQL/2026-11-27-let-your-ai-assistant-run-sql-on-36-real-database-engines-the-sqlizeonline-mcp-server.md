---
title: 'Let your AI assistant run SQL on 36 real database engines: the sqlize.online
  MCP server'
date: '2026-11-27'
source: https://dev.to/rozhnev/let-your-ai-assistant-run-sql-on-36-real-database-engines-the-sqlizeonline-mcp-server-253d
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-11-04-a-10-minute-sql-window-functions-lesson-from-a-chat-app-and-i-re-ran-its-queries]]'
- '[[2026-10-28-build-an-mcp-server-in-c-that-safely-queries-sql-server]]'
- '[[2026-07-01-ql-ai-database-solutions-building-a-text-to-sql-pipeline-you-can-actually-run]]'
status: unread
---

> **TL;DR:** AI assistants are good at writing SQL and bad at knowing whether it actually runs. Is || string concatenation in MySQL? Does that window function work in SQL Server 2017? Does PostgreSQL 19 still accept this syntax? The…

## What’s new and why it matters
AI assistants are good at writing SQL and bad at knowing whether it actually runs. Is || string concatenation in MySQL? Does that window function work in SQL Server 2017? Does PostgreSQL 19 still accept this syntax? The model guesses, you copy the query into a terminal, and only then do you find out. Today I launched an MCP server for sqlize.online , the online SQL sandbox I've been running for several years. Now Claude, Cursor, VS Code Copilot and any other Model Context Protocol client can run SQL themselves, on real database engines, and show you the actual result instead of a guess. It's l…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/rozhnev/let-your-ai-assistant-run-sql-on-36-real-database-engines-the-sqlizeonline-mcp-server-253d

## Related notes
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-11-04-a-10-minute-sql-window-functions-lesson-from-a-chat-app-and-i-re-ran-its-queries]]
- [[2026-10-28-build-an-mcp-server-in-c-that-safely-queries-sql-server]]
- [[2026-07-01-ql-ai-database-solutions-building-a-text-to-sql-pipeline-you-can-actually-run]]
