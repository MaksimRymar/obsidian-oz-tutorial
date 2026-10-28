---
title: I compared four ways to pick tables for a text-to-SQL prompt
date: '2026-10-28'
source: https://dev.to/ashish_sinha_5241c7673d93/i-compared-four-ways-to-pick-tables-for-a-text-to-sql-prompt-aog
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-06-05-i-tried-ai-powered-web-scraping-so-my-selectors-could-finally-rest]]'
- '[[2026-06-30-your-database-ai-agent-re-reads-the-whole-catalog-every-step-thats-the-bill]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
status: unread
---

> **TL;DR:** Every text-to-SQL prompt carries a schema. Send all of it and you pay for every table on every call. Send a few and you risk leaving out the one the question needs. So how you pick the tables matters. I tested four ways…

## What’s new and why it matters
Every text-to-SQL prompt carries a schema. Send all of it and you pay for every table on every call. Send a few and you risk leaving out the one the question needs. So how you pick the tables matters. I tested four ways on the same questions, with no model calls at all: Full schema : no picking. BM25 : keyword search over each table's definition. Embeddings : all-MiniLM-L6-v2 similarity, the usual way LangChain, LlamaIndex or Vanna pick tables from a vector store. schemagate , the open-source library I maintain, using the same MiniLM model. Each method got the same number of tables: 12 on Spid…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/i-compared-four-ways-to-pick-tables-for-a-text-to-sql-prompt-aog

## Related notes
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-06-05-i-tried-ai-powered-web-scraping-so-my-selectors-could-finally-rest]]
- [[2026-06-30-your-database-ai-agent-re-reads-the-whole-catalog-every-step-thats-the-bill]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
