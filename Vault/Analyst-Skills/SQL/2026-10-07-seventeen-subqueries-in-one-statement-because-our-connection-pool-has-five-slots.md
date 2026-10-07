---
title: Seventeen subqueries in one statement, because our connection pool has five
  slots
date: '2026-10-07'
source: https://dev.to/daniel_pertu/seventeen-subqueries-in-one-statement-because-our-connection-pool-has-five-slots-3ceg
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]'
- '[[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
status: unread
---

> **TL;DR:** Nakodo has an operator panel at /admin : accounts, plans, campaigns, the inbound mail that failed to forward, the job queue, and a run log of the background pipeline. Its front page is a wall of numbers, and the first ve…

## What’s new and why it matters
Nakodo has an operator panel at /admin : accounts, plans, campaigns, the inbound mail that failed to forward, the job queue, and a run log of the background pipeline. Its front page is a wall of numbers, and the first version of it was the obvious thing. Fifteen counts, each its own query, all fired at once: const [ accounts , newAccounts , onboarded , free , pro , business /* ... */ ] = await Promise . all ([ db . select ({ n : count () }). from ( authUsers ), // ... fourteen more ]); That is idiomatic, it reads well, and it is wrong for this app for one reason that has nothing to do with SQL…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/daniel_pertu/seventeen-subqueries-in-one-statement-because-our-connection-pool-has-five-slots-3ceg

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]
- [[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
