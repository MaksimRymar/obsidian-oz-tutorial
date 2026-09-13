---
title: Spider 2.0 deleted a claim I made this morning
date: '2026-09-13'
source: https://dev.to/ashish_sinha_5241c7673d93/spider-20-deleted-a-claim-i-made-this-morning-56i9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]'
status: unread
---

> **TL;DR:** This morning I wrote that swapping the hashed vectoriser in my schema retriever for a sentence-transformer was a consistent win. I had numbers: on a pooled Spider 1.0 catalog, strict recall at k=10 went from 82.6% to 88.…

## What’s new and why it matters
This morning I wrote that swapping the hashed vectoriser in my schema retriever for a sentence-transformer was a consistent win. I had numbers: on a pooled Spider 1.0 catalog, strict recall at k=10 went from 82.6% to 88.1%. Consistent, I said. Larger than my own benchmarks suggested. This evening I ran the same comparison on Spider 2.0 and the effect vanished. Not shrank — vanished, and if anything went the other way. What follows is the run, what I think happened, and the experiment that would actually settle it, which I have not done yet. Spider 2.0 is the benchmark this problem needed Spide…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/spider-20-deleted-a-claim-i-made-this-morning-56i9

## Related notes
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]
