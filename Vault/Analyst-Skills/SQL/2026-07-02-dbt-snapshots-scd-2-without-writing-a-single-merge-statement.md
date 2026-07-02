---
title: 'dbt Snapshots: SCD-2 Without Writing a Single MERGE Statement'
date: '2026-07-02'
source: https://dev.to/gowthampotureddi/dbt-snapshots-scd-2-without-writing-a-single-merge-statement-737
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]'
status: unread
---

> **TL;DR:** dbt snapshots are the declarative feature that quietly killed the hand-rolled SCD-2 MERGE statement — and the single piece of dbt infrastructure most senior analytics engineers inherit half-configured on the day someone…

## What’s new and why it matters
dbt snapshots are the declarative feature that quietly killed the hand-rolled SCD-2 MERGE statement — and the single piece of dbt infrastructure most senior analytics engineers inherit half-configured on the day someone asks "what did this customer's plan look like on the 14th of last month?" A scd type 2 dbt history table is the answer to every point-in-time question in a warehouse: what was the customer's tier when they placed that order, what was the discount rate at fulfilment time, what did the product catalog say the price was three revisions ago. Before dbt shipped snapshots, you built…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gowthampotureddi/dbt-snapshots-scd-2-without-writing-a-single-merge-statement-737

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-06-15-postgres-or-clickhouse-row-vs-column-storage-and-when-each-wins]]
