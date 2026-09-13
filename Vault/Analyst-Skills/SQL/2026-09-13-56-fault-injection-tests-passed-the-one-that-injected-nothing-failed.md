---
title: 56 fault-injection tests passed. The one that injected nothing failed.
date: '2026-09-13'
source: https://dev.to/ashg2099/56-fault-injection-tests-passed-the-one-that-injected-nothing-failed-ihj
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
status: unread
---

> **TL;DR:** I was building a tool that detects when data quietly changes meaning — a vendor switching units, a source dropping a field, an undocumented enum appearing. The kind of failure where every test passes and every job is gre…

## What’s new and why it matters
I was building a tool that detects when data quietly changes meaning — a vendor switching units, a source dropping a field, an undocumented enum appearing. The kind of failure where every test passes and every job is green. Claims about detection are cheap, so I built a benchmark. 56 seeded defects across fault type, magnitude, time window and pipeline layer. Each one has a known root cause. The tool profiles the pipeline, detects drift, walks the lineage graph, and names the node where the problem started. Score it against the node I actually broke. It scored 55/56. I was pleased with myself…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashg2099/56-fault-injection-tests-passed-the-one-that-injected-nothing-failed-ihj

## Related notes
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-24-i-am-not-a-developer-i-built-a-database-audit-script-with-deepseek-here-is-where-it-went-wrong]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
