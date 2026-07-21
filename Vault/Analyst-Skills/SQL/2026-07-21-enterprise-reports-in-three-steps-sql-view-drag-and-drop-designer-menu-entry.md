---
title: 'Enterprise reports in three steps: SQL view drag-and-drop designer menu entry'
date: '2026-07-21'
source: https://dev.to/wuicframework/building-reports-without-code-sql-view-to-mrt-to-printed-pdf-in-one-route-5bgj
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-05-15-oracle-fusion-vs-ebs-7-sql-patterns-every-bip-report-developer-needs]]'
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-06-18-how-to-query-your-database-in-plain-english-no-sql-required]]'
status: unread
---

> **TL;DR:** The reporting story in most enterprise apps goes like this: build a stored procedure, expose it via a custom controller, write a TypeScript service to call it, embed a Stimulsoft (or Crystal, or Telerik) viewer, manually…

## What’s new and why it matters
The reporting story in most enterprise apps goes like this: build a stored procedure, expose it via a custom controller, write a TypeScript service to call it, embed a Stimulsoft (or Crystal, or Telerik) viewer, manually wire the parameters, manually handle the per-user filter, manually validate the permissions. Multiply by 40 reports. Each one is a tiny project. The WUIC version: write a SQL view, scaffold it as a metadata route, lay the report out in the embedded designer (it saves into the route's folder for you), add a menu entry pointing at the route's report viewer. The framework picks i…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/wuicframework/building-reports-without-code-sql-view-to-mrt-to-printed-pdf-in-one-route-5bgj

## Related notes
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-05-15-oracle-fusion-vs-ebs-7-sql-patterns-every-bip-report-developer-needs]]
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-06-18-how-to-query-your-database-in-plain-english-no-sql-required]]
