---
title: Mnemosyne – A local, Hebbian memory server for Claude/Cursor (MCP)
date: '2026-05-04'
source: https://dev.to/taterlabsllc/mnemosyne-a-local-hebbian-memory-server-for-claudecursor-mcp-3bfm
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-04-16-what-i-learned-building-an-mcp-server-for-a-130k-node-knowledge-graph]]'
- '[[2026-03-04-sqlite-as-a-vector-database-yes-really]]'
- '[[2026-03-27-hyc-image-mcp-tutorial-image-understanding-ocr-with-mcp-nexaapi-python-guide-2026]]'
- '[[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
status: unread
---

> **TL;DR:** I'm Zackery, a solo dev. I got frustrated with the current state of LLM memory (mostly just dumping embeddings into a vector DB and doing a top-K semantic search). It feels like a filing cabinet, not a brain. I built Mne…

## What’s new and why it matters
I'm Zackery, a solo dev. I got frustrated with the current state of LLM memory (mostly just dumping embeddings into a vector DB and doing a top-K semantic search). It feels like a filing cabinet, not a brain. I built Mnemosyne as a local, associative memory backend that plugs directly into Claude Desktop, Cursor, and Windsurf via the Model Context Protocol (MCP). Instead of standard RAG, it uses a SQLite graph with spreading activation and Hebbian decay. How it works: It uses SQLite FTS5 for the initial retrieval (BM25). It then performs a Breadth-First Search (BFS) across a localized graph of…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/taterlabsllc/mnemosyne-a-local-hebbian-memory-server-for-claudecursor-mcp-3bfm

## Related notes
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-04-16-what-i-learned-building-an-mcp-server-for-a-130k-node-knowledge-graph]]
- [[2026-03-04-sqlite-as-a-vector-database-yes-really]]
- [[2026-03-27-hyc-image-mcp-tutorial-image-understanding-ocr-with-mcp-nexaapi-python-guide-2026]]
- [[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
