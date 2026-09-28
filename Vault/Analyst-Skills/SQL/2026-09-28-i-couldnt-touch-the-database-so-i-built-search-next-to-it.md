---
title: I couldn't touch the database, so I built search next to it
date: '2026-09-28'
source: https://dev.to/_er2es_/i-couldnt-touch-the-database-so-i-built-search-next-to-it-1pjn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** A production system I work on needed a search box that forgives people. They type kavefozo and expect Kávéfőző . They type hedphones and expect headphones. The constraints were the interesting part: The schema could not…

## What’s new and why it matters
A production system I work on needed a search box that forgives people. They type kavefozo and expect Kávéfőző . They type hedphones and expect headphones. The constraints were the interesting part: The schema could not change. No new columns, no generated columns, no migrations on tables that weren't ours. No new infrastructure. No Elasticsearch, no Meilisearch, no extra service to run, sync, back up and secure. So search had to happen inside the database that was already there. PostgreSQL turned out to have almost every piece needed. Wiring those pieces together properly was the hard part, a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/_er2es_/i-couldnt-touch-the-database-so-i-built-search-next-to-it-1pjn

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
