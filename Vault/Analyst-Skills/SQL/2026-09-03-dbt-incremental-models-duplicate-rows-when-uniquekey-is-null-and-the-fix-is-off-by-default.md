---
title: dbt Incremental Models Duplicate Rows When `unique_key` Is NULL — and the Fix
  Is Off by Default
date: '2026-09-03'
source: https://dev.to/eu_ti_f127c5b5d7535b7174f/dbt-incremental-models-duplicate-rows-when-uniquekey-is-null-and-the-fix-is-off-by-default-2pmd
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
status: unread
---

> **TL;DR:** You have an incremental model. It has a unique_key . You ran it twice on overlapping data, and the row count went up instead of staying flat: {{ config ( materialized = 'incremental' , unique_key = 'order_id' ) }} select…

## What’s new and why it matters
You have an incremental model. It has a unique_key . You ran it twice on overlapping data, and the row count went up instead of staying flat: {{ config ( materialized = 'incremental' , unique_key = 'order_id' ) }} select order_id , customer_id , status , updated_at from {{ source ( 'shop' , 'orders' ) }} { % if is_incremental () % } where updated_at > ( select max ( updated_at ) from {{ this }}) { % endif % } Most of the table updates correctly. A small, stubborn subset duplicates on every single run, and it is always the same rows. Check whether order_id is NULL in exactly those rows. It almo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/eu_ti_f127c5b5d7535b7174f/dbt-incremental-models-duplicate-rows-when-uniquekey-is-null-and-the-fix-is-off-by-default-2pmd

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
