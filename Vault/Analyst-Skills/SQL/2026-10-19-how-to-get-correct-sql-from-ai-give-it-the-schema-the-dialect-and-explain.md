---
title: 'How to get correct SQL from AI: give it the schema, the dialect, and EXPLAIN'
date: '2026-10-19'
source: https://dev.to/mars_peakul/how-to-get-correct-sql-from-ai-give-it-the-schema-the-dialect-and-explain-nfm
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]'
status: unread
---

> **TL;DR:** AI tools are genuinely good at writing SQL. Ask ChatGPT, Claude, Cursor or Claude Code for "monthly revenue per plan" and you'll have a query in seconds, and it will probably run. That's the problem. Wrong SQL rarely fai…

## What’s new and why it matters
AI tools are genuinely good at writing SQL. Ask ChatGPT, Claude, Cursor or Claude Code for "monthly revenue per plan" and you'll have a query in seconds, and it will probably run. That's the problem. Wrong SQL rarely fails loudly. It returns a number, and the number looks plausible. Here are the mistakes I see most often in AI-written SQL, why they happen, and the three inputs that fix most of them: the schema, the dialect, and the plan . Why the model gets it wrong The model isn't careless. It's missing information: It hasn't seen your schema, so it writes the column names that are usually th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/mars_peakul/how-to-get-correct-sql-from-ai-give-it-the-schema-the-dialect-and-explain-nfm

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-01-on-delete-set-null-vs-cascade-vs-restrict-in-postgresql-which-to-use]]
