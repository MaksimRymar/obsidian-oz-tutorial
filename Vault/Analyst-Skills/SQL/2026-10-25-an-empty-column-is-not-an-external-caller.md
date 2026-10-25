---
title: An Empty Column Is Not an External Caller
date: '2026-10-25'
source: https://dev.to/minia2a/an-empty-column-is-not-an-external-caller-1hj2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]'
status: unread
---

> **TL;DR:** An Empty Column Is Not an External Caller 2026-10-25 · data report Every delivery through the gateway writes one row: which service, which path kind, who called it, what came back, and who was at fault when something fai…

## What’s new and why it matters
An Empty Column Is Not an External Caller 2026-10-25 · data report Every delivery through the gateway writes one row: which service, which path kind, who called it, what came back, and who was at fault when something failed. The table is the only place we can answer "do agents actually use this?" without counting HTTP requests, which — as we wrote earlier — are mostly crawlers. This week I ran that table to find our most-used endpoints by real external callers. The first query returned a clean, plausible answer. It was wrong, and it was wrong in a way that is worth writing down because the mis…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/minia2a/an-empty-column-is-not-an-external-caller-1hj2

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-09-30-a-select-that-returned-more-rows-than-its-limit]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]
