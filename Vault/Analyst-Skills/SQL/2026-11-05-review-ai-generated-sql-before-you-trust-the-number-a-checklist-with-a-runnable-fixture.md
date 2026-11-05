---
title: 'Review AI-generated SQL before you trust the number: a checklist with a runnable
  fixture'
date: '2026-11-05'
source: https://dev.to/prachitparikh/review-ai-generated-sql-before-you-trust-the-number-a-checklist-with-a-runnable-fixture-2j45
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#presentations'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-10-22-sql-ties-python-at-58-what-it-means-for-data-engineer-interviews]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
status: unread
---

> **TL;DR:** Photo by Chris Ried on Unsplash (Unsplash License). A query that runs is not a query that's right. Most of us know this, and few of us act on it when an assistant hands back a query in four seconds and the number looks a…

## What’s new and why it matters
Photo by Chris Ried on Unsplash (Unsplash License). A query that runs is not a query that's right. Most of us know this, and few of us act on it when an assistant hands back a query in four seconds and the number looks about right. This is the review I run on AI-written SQL before its number goes anywhere near a sign-off. Eight checks, each written as a query that returns rows only when something is wrong. It comes with a tiny fictional fixture you can paste into SQLite, where a perfectly plausible revenue query returns 1,820 and the reviewed one returns 825 . Same tables, same question, same…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/prachitparikh/review-ai-generated-sql-before-you-trust-the-number-a-checklist-with-a-runnable-fixture-2j45

## Related notes
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-10-22-sql-ties-python-at-58-what-it-means-for-data-engineer-interviews]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
