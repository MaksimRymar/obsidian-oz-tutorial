---
title: Letting AI agents query my databases without ever giving them the credentials
date: '2026-10-20'
source: https://dev.to/cccadet/letting-ai-agents-query-my-databases-without-ever-giving-them-the-credentials-12nf
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]'
- '[[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]'
- '[[2026-03-23-ai-safe-mcp-server-for-sql]]'
- '[[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]'
- '[[2026-06-04-why-llm-agents-still-cant-query-nosql-databases]]'
status: unread
---

> **TL;DR:** Every time I connect an AI agent to a database, the same question comes up: where does the connection string live? Usually the answer is "in the agent's config file", which means a password sitting in a JSON file next to…

## What’s new and why it matters
Every time I connect an AI agent to a database, the same question comes up: where does the connection string live? Usually the answer is "in the agent's config file", which means a password sitting in a JSON file next to a tool I don't fully control. I took a different route in omni-sql , an open-source desktop SQL IDE. The IDE already holds my connections (passwords live in the OS keyring). It also runs a local MCP server, so the agent talks to the IDE, not to the database. How it works The MCP server runs over STDIO on loopback. The agent never receives a host, user, password or connection s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cccadet/letting-ai-agents-query-my-databases-without-ever-giving-them-the-credentials-12nf

## Related notes
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-05-13-ai-database-agents-need-result-contracts-not-just-rows]]
- [[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]
- [[2026-03-23-ai-safe-mcp-server-for-sql]]
- [[2026-03-30-i-stopped-pasting-ddl-into-random-chatbots-heres-the-local-windows-db-client-i-use]]
- [[2026-06-04-why-llm-agents-still-cant-query-nosql-databases]]
