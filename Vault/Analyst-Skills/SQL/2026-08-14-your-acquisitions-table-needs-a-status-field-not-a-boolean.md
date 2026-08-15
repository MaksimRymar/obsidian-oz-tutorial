---
title: Your acquisitions table needs a status field, not a boolean
date: '2026-08-14'
source: https://dev.to/corpdigest/your-acquisitions-table-needs-a-status-field-not-a-boolean-1gck
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-07-15-temporal-edges-in-knowledge-graphs-why-static-edges-break-graph-rag]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-08-your-companies-table-is-lying-to-you-about-when-things-happened]]'
- '[[2026-07-24-alpha-to-beta-bringing-in-qa]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** Most schemas model corporate acquisitions as a join table: acquirer_id , target_id , price , closed_date . Some add is_completed BOOLEAN . That boolean is where the model starts lying to you. Four states a boolean cannot…

## What’s new and why it matters
Most schemas model corporate acquisitions as a join table: acquirer_id , target_id , price , closed_date . Some add is_completed BOOLEAN . That boolean is where the model starts lying to you. Four states a boolean cannot hold An acquisition is not binary. Working through several hundred company profiles, the deals refuse to sit in two buckets: Announced but not closed. In July 2026 Uber announced a voluntary takeover offer for Delivery Hero, around $14.8 billion, with closing expected in the second half of 2027 subject to conditions and regulatory approval. If your pipeline writes that row wit…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/corpdigest/your-acquisitions-table-needs-a-status-field-not-a-boolean-1gck

## Related notes
- [[2026-07-15-temporal-edges-in-knowledge-graphs-why-static-edges-break-graph-rag]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-08-your-companies-table-is-lying-to-you-about-when-things-happened]]
- [[2026-07-24-alpha-to-beta-bringing-in-qa]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
