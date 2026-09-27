---
title: Normalizing public job-board data with Python
date: '2026-09-27'
source: https://dev.to/abdulwhab95/normalizing-public-job-board-data-with-python-3pno
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** Many companies host their careers page on Greenhouse, Lever or Ashby, and each of these vendors documents a public, read-only JSON API for those boards. You don't need a key or a login. The catch is that the three APIs d…

## What’s new and why it matters
Many companies host their careers page on Greenhouse, Lever or Ashby, and each of these vendors documents a public, read-only JSON API for those boards. You don't need a key or a login. The catch is that the three APIs describe a job in three different ways, so putting several boards in one spreadsheet means mapping three shapes into one. This post covers: how the three APIs differ, a small standard-library Python script that normalizes title, location and apply link (plus a few optional fields), real output from a run on 27 September 2026 (UTC), JSON and CSV export, missing values, source lim…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/abdulwhab95/normalizing-public-job-board-data-with-python-3pno

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
