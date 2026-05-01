---
title: The database is where AI agents in production get weird
date: '2026-04-30'
source: https://dev.to/saluc28/the-database-is-where-ai-agents-in-production-get-weird-4lj4
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-12-every-ai-pitch-at-forbes-under-30-had-the-same-architecture-gap]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-03-23-ai-safe-mcp-server-for-sql]]'
status: unread
---

> **TL;DR:** A lot of what I keep reading online about shipping LLM agents to production skips over the database layer, and I think that is going to be the awkward part of the whole wave. Not because anyone is doing anything stupid.…

## What’s new and why it matters
A lot of what I keep reading online about shipping LLM agents to production skips over the database layer, and I think that is going to be the awkward part of the whole wave. Not because anyone is doing anything stupid. Because the assumptions baked into how we secure databases were written for a caller that does not really exist anymore. A traditional service hits the database with a small, predictable set of queries. You can review them, unit test them, put them behind stored procedures and call it a day. Even a messy web app has at most a few hundred query shapes total, and most of them rhy…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/saluc28/the-database-is-where-ai-agents-in-production-get-weird-4lj4

## Related notes
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-12-every-ai-pitch-at-forbes-under-30-had-the-same-architecture-gap]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-03-23-ai-safe-mcp-server-for-sql]]
