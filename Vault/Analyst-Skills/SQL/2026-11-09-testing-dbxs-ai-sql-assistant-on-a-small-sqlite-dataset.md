---
title: Testing DBX's AI SQL Assistant on a Small SQLite Dataset
date: '2026-11-09'
source: https://dev.to/david_xiao_cf79e6c879b2ae/testing-dbxs-ai-sql-assistant-on-a-small-sqlite-dataset-3jk0
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]'
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
status: unread
---

> **TL;DR:** Can an AI SQL assistant preserve a filtering rule when you add a condition in a follow-up? I tried a small case in DBX: total each customer's completed orders, then keep only customers whose total is strictly greater tha…

## What’s new and why it matters
Can an AI SQL assistant preserve a filtering rule when you add a condition in a follow-up? I tried a small case in DBX: total each customer's completed orders, then keep only customers whose total is strictly greater than 30,000 cents. Both generated queries returned the expected results without manual SQL edits. That is a useful observation, but it covers just two prompts against a database with three fictional customers and six orders. Here is the setup, the SQL, and the parts of the interface that needed attention. What was tested Item Setup Test dates November 6, 2026: basic SQLite workflo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/david_xiao_cf79e6c879b2ae/testing-dbxs-ai-sql-assistant-on-a-small-sqlite-dataset-3jk0

## Related notes
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-09-29-sql-joins-how-to-combine-tables-the-right-way]]
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
