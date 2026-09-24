---
title: The embedder I attached got 0 encode() calls during writes
date: '2026-09-24'
source: https://dev.to/spranab/the-embedder-i-attached-got-0-encode-calls-during-writes-1k5b
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
status: unread
---

> **TL;DR:** A brand-new memory store worked fine in one process. In the next one the plugin's init failed, and every Hermes tool call after that came back with YantrikDB is not active for this session. Underneath, the engine had ref…

## What’s new and why it matters
A brand-new memory store worked fine in one process. In the next one the plugin's init failed, and every Hermes tool call after that came back with YantrikDB is not active for this session. Underneath, the engine had refused to attach the embedder: this database's vectors were built by potion-base-8M (digest sha256:89dd…, dim 256), and the embedder being attached declares no `fingerprint` or `digest`. Queries would be encoded in a different space than the vectors they are compared against, and cosine distance still returns a plausible number for unrelated spaces — so the results would look fin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/spranab/the-embedder-i-attached-got-0-encode-calls-during-writes-1k5b

## Related notes
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
