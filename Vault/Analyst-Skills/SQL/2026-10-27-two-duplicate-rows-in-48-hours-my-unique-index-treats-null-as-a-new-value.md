---
title: 'Two Duplicate Rows in 48 Hours: My Unique Index Treats NULL as a New Value'
date: '2026-10-27'
source: https://dev.to/codepy_1473/two-duplicate-rows-in-48-hours-my-unique-index-treats-null-as-a-new-value-3jmb
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-19-indexes-in-postgresql]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
status: unread
---

> **TL;DR:** I shipped a nightly enrichment job with a unique index on (tenant_id, source_hash) and called it idempotent. Forty-eight hours later I had three rows for one tenant and one source document, all identical, and the index h…

## What’s new and why it matters
I shipped a nightly enrichment job with a unique index on (tenant_id, source_hash) and called it idempotent. Forty-eight hours later I had three rows for one tenant and one source document, all identical, and the index had approved every one of them. If a unique index is unique, how does an insert get past it twice? The answer is not a race, a bug in Postgres, or a failed commit — it is one nullable column and a rule most of us read once and then forget. I want to write this down because the fix took ten minutes and the diagnosis took a weekend, and because the harness I used is short enough t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codepy_1473/two-duplicate-rows-in-48-hours-my-unique-index-treats-null-as-a-new-value-3jmb

## Related notes
- [[2026-10-19-indexes-in-postgresql]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-26-postgresql-unique-constraint-vs-unique-index-which-to-use-and-how-to-add-one-without-locking-the-table]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
