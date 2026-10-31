---
title: 'LangGraph SummarizationMiddleware wiped my chat history: keeping the full
  transcript with PostgresSaver'
date: '2026-10-31'
source: https://dev.to/memorysync_rafay/langgraph-summarizationmiddleware-wiped-my-chat-history-keeping-the-full-transcript-with-2805
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-10-23-persistent-memory-for-crewai-1x-keep-crew-memory-across-runs-and-redeploys]]'
- '[[2026-10-23-add-persistent-memory-to-a-llamaindex-agent-memory-memory-blocks-and-a-retriever]]'
- '[[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-10-15-why-my-database-client-makes-you-review-every-edit-before-it-runs]]'
status: unread
---

> **TL;DR:** Disclosure: I work on MemorySync (I'm Mohammed, the founder). I drafted this page with AI assistance and checked it against the source thread and the official docs listed under Sources on Oct 28, 2026. I read the thread…

## What’s new and why it matters
Disclosure: I work on MemorySync (I'm Mohammed, the founder). I drafted this page with AI assistance and checked it against the source thread and the official docs listed under Sources on Oct 28, 2026. I read the thread and the LangChain docs; I didn't run this agent for this page. The question In the LangChain forum thread "LangGraph + PostgreSQL: Chat history and summarization best practice" (Apr 20, 2026), a developer building a ChatGPT-style chatbot on LangGraph, with PostgreSQL as the checkpointer, described the bind: When I summarize older messages and delete them from the database, the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/memorysync_rafay/langgraph-summarizationmiddleware-wiped-my-chat-history-keeping-the-full-transcript-with-2805

## Related notes
- [[2026-10-23-persistent-memory-for-crewai-1x-keep-crew-memory-across-runs-and-redeploys]]
- [[2026-10-23-add-persistent-memory-to-a-llamaindex-agent-memory-memory-blocks-and-a-retriever]]
- [[2026-10-11-your-chatgpt-api-bill-is-high-because-your-prompts-are-bloated-heres-a-free-checklist-to-fix-it]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-10-15-why-my-database-client-makes-you-review-every-edit-before-it-runs]]
