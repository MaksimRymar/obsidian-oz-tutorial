---
title: '48-Hour Field Notes: The Batch Worker Vanished and My Re-Run Redid Every Item'
date: '2026-10-18'
source: https://dev.to/codepy_1473/48-hour-field-notes-the-batch-worker-vanished-and-my-re-run-redid-every-item-505k
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-09-02-the-48-hour-verdict-sort-your-ai-failures-before-you-fix-them]]'
- '[[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]'
- '[[2026-10-17-retries-timeouts-and-model-fallback-for-openai-compatible-apis-in-40-lines-of-python]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
status: unread
---

> **TL;DR:** Two days ago I started a batch of prompt evaluations, closed the laptop lid, and assumed the free server would keep chewing through the queue while I slept. It did not. When I opened the terminal the next morning, the wo…

## What’s new and why it matters
Two days ago I started a batch of prompt evaluations, closed the laptop lid, and assumed the free server would keep chewing through the queue while I slept. It did not. When I opened the terminal the next morning, the worker was gone and the only output was a JSONL file that stopped in the middle of a record. Why do we keep trusting long-running processes we never instrumented? This is a field note about the 48 hours that followed: the naive loop I wrote, the four ways it lied to me, and the small ledger I now put in front of every batch that outlives a single shell session. What I built first…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codepy_1473/48-hour-field-notes-the-batch-worker-vanished-and-my-re-run-redid-every-item-505k

## Related notes
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-09-02-the-48-hour-verdict-sort-your-ai-failures-before-you-fix-them]]
- [[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]
- [[2026-10-17-retries-timeouts-and-model-fallback-for-openai-compatible-apis-in-40-lines-of-python]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
