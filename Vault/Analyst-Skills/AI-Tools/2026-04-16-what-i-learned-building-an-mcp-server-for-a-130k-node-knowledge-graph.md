---
title: What I Learned Building an MCP Server for a 130K-Node Knowledge Graph
date: '2026-04-16'
source: https://dev.to/deadbyapril/what-i-learned-building-an-mcp-server-for-a-130k-node-knowledge-graph-31ia
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-23-build-your-first-ai-agent-with-python-and-langchain-in-2026]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
- '[[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-03-python-web-scraping-techniques-that-turn-any-website-into-structured-data]]'
- '[[2026-03-24-sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j]]'
status: unread
---

> **TL;DR:** I built a Model Context Protocol server that lets Claude query a knowledge graph with 130,000+ nodes. Here's what I learned — the parts the tutorials skip. The Setup Backend : Neo4j graph database (bolt protocol) MCP Ser…

## What’s new and why it matters
I built a Model Context Protocol server that lets Claude query a knowledge graph with 130,000+ nodes. Here's what I learned — the parts the tutorials skip. The Setup Backend : Neo4j graph database (bolt protocol) MCP Server : Python, using the mcp SDK Tools exposed : 5 read-only query tools (entity search, contact lookup, session history, fact retrieval, semantic search) Auth : Scoped bearer tokens with sensitivity tiers (public/internal/sensitive/restricted) Size : 232 lines of Python. That's it. Lesson 1: One Tool Per Question, Not One Tool Per Table My first instinct was to mirror the datab…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/deadbyapril/what-i-learned-building-an-mcp-server-for-a-130k-node-knowledge-graph-31ia

## Related notes
- [[2026-03-23-build-your-first-ai-agent-with-python-and-langchain-in-2026]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
- [[2026-04-04-build-your-first-ai-agent-with-langgraph-step-by-step-python-tutorial-2026]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-03-python-web-scraping-techniques-that-turn-any-website-into-structured-data]]
- [[2026-03-24-sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j]]
