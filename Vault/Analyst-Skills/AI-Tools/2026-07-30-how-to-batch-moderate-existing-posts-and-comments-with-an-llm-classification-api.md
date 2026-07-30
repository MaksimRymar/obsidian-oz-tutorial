---
title: How to batch moderate existing posts and comments with an LLM classification
  API
date: '2026-07-30'
source: https://dev.to/svennilsson228/how-to-batch-moderate-existing-posts-and-comments-with-an-llm-classification-api-28oc
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]'
- '[[2026-07-07-the-content-audit-that-didnt-need-me-to-build-a-scraper]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-06-24-why-i-run-ai-locally-instead-of-using-chatgpt-for-client-work]]'
- '[[2026-06-22-how-i-cut-my-llm-api-bill-by-80-with-a-simple-router]]'
status: unread
---

> **TL;DR:** Short answer: for a moderation backfill over existing posts and comments, submit the whole backlog as one bulk job and poll it, instead of firing one LLM classification request per row. Every batch API worth using is bui…

## What’s new and why it matters
Short answer: for a moderation backfill over existing posts and comments, submit the whole backlog as one bulk job and poll it, instead of firing one LLM classification request per row. Every batch API worth using is built for that shape, and the export step — the part that writes verdicts back into your database — is where the real work hides. I've done this three times now, on three different products. The first two times I did it the slow way. Why the one-request-per-row loop dies under real traffic Last year I ran a policy re-check across 412,000 forum comments with a thread pool and a pla…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/svennilsson228/how-to-batch-moderate-existing-posts-and-comments-with-an-llm-classification-api-28oc

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]
- [[2026-07-07-the-content-audit-that-didnt-need-me-to-build-a-scraper]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-06-24-why-i-run-ai-locally-instead-of-using-chatgpt-for-client-work]]
- [[2026-06-22-how-i-cut-my-llm-api-bill-by-80-with-a-simple-router]]
