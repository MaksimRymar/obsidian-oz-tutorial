---
title: Hybrid Search (Full-Text and Vector Similarity) in HorizonDB
date: '2026-06-29'
source: https://dev.to/franckpachot/hybrid-search-full-text-and-vector-similarity-in-horizondb-3a5f
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-03-01-pgvector-distance-functions-cosine-vs-l2-vs-inner-product]]'
- '[[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
status: unread
---

> **TL;DR:** You may have read about Hybrid search for Azure HorizonDB . It is presented as combining BM25 full‑text and vector similarity in a single query. But how are they actually combined? The execution plan answers that. In thi…

## What’s new and why it matters
You may have read about Hybrid search for Azure HorizonDB . It is presented as combining BM25 full‑text and vector similarity in a single query. But how are they actually combined? The execution plan answers that. In this post, I use a small synthetic product catalog to ensure the entire demo is reproducible. The text is sufficiently realistic for BM25 queries, and the embeddings are deterministic synthetic vectors, allowing you to run the full script without needing an embedding model. If you have azure_openai.create_embeddings() configured, you can substitute the synthetic embedding function…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/franckpachot/hybrid-search-full-text-and-vector-similarity-in-horizondb-3a5f

## Related notes
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-03-01-pgvector-distance-functions-cosine-vs-l2-vs-inner-product]]
- [[2026-03-09-mastering-sql-joins-and-window-functions-with-real-examples]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
