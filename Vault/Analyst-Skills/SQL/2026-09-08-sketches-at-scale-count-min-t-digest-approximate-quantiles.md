---
title: 'Sketches at Scale: Count-Min, t-digest & Approximate Quantiles'
date: '2026-09-08'
source: https://dev.to/gowthampotureddi/sketches-at-scale-count-min-t-digest-approximate-quantiles-427l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#library'
- '#presentations'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]'
- '[[2026-06-08-retention-cohort-analysis-with-plain-sql]]'
status: unread
---

> **TL;DR:** data sketches are the compact, probabilistic data structures that let you answer "how many times did this key appear?", "what are the top few heaviest keys?", and "what is the 99th-percentile latency?" over a stream so l…

## What’s new and why it matters
data sketches are the compact, probabilistic data structures that let you answer "how many times did this key appear?", "what are the top few heaviest keys?", and "what is the 99th-percentile latency?" over a stream so large you can never hold it in memory — and they are the single tool that separates an engineer who says "we'd sample it" from one who says "we'd sketch it with a bounded error." A sketch reads the stream once, keeps a summary that is sublinear in the size of the data (often a few kilobytes for a billion events), and answers queries with a guarantee of the form "the answer is wi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/sketches-at-scale-count-min-t-digest-approximate-quantiles-427l

## Related notes
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-04-29-aggregations-counting-summing-and-averaging-your-data]]
- [[2026-06-08-retention-cohort-analysis-with-plain-sql]]
