---
title: 'How Uber Scaled Text-to-SQL to 1.2M Monthly Queries: Inside QueryGPT''s Multi-Agent
  Architecture'
date: '2026-11-25'
source: https://dev.to/chethanramaswamy/how-uber-scaled-text-to-sql-to-12m-monthly-queries-inside-querygpts-multi-agent-architecture-592j
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-07-like-in-sql-explained-for-beginners]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]'
status: unread
---

> **TL;DR:** Most Text-to-SQL demos look impressive on a 5-table toy database and fall apart the moment they meet an enterprise data warehouse. The bottleneck isn't SQL syntax—it's context bloat, ambiguous domain boundaries, and trib…

## What’s new and why it matters
Most Text-to-SQL demos look impressive on a 5-table toy database and fall apart the moment they meet an enterprise data warehouse. The bottleneck isn't SQL syntax—it's context bloat, ambiguous domain boundaries, and tribal schema knowledge . In their engineering deep dive, QueryGPT – Natural Language to SQL Using Generative AI , Uber shared how they evolved a 2023 hackathon prototype through 20+ iterations into a production system serving ~1.2 million interactive queries per month (with Operations alone driving ~36% of volume), cutting average query authoring time from ~10 minutes down to ~3 m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/chethanramaswamy/how-uber-scaled-text-to-sql-to-12m-monthly-queries-inside-querygpts-multi-agent-architecture-592j

## Related notes
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-07-like-in-sql-explained-for-beginners]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-11-11-your-unique-constraint-in-postgresql-lets-duplicates-through-here-is-how-to-find-every-one]]
