---
title: What is Hybrid search in RAGs?
date: '2026-04-30'
source: https://dev.to/rushanksavant/what-is-hybrid-search-in-rags-5277
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-04-08-rag-in-production-the-chunking-and-retrieval-mistakes-everyone-makes]]'
- '[[2026-04-25-6-essential-sql-concepts-every-beginner-should-master]]'
- '[[2026-04-21-15-engineering-decisions-behind-rag-hybrid-search]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
status: unread
---

> **TL;DR:** ⚠️Need of Hybrid Search We have documents containing error codes in python with their respective definitions and use-cases. User writes a query to know about "What is ERR_404_AUTH?" Classic Rag: Will retrieve all the aut…

## What’s new and why it matters
⚠️Need of Hybrid Search We have documents containing error codes in python with their respective definitions and use-cases. User writes a query to know about "What is ERR_404_AUTH?" Classic Rag: Will retrieve all the authentication and error related context it can find from vector db (document embeddings). Lexical search: Will search for terms ["What", "is", "ERR_404_AUTH"] Hybrid search: Will search for keyword "ERR_404_AUTH" and retrieve semantically similar documents using similarity search. 🛠️Using BM25 Take BM25 as extended version of TF-IDF for key-word based search. The step-wise implem…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rushanksavant/what-is-hybrid-search-in-rags-5277

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-04-08-rag-in-production-the-chunking-and-retrieval-mistakes-everyone-makes]]
- [[2026-04-25-6-essential-sql-concepts-every-beginner-should-master]]
- [[2026-04-21-15-engineering-decisions-behind-rag-hybrid-search]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
