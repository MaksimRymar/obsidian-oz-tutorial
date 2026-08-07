---
title: I ran a RAG index for 13 months. 89.73% is stale, orphaned or a duplicate.
date: '2026-08-07'
source: https://dev.to/rostyslav_myronenko_faf2f/i-ran-a-rag-index-for-13-months-8973-is-stale-orphaned-or-a-duplicate-18i8
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]'
status: unread
---

> **TL;DR:** A reproducible teardown of what happens to a vector index after 13 months of real document churn, across pgvector, Qdrant and Chroma. 07 August 2026 · Rostyslav Myronenko Why I built this I build, consult and teach in th…

## What’s new and why it matters
A reproducible teardown of what happens to a vector index after 13 months of real document churn, across pgvector, Qdrant and Chroma. 07 August 2026 · Rostyslav Myronenko Why I built this I build, consult and teach in the GenAI domain, and I'm an active AWS Community Builder in AI Engineering category. One of my friends came to me with some version of "Why retrieval quality of our in-house RAG degrades over time?" - and I didn't have a satisfying answer other than "let me look". The root cause was removal of a bunch of docs belonging to another track, and this situation inspired me to write th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rostyslav_myronenko_faf2f/i-ran-a-rag-index-for-13-months-8973-is-stale-orphaned-or-a-duplicate-18i8

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-07-16-natural-language-sql-needs-guardrails-not-just-better-prompts]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]
