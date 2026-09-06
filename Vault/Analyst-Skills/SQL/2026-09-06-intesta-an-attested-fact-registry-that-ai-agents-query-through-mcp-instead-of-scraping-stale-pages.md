---
title: 'Intesta: an attested fact registry that AI agents query through MCP instead
  of scraping stale pages'
date: '2026-09-06'
source: https://dev.to/darius_ceponas_2b7889e363/intesta-an-attested-fact-registry-that-ai-agents-query-through-mcp-instead-of-scraping-stale-pages-48d9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-10-my-ai-agent-found-a-5-sigma-result-on-day-one-i-deleted-it]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
status: unread
---

> **TL;DR:** AI agents already answer questions about small businesses. Most of the time they do it from stale pages, and when the page is missing they guess. After watching agents confidently misstate delivery terms for shops near m…

## What’s new and why it matters
AI agents already answer questions about small businesses. Most of the time they do it from stale pages, and when the page is missing they guess. After watching agents confidently misstate delivery terms for shops near me, I built Intesta — a public registry where a business publishes its own facts once and every agent reads the same attested source. Site: https://intesta.io · Benchmark vs. a scraping agent: https://intesta.io/benchmark · Public traffic stats: https://intesta.io/stats The model A business registers an entity and proves domain control (a DNS TXT record or a file under /.well-kn…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/darius_ceponas_2b7889e363/intesta-an-attested-fact-registry-that-ai-agents-query-through-mcp-instead-of-scraping-stale-pages-48d9

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-10-my-ai-agent-found-a-5-sigma-result-on-day-one-i-deleted-it]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
