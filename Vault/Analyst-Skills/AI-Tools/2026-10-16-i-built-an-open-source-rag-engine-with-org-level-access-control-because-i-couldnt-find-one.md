---
title: I built an open-source RAG engine with org-level access control, because I
  couldn't find one
date: '2026-10-16'
source: https://dev.to/njnagaraj/i-built-an-open-source-rag-engine-with-org-level-access-control-because-i-couldnt-find-one-1643
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-19-a-rest-api-for-polymarket-whale-data-a-developer-guide]]'
- '[[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]'
- '[[2026-04-20-try-asqav-in-30-seconds]]'
- '[[2026-09-05-let-non-technical-teammates-query-the-database-without-handing-out-db-access]]'
- '[[2026-04-27-archery-cli-a-psql-style-cli-for-archery-query-databases-from-terminal-or-ai-agents]]'
status: unread
---

> **TL;DR:** Most open-source RAG tools I tried had the same gap. Either org-level access control sat behind a paid enterprise tier, or everything lived in one shared workspace per team. For a real company, where HR, finance, and eng…

## What’s new and why it matters
Most open-source RAG tools I tried had the same gap. Either org-level access control sat behind a paid enterprise tier, or everything lived in one shared workspace per team. For a real company, where HR, finance, and engineering can't all see each other's documents, that isn't enough. So I built Production RAG , a local-first RAG engine with org support built in, under Apache 2.0. Permissions belong in the query, not after it Many RAG setups retrieve the top-k chunks and then filter out what the user can't see. That leaks information through ranking, and it returns fewer results than asked for…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/njnagaraj/i-built-an-open-source-rag-engine-with-org-level-access-control-because-i-couldnt-find-one-1643

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-19-a-rest-api-for-polymarket-whale-data-a-developer-guide]]
- [[2026-06-01-how-i-built-a-zero-token-memory-layer-for-llms-and-why-it-outperforms-vector-store-approaches]]
- [[2026-04-20-try-asqav-in-30-seconds]]
- [[2026-09-05-let-non-technical-teammates-query-the-database-without-handing-out-db-access]]
- [[2026-04-27-archery-cli-a-psql-style-cli-for-archery-query-databases-from-terminal-or-ai-agents]]
