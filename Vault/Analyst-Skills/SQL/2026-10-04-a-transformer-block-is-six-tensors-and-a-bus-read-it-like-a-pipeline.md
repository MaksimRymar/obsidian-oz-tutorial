---
title: 'A transformer block is six tensors and a bus: read it like a pipeline'
date: '2026-10-04'
source: https://dev.to/cchinchilladev/a-transformer-block-is-six-tensors-and-a-bus-read-it-like-a-pipeline-34a8
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]'
status: unread
---

> **TL;DR:** Originally published at cchinchilla.dev . Part 5 of From code to weights, a 12-part series on ML fundamentals for engineers. Part 4 ended on one stage. A decoder is a stack of blocks, twelve in GPT-2 small, and attention…

## What’s new and why it matters
Originally published at cchinchilla.dev . Part 5 of From code to weights, a 12-part series on ML fundamentals for engineers. Part 4 ended on one stage. A decoder is a stack of blocks, twelve in GPT-2 small, and attention is one of two stages in each. This post reads a whole block the way you'd read a pipeline: what flows in, what each stage writes, and where the parameters and the cost end up. They don't end up in the same place. I read Block in nanoGPT's model.py with the shapes in the margin and loaded GPT-2's weights into it. Then I broke it on purpose: I took blocks out one at a time, then…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/cchinchilladev/a-transformer-block-is-six-tensors-and-a-bus-read-it-like-a-pipeline-34a8

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-09-18-how-we-grade-hundreds-of-sports-picks-a-day-in-public]]
