---
title: 'Semantic Search with PostgreSQL: Pragmatism Beats Hype - Most of the Time'
date: '2026-06-24'
source: https://dev.to/ben-witt/semantic-search-with-postgresql-pragmatism-beats-hype-most-of-the-time-25cg
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-05-24-day-4-creating-tables-data-types-null-and-default-constraints]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-01-sql-joins]]'
status: unread
---

> **TL;DR:** When you start adding semantic search to an application, the obvious options are often Pinecone, Weaviate, Qdrant, Milvus, or another dedicated vector database. That can be the right choice. But many applications already…

## What’s new and why it matters
When you start adding semantic search to an application, the obvious options are often Pinecone, Weaviate, Qdrant, Milvus, or another dedicated vector database. That can be the right choice. But many applications already have a PostgreSQL database running. And for a large class of semantic search use cases, that database can do the job directly. The key is pgvector , an open-source PostgreSQL extension that adds vector types and vector similarity search to Postgres. It lets you store embeddings next to your relational data and query them with SQL. The advantage is not only fewer moving parts.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ben-witt/semantic-search-with-postgresql-pragmatism-beats-hype-most-of-the-time-25cg

## Related notes
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-05-24-day-4-creating-tables-data-types-null-and-default-constraints]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-01-sql-joins]]
