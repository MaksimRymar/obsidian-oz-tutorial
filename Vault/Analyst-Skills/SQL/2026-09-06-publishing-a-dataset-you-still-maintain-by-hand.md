---
title: Publishing a dataset you still maintain by hand
date: '2026-09-06'
source: https://dev.to/jagelski/publishing-a-dataset-you-still-maintain-by-hand-eof
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** We keep a set of regulatory reference tables by hand. Fifty jurisdictions, one row each, describing what it takes to get a crypto licence in that country: the regulator, the operative instrument, the statutory minimum ca…

## What’s new and why it matters
We keep a set of regulatory reference tables by hand. Fifty jurisdictions, one row each, describing what it takes to get a crypto licence in that country: the regulator, the operative instrument, the statutory minimum capital, the licence term, the timeline. The tables sit behind a comparison tool on our site and they change whenever a regulator moves. People were screenshotting them. That is a reasonable thing for a reader to do and a bad thing for the reader to end up with. A screenshot has no date, no provenance and no way to check whether the number moved last Tuesday. So we published the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/jagelski/publishing-a-dataset-you-still-maintain-by-hand-eof

## Related notes
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
