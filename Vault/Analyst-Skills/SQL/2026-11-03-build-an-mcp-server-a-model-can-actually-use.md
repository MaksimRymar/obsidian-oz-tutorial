---
title: Build an MCP Server a Model Can Actually Use
date: '2026-11-03'
source: https://dev.to/ranadhir19/build-an-mcp-server-a-model-can-actually-use-1flc
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-10-21-modelling-surgical-instrument-sets-as-data-a-dilator-set-example]]'
- '[[2026-10-28-build-an-mcp-server-in-c-that-safely-queries-sql-server]]'
status: unread
---

> **TL;DR:** Most MCP tutorials stop at "it connects." But a model never sees your server code — it sees tool names, descriptions and JSON schemas. An MCP server is a user interface designed for a language model, and interfaces can b…

## What’s new and why it matters
Most MCP tutorials stop at "it connects." But a model never sees your server code — it sees tool names, descriptions and JSON schemas. An MCP server is a user interface designed for a language model, and interfaces can be measured. So I built one server twice, attacked both designs with the ten worst calls a model could plausibly make, and ran a model against each. The loose design rejected 0 of 10. The strict redesign rejected 10 of 10. Here is the full experiment — including the metric that pointed the wrong way. Two designs, one notes store The lab is a notes MCP server in pure Python stdli…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ranadhir19/build-an-mcp-server-a-model-can-actually-use-1flc

## Related notes
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-09-09-pick-agent-compute-by-blast-radius-not-by-the-price-tag]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-10-21-modelling-surgical-instrument-sets-as-data-a-dilator-set-example]]
- [[2026-10-28-build-an-mcp-server-in-c-that-safely-queries-sql-server]]
