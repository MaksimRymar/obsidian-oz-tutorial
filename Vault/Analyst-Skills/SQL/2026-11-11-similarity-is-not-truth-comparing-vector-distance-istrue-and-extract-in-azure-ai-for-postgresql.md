---
title: 'Similarity Is Not Truth: Comparing vector distance, is_true(), and extract()
  in Azure AI for PostgreSQL'
date: '2026-11-11'
source: https://dev.to/franckpachot/similarity-is-not-truth-comparing-vector-distance-istrue-and-extract-in-azure-ai-for-2and
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-30-cte-vs-temporary-tables-in-sql-which-one-should-you-use]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-09-21-build-bilingual-document-search-with-devup-ai-embeddings-reranking-and-answers-with-sources]]'
- '[[2026-06-09-pandas-vs-sql-when-to-use-each]]'
status: unread
---

> **TL;DR:** Vector search queries often use top-k similarity, assuming the highest-scoring results are true and can serve as factual validation. High scores represent low distances between vectors (e.g., <=> for cosine distance in P…

## What’s new and why it matters
Vector search queries often use top-k similarity, assuming the highest-scoring results are true and can serve as factual validation. High scores represent low distances between vectors (e.g., <=> for cosine distance in PostgreSQL with pgvector). They should be used to retrieve a relevant subset to rank or qualify—not as a final ranking of truth. Azure AI on HorizonDB can call an AI model to generate embeddings for comparison and provides more specific functions, such is_true() or extract() , for structured responses. Objective In this blog post, I'll use the three of them on a small dataset, a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/franckpachot/similarity-is-not-truth-comparing-vector-distance-istrue-and-extract-in-azure-ai-for-2and

## Related notes
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-30-cte-vs-temporary-tables-in-sql-which-one-should-you-use]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-09-21-build-bilingual-document-search-with-devup-ai-embeddings-reranking-and-answers-with-sources]]
- [[2026-06-09-pandas-vs-sql-when-to-use-each]]
