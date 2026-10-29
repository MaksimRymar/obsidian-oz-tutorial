---
title: 'Modelling a shared inbox: why the message is the primary key, not the conversation'
date: '2026-10-29'
source: https://dev.to/imonitorsoft/modelling-a-shared-inbox-why-the-message-is-the-primary-key-not-the-conversation-3cjn
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]'
- '[[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]'
- '[[2026-05-25-safer-nl2sql-with-select-ai-and-ai-profiles]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
status: unread
---

> **TL;DR:** Every shared-inbox implementation starts with a conversations table and ends up regretting it. Here is the model that survives contact with real support traffic. The problem with conversation-first A conversation is a de…

## What’s new and why it matters
Every shared-inbox implementation starts with a conversations table and ends up regretting it. Here is the model that survives contact with real support traffic. The problem with conversation-first A conversation is a derived thing. It is what you get after you decide which messages belong together. If you store conversations as the source of truth, every new channel forces you to write merge logic that mutates the conversation rows — and merges are the one operation that must never lose data. Messages, by contrast, arrive once and never change. They are the natural primary key. The model -- t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/imonitorsoft/modelling-a-shared-inbox-why-the-message-is-the-primary-key-not-the-conversation-3cjn

## Related notes
- [[2026-04-21-sql-joins-and-window-functions-a-practical-guide]]
- [[2026-09-02-deriving-data-quality-rules-from-the-schema-what-the-metadata-already-knows]]
- [[2026-05-25-safer-nl2sql-with-select-ai-and-ai-profiles]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
