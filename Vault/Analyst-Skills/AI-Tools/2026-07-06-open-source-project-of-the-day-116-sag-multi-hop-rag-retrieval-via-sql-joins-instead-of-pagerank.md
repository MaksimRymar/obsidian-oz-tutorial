---
title: 'Open Source Project of the Day (#116): SAG — Multi-Hop RAG Retrieval via SQL
  JOINs Instead of PageRank'
date: '2026-07-06'
source: https://dev.to/wonderlab/open-source-project-of-the-day-116-sag-multi-hop-rag-retrieval-via-sql-joins-instead-of-6j7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-05-i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-agents]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]'
- '[[2026-03-24-sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j]]'
- '[[2026-03-14-demystifying-sql-joins-window-functions]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
status: unread
---

> **TL;DR:** Introduction "Graph RAG typically pre-builds a global graph offline, then uses PageRank for query-time scoring and expansion — but PageRank has decay: the longer the chain, the lower the score. SAG uses SQL JOINs to expa…

## What’s new and why it matters
Introduction "Graph RAG typically pre-builds a global graph offline, then uses PageRank for query-time scoring and expansion — but PageRank has decay: the longer the chain, the lower the score. SAG uses SQL JOINs to expand at query time instead. No decay, no pre-built global graph." This is article #116 in the Open Source Project of the Day series. Today's project is SAG (Structured Agentic Graph) — Zleap-AI's open-source next-generation multi-hop RAG framework, backed by an arXiv paper (2606.15971). Multi-hop retrieval's core challenge: some questions need to chain information from multiple s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wonderlab/open-source-project-of-the-day-116-sag-multi-hop-rag-retrieval-via-sql-joins-instead-of-6j7

## Related notes
- [[2026-06-05-i-built-the-centralized-us-business-entity-api-that-doesnt-exist-with-an-mcp-server-for-ai-agents]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]
- [[2026-03-24-sqlite-as-a-graph-database-recursive-ctes-semantic-search-and-why-we-ditched-neo4j]]
- [[2026-03-14-demystifying-sql-joins-window-functions]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
