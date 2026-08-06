---
title: 'Batch Moderation for Existing Posts and Comments: Bulk LLM Classification
  Jobs'
date: '2026-08-06'
source: https://dev.to/jamesanderson3589/batch-moderation-for-existing-posts-and-comments-bulk-llm-classification-jobs-131e
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-07-30-how-to-batch-moderate-existing-posts-and-comments-with-an-llm-classification-api]]'
- '[[2026-08-05-decision-record-an-in-app-saas-chatbot-api-with-one-key-and-durable-transcripts]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]'
- '[[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]'
- '[[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]'
status: unread
---

> **TL;DR:** Short answer: Backfill existing posts and comments with a resumable batch job, not a loop that sends one LLM classification request at a time; persist the source identity, poll job state, then export or fetch results bef…

## What’s new and why it matters
Short answer: Backfill existing posts and comments with a resumable batch job, not a loop that sends one LLM classification request at a time; persist the source identity, poll job state, then export or fetch results before applying moderation flags in an idempotent database update. The model call is the easy part. The hard part is proving that every eligible row was classified once, that every result belongs to the exact source revision you intended to inspect, and that a restart cannot silently skip or duplicate work. I design storage layers, so I start with those invariants rather than thro…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jamesanderson3589/batch-moderation-for-existing-posts-and-comments-bulk-llm-classification-jobs-131e

## Related notes
- [[2026-07-30-how-to-batch-moderate-existing-posts-and-comments-with-an-llm-classification-api]]
- [[2026-08-05-decision-record-an-in-app-saas-chatbot-api-with-one-key-and-durable-transcripts]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-05-29-one-practical-sql-trigger-example-you-can-actually-use]]
- [[2026-04-30-the-database-is-where-ai-agents-in-production-get-weird]]
- [[2026-06-30-postgresql-mvcc-vacuum-bloat-wraparound-autovacuum-tuning-in-production]]
