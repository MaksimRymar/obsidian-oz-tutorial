---
title: How I Added dbt Cloud to Coral — My Open Source Hackathon Journey
date: '2026-05-28'
source: https://dev.to/gaurang_bhatt_b6d91a19879/how-i-added-dbt-cloud-to-coral-my-open-source-hackathon-journey-4gg3
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-05-19-stop-writing-ugly-sql-a-developers-guide-to-clean-readable-queries]]'
- '[[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]'
- '[[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]'
- '[[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]'
status: unread
---

> **TL;DR:** What is Coral? Coral is an open-source tool that lets you query any API, database, or file as SQL — no ETL, no warehouse, no glue code. The Problem I Solved dbt Cloud is used by thousands of data engineers. But there was…

## What’s new and why it matters
What is Coral? Coral is an open-source tool that lets you query any API, database, or file as SQL — no ETL, no warehouse, no glue code. The Problem I Solved dbt Cloud is used by thousands of data engineers. But there was no way to query dbt Cloud jobs, runs, and environments via SQL. I built that. What I Built PR #627 — dbt Cloud Community Source Added 3 tables to Coral: dbt_cloud.jobs — all jobs with schedules and state dbt_cloud.runs — run history with status codes dbt_cloud.environments — deployment environments The Code # manifest.yaml (simplified) name : dbt_cloud backend : http tables :…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gaurang_bhatt_b6d91a19879/how-i-added-dbt-cloud-to-coral-my-open-source-hackathon-journey-4gg3

## Related notes
- [[2026-05-19-stop-writing-ugly-sql-a-developers-guide-to-clean-readable-queries]]
- [[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]
- [[2026-04-11-master-mysql-views-and-window-functions-advanced-query-optimization-guide]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-05-01-i-built-a-vs-code-extension-to-debug-mysql-queries-step-by-step]]
- [[2026-05-04-why-we-chose-self-hosted-ai-over-cloud-for-business-data-posted-by-the-ragleap-team-building-ragleap-a-private-server-ai]]
