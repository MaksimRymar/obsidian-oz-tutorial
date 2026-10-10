---
title: What 6,000 Pharmacy Transactions Taught Me About Discounts
date: '2026-10-09'
source: https://dev.to/code_with_mwai/what-6000-pharmacy-transactions-taught-me-about-discounts-187h
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tableau'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** A 25% discount cut this pharmacy's margin from 31% to 8% and did not sell a single extra unit per order. That was the clearest finding from a project I built on 6,000 transactions from a multi-branch Kenyan retail pharma…

## What’s new and why it matters
A 25% discount cut this pharmacy's margin from 31% to 8% and did not sell a single extra unit per order. That was the clearest finding from a project I built on 6,000 transactions from a multi-branch Kenyan retail pharmacy, running from a raw CSV through PostgreSQL to a Power BI dashboard. The finding is useful. The way I got to it is the part I want to write about. Before any chart reached the dashboard, the SQL behind it had to reconcile to the raw data to the last shilling. That habit shaped every decision in the project, and it is the main thing I'd want another analyst to take from this a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/code_with_mwai/what-6000-pharmacy-transactions-taught-me-about-discounts-187h

## Related notes
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
