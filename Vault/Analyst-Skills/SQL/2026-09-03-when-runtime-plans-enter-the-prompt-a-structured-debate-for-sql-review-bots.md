---
title: 'When Runtime Plans Enter the Prompt: A Structured Debate for SQL Review Bots'
date: '2026-09-03'
source: https://dev.to/dataio_4921/when-runtime-plans-enter-the-prompt-a-structured-debate-for-sql-review-bots-2i3e
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** The following scene is a composite on-call pattern, not a personal claim about one employer. A checkout query crossed its p95 budget during a mid-afternoon spike, and the reviewer copied the plan. The paste included actu…

## What’s new and why it matters
The following scene is a composite on-call pattern, not a personal claim about one employer. A checkout query crossed its p95 budget during a mid-afternoon spike, and the reviewer copied the plan. The paste included actual rows, shared hit counts, and a filter on a customer email that should never leave the database host. The nested loop looked cheap in EXPLAIN and expensive in EXPLAIN ANALYZE , so the reviewer wanted a second opinion from a model. That single paste created a durable contract question: should runtime plans enter the model context at all? Static SQL text is easy to version, red…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/dataio_4921/when-runtime-plans-enter-the-prompt-a-structured-debate-for-sql-review-bots-2i3e

## Related notes
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-28-stop-writing-raw-sql-in-your-migrations-most-of-the-time]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-03-speeding-up-a-slow-plsql-routine-with-bulk-collect-and-forall]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
