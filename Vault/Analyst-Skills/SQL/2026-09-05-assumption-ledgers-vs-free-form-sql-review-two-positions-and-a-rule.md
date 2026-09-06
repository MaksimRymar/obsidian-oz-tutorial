---
title: 'Assumption Ledgers vs Free-Form SQL Review: Two Positions and a Rule'
date: '2026-09-05'
source: https://dev.to/dataio_4921/assumption-ledgers-vs-free-form-sql-review-two-positions-and-a-rule-27fm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-04-when-index-hit-stats-go-stale-two-positions-for-sql-review-agents]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
status: unread
---

> **TL;DR:** Scene (composite, not a production postmortem): a nightly SQL review bot posts a merge comment that sounds complete, calm, and specific. The query joins orders to customers , and the bot claims an index already covers th…

## What’s new and why it matters
Scene (composite, not a production postmortem): a nightly SQL review bot posts a merge comment that sounds complete, calm, and specific. The query joins orders to customers , and the bot claims an index already covers the foreign key. No reviewer opens the catalog, because the comment already named the index and estimated the cost. The guess never appeared as a guess, so the pull request merged with an undeclared hole. Agentic review tools now sit beside linters, and they fail in a quieter way than syntax errors. They fill missing catalog facts with fluent language instead of stopping. Cheap m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataio_4921/assumption-ledgers-vs-free-form-sql-review-two-positions-and-a-rule-27fm

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-04-when-index-hit-stats-go-stale-two-positions-for-sql-review-agents]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
