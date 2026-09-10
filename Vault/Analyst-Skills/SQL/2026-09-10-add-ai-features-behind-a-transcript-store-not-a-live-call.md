---
title: Add AI Features Behind a Transcript Store, Not a Live Call
date: '2026-09-10'
source: https://dev.to/kongkong1/add-ai-features-behind-a-transcript-store-not-a-live-call-2hme
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]'
- '[[2026-08-17-build-a-tiny-model-ledger-before-spending-free-tokens]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
status: unread
---

> **TL;DR:** The demo froze at 4:11 p.m., right when I thought the incident summary feature was finally done. Someone had clicked Generate on a long report, waited, and watched a spinner that never resolved. Was the model merely slow…

## What’s new and why it matters
The demo froze at 4:11 p.m., right when I thought the incident summary feature was finally done. Someone had clicked Generate on a long report, waited, and watched a spinner that never resolved. Was the model merely slow, or had our handler already forgotten what it asked? I opened the API logs, found a 502 from the provider, and discovered nothing durable remained. That empty log is why I now take a stubborn position on AI feature design. You should not put a live model call on the request path of a user action. You should store a transcript first, then serve the feature from records you can…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kongkong1/add-ai-features-behind-a-transcript-store-not-a-live-call-2hme

## Related notes
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]
- [[2026-08-17-build-a-tiny-model-ledger-before-spending-free-tokens]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
