---
title: 'Acacia DB for VS Code: Map your database usage in source code (1.0.0 1.2.0)'
date: '2026-04-30'
source: https://dev.to/acaciaman/acacia-db-for-vs-code-map-your-database-usage-in-source-code-100-120-93a
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-09-i-built-an-mcp-server-that-lets-claude-control-my-kubernetes-cluster]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-16-real-time-sql-analysis-in-vs-code-catch-dangerous-queries-before-you-save-the-file]]'
- '[[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]'
status: unread
---

> **TL;DR:** If you've ever inherited a legacy system and asked "which tables are actually used, where, and how do they connect?" — that's the question Acacia DB tries to answer. It's a VS Code extension that scans your workspace for…

## What’s new and why it matters
If you've ever inherited a legacy system and asked "which tables are actually used, where, and how do they connect?" — that's the question Acacia DB tries to answer. It's a VS Code extension that scans your workspace for references to database tables and columns, then turns the raw matches into something you can navigate, rank, and diagram. No LLMs, no cloud calls — just a deterministic pipeline over your source tree and a tables_views.json schema file. The last three releases (1.0.0, 1.1.0, 1.2.0) reshaped the extension from a workspace scanner into a small analysis suite. Here's what landed.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/acaciaman/acacia-db-for-vs-code-map-your-database-usage-in-source-code-100-120-93a

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-09-i-built-an-mcp-server-that-lets-claude-control-my-kubernetes-cluster]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-16-real-time-sql-analysis-in-vs-code-catch-dangerous-queries-before-you-save-the-file]]
- [[2026-03-02-database-indexing-explained-how-to-make-your-queries-1000x-faster]]
