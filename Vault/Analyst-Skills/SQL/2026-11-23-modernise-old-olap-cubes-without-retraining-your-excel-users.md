---
title: Modernise old OLAP cubes without retraining your Excel users
date: '2026-11-23'
source: https://dev.to/sergeisemenkov/modernise-old-olap-cubes-without-retraining-your-excel-users-3lp2
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tableau'
related:
- '[[2026-11-04-i-gave-ai-agents-a-video-downloader-building-a-remote-mcp-server-in-python]]'
- '[[2026-10-20-letting-ai-agents-query-my-databases-without-ever-giving-them-the-credentials]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-10-12-introducing-sqlsift-schema-aware-static-analysis-for-sql-no-database-needed]]'
- '[[2026-03-31-ai-agent-for-data-analysis-automate-reports-dashboards-amp-insights-2026]]'
- '[[2026-10-27-ai-agents-can-run-sql-now-where-should-database-teams-draw-the-line]]'
status: unread
---

> **TL;DR:** Your reporting runs on old OLAP cubes, and nobody wants to maintain the server under them. eMondrian replaces it with an open-source semantic layer that speaks the same language as the cubes: an MDX/XMLA endpoint . Excel…

## What’s new and why it matters
Your reporting runs on old OLAP cubes, and nobody wants to maintain the server under them. eMondrian replaces it with an open-source semantic layer that speaks the same language as the cubes: an MDX/XMLA endpoint . Excel connects to it the way it connects to Analysis Services, so your users keep their PivotTables, their hierarchies and their measures, and work the way they always have. The data moves to ClickHouse or another SQL database that you already know how to run. What stays the same for Excel users The same connection. Excel uses its built-in From Analysis Services connection. Nothing…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/sergeisemenkov/modernise-old-olap-cubes-without-retraining-your-excel-users-3lp2

## Related notes
- [[2026-11-04-i-gave-ai-agents-a-video-downloader-building-a-remote-mcp-server-in-python]]
- [[2026-10-20-letting-ai-agents-query-my-databases-without-ever-giving-them-the-credentials]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-10-12-introducing-sqlsift-schema-aware-static-analysis-for-sql-no-database-needed]]
- [[2026-03-31-ai-agent-for-data-analysis-automate-reports-dashboards-amp-insights-2026]]
- [[2026-10-27-ai-agents-can-run-sql-now-where-should-database-teams-draw-the-line]]
