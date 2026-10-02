---
title: Your RLS policy returns zero rows. The view next to it returns two.
date: '2026-10-02'
source: https://dev.to/ashish_sinha_5241c7673d93/your-rls-policy-returns-zero-rows-the-view-next-to-it-returns-two-e9n
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-13-recursive-ctes-how-sql-secretly-learned-to-loop]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-15-vanna-is-archived-the-failure-mode-none-of-the-replacements-fix]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
status: unread
---

> **TL;DR:** I have a row-level security policy that denies a user every row in a table. The user queries the table and gets nothing, which is right. The user queries a view over that same table and gets real salary data back. This i…

## What’s new and why it matters
I have a row-level security policy that denies a user every row in a table. The user queries the table and gets nothing, which is right. The user queries a view over that same table and gets real salary data back. This is documented PostgreSQL behaviour, not a bug, and it is six years older than the option that fixes it. I went looking for it because I write a library that decides which tables to show a language model, and I wanted to know whether "you don't have the grant" was the same as "you can't read it". It isn't. Here is the whole thing, on PostgreSQL 16.13. Paste it into a scratch data…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ashish_sinha_5241c7673d93/your-rls-policy-returns-zero-rows-the-view-next-to-it-returns-two-e9n

## Related notes
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-13-recursive-ctes-how-sql-secretly-learned-to-loop]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-15-vanna-is-archived-the-failure-mode-none-of-the-replacements-fix]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
