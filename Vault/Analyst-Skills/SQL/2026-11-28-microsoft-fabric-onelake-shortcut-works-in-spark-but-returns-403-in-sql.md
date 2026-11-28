---
title: Microsoft Fabric OneLake Shortcut Works in Spark but Returns 403 in SQL
date: '2026-11-28'
source: https://dev.to/ultimateinfoguide/microsoft-fabric-onelake-shortcut-works-in-spark-but-returns-403-in-sql-1k95
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]'
- '[[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]'
- '[[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]'
status: unread
---

> **TL;DR:** OneLake shortcut works in Spark but returns 403 in SQL? Check table sync and endpoint identity first. Quick answer: If the table is missing from the SQL explorer, check the shortcut location and metadata sync. If the tab…

## What’s new and why it matters
OneLake shortcut works in Spark but returns 403 in SQL? Check table sync and endpoint identity first. Quick answer: If the table is missing from the SQL explorer, check the shortcut location and metadata sync. If the table is visible but the query is denied, start with endpoint identity and permissions. A successful Spark read only tells you that the Spark read path worked. Still blocked? Open the full OneLake shortcut 403 checklist on UltimateInfoGuide . It also covers cross-workspace and external-storage shortcuts. Run the two checks as the affected user For this example, a consumer lakehous…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ultimateinfoguide/microsoft-fabric-onelake-shortcut-works-in-spark-but-returns-403-in-sql-1k95

## Related notes
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]
- [[2026-10-11-your-first-sql-query-can-work-before-you-understand-it]]
- [[2026-06-08-running-real-sql-on-dynamodb-how-it-actually-works]]
