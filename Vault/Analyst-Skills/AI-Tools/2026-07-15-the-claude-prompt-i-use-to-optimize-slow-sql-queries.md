---
title: The Claude prompt I use to optimize slow SQL queries
date: '2026-07-15'
source: https://dev.to/razorphish/the-claude-prompt-i-use-to-optimize-slow-sql-queries-38ik
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-03-08-postgresql-query-optimization-10-techniques-that-actually-work]]'
- '[[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]'
- '[[2026-07-08-how-to-use-ai-to-write-sql-queries-from-plain-english]]'
- '[[2026-07-02-before-you-pick-an-azure-target-run-the-oracle-assessment-youre-probably-skipping]]'
- '[[2026-06-25-star-schema-vs-snowflake-schema-which-to-use-and-when]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** Here's the single Claude prompt I reach for most when a query is dragging. Optimize a slow SQL query Analyze and optimize this slow SQL query : [ paste query ] Context : - Table size : [ rows ] - Query frequency : [ per…

## What’s new and why it matters
Here's the single Claude prompt I reach for most when a query is dragging. Optimize a slow SQL query Analyze and optimize this slow SQL query : [ paste query ] Context : - Table size : [ rows ] - Query frequency : [ per second / minute ] - Current performance : [ ms ] -> Target : [ ms ] Suggest indexes , rewrites , and explain the trade - offs ( read speed vs . write cost ). Show EXPLAIN reasoning : what scans it eliminates . Use it when a query is slow and you are not sure whether the fix is an index, a rewrite, or a schema change. Asking for the EXPLAIN reasoning and the read-vs-write trade-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/razorphish/the-claude-prompt-i-use-to-optimize-slow-sql-queries-38ik

## Related notes
- [[2026-03-08-postgresql-query-optimization-10-techniques-that-actually-work]]
- [[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]
- [[2026-07-08-how-to-use-ai-to-write-sql-queries-from-plain-english]]
- [[2026-07-02-before-you-pick-an-azure-target-run-the-oracle-assessment-youre-probably-skipping]]
- [[2026-06-25-star-schema-vs-snowflake-schema-which-to-use-and-when]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
