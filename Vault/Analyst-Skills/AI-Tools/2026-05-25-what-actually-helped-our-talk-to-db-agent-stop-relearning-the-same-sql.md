---
title: What Actually Helped Our Talk-to-DB Agent Stop Relearning the Same SQL
date: '2026-05-25'
source: https://dev.to/zeeshan_ghazanfar_97/what-actually-helped-our-talk-to-db-agent-stop-relearning-the-same-sql-123m
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
related:
- '[[2026-03-23-ai-safe-mcp-server-for-sql]]'
- '[[2026-05-21-engineering-around-bitcoins-traditional-platform-lockdowns]]'
- '[[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]'
- '[[2026-04-28-i-built-a-natural-language-to-sql-generator-with-langchain-groq-and-streamlit-full-tutorial]]'
- '[[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
status: unread
---

> **TL;DR:** Natural language to SQL gets expensive when the agent keeps solving the same problem from scratch. In our Talk-to-DB layer, we added a semantic query cache: text-embedding-3-large 3072-dimensional embeddings pgvector cos…

## What’s new and why it matters
Natural language to SQL gets expensive when the agent keeps solving the same problem from scratch. In our Talk-to-DB layer, we added a semantic query cache: text-embedding-3-large 3072-dimensional embeddings pgvector cosine similarity top 5 similar cached queries injected into the system prompt table schemas stored with the cached SQL user feedback stored as thumb_up or thumb_down The failure mode was predictable. A user would ask: "Show revenue by product." The agent would generate a working SQL query. Next week, another user would ask: "Which products made the most sales?" Same intent. Same…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/zeeshan_ghazanfar_97/what-actually-helped-our-talk-to-db-agent-stop-relearning-the-same-sql-123m

## Related notes
- [[2026-03-23-ai-safe-mcp-server-for-sql]]
- [[2026-05-21-engineering-around-bitcoins-traditional-platform-lockdowns]]
- [[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]
- [[2026-04-28-i-built-a-natural-language-to-sql-generator-with-langchain-groq-and-streamlit-full-tutorial]]
- [[2026-04-13-how-i-learned-sql-by-creating-a-simple-school-database]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
