---
title: How Tian AI Builds a Million-Entry Knowledge Base on Your Phone
date: '2026-04-25'
source: https://dev.to/3969129510/how-tian-ai-builds-a-million-entry-knowledge-base-on-your-phone-4kj6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
- '[[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-29-step-by-step-guide-setting-up-rag-for-gen-ai-agents-using-iris-vector-db-in-python]]'
- '[[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]'
- '[[2026-03-04-sqlite-as-an-mcp-context-saver-stop-cramming-raw-api-data-into-your-llm]]'
status: unread
---

> **TL;DR:** SQLite at Scale: Million-Entry Knowledge Base Tian AI demonstrates that you don't need a cloud database to build a powerful knowledge base. Using SQLite with FTS5 full-text search and custom optimizations, we achieve sub…

## What’s new and why it matters
SQLite at Scale: Million-Entry Knowledge Base Tian AI demonstrates that you don't need a cloud database to build a powerful knowledge base. Using SQLite with FTS5 full-text search and custom optimizations, we achieve sub-0.05 second retrieval across a million entries -- all on your phone. Data Generation Strategy # Synthetic data generation with realistic patterns entries = [] for i in range ( 1_000_000 ): title = generate_title ( i ) content = generate_content ( i ) tags = random_tags ( 2 , 5 ) entries . append (( title , content , json . dumps ( tags ))) The key insight: batch insert 10,000…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/3969129510/how-tian-ai-builds-a-million-entry-knowledge-base-on-your-phone-4kj6

## Related notes
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
- [[2026-03-26-sqlite-can-do-more-than-you-think-full-text-search-json-window-functions-and-281tb-databases]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-29-step-by-step-guide-setting-up-rag-for-gen-ai-agents-using-iris-vector-db-in-python]]
- [[2026-03-26-sqlite-is-enough-for-your-side-project-full-text-search-json-and-wal-mode-included]]
- [[2026-03-04-sqlite-as-an-mcp-context-saver-stop-cramming-raw-api-data-into-your-llm]]
