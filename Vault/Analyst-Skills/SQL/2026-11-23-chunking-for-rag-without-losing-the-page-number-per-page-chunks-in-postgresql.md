---
title: 'Chunking for RAG without losing the page number: per-page chunks in PostgreSQL'
date: '2026-11-23'
source: https://dev.to/danbasseda/chunking-for-rag-without-losing-the-page-number-per-page-chunks-in-postgresql-1nim
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
status: unread
---

> **TL;DR:** A user asks your document Q&A system how long the warranty is. The answer comes back: "twelve months." Fine. Now they ask where that came from, and the system can't say. The text was split into chunks, the chunks were em…

## What’s new and why it matters
A user asks your document Q&A system how long the warranty is. The answer comes back: "twelve months." Fine. Now they ask where that came from, and the system can't say. The text was split into chunks, the chunks were embedded and searched, and somewhere along the way the information about which page it came from was thrown away. That's a chunking problem, not a model problem. If the chunk doesn't know its page, nothing downstream can cite it. Here's how I chunk so the file and page stay attached to every piece, all the way to the answer. Why the page gets lost Chunking exists because a whole…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/danbasseda/chunking-for-rag-without-losing-the-page-number-per-page-chunks-in-postgresql-1nim

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
