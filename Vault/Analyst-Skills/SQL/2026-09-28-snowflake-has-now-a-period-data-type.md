---
title: Snowflake has now a PERIOD Data Type
date: '2026-09-28'
source: https://dev.to/fabian_stadler/snowflake-period-a-small-test-of-temporal-boundaries-42c7
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** Snowflake recently made the PERIOD generally available. I saw it in the release notes and wondered what it would change in a model that already has valid_from and valid_to . Two date columns are not hard to understand. T…

## What’s new and why it matters
Snowflake recently made the PERIOD generally available. I saw it in the release notes and wondered what it would change in a model that already has valid_from and valid_to . Two date columns are not hard to understand. The part that tends to cause trouble is agreeing on what happens at the edge. Therefore, I tried a small subscription example to make that edge visible. It has an old plan, a renewal that overlaps it, and a replacement that starts on the old plan's end date. I wanted to check two things: would PERIOD call the last pair adjacent rather than overlapping, and would its result match…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/fabian_stadler/snowflake-period-a-small-test-of-temporal-boundaries-42c7

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-13-3-testing-habits-that-caught-bugs-before-my-users-did]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
