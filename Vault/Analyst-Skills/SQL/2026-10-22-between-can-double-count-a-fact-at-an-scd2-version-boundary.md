---
title: BETWEEN can double-count a fact at an SCD2 version boundary
date: '2026-10-22'
source: https://dev.to/antony502189max/between-can-double-count-a-fact-at-an-scd2-version-boundary-42a6
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-21-free-sql-practice-why-sumdistinct-doesnt-fix-inflated-payment-totals]]'
- '[[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-10-22-a-single-sql-constraint-can-save-your-database-from-bad-data-do-you-know-which-one]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]'
status: unread
---

> **TL;DR:** A customer changes tier at midnight. A payment happens at exactly that instant. A historical join returns the payment twice: once under the old tier and once under the new one. This can happen even when the history has n…

## What’s new and why it matters
A customer changes tier at midnight. A payment happens at exactly that instant. A historical join returns the payment twice: once under the old tier and once under the new one. This can happen even when the history has no duplicate change records. An inclusive upper boundary is enough. Put a fact on the boundary Assume the following effective changes for customer c. They arrive in this order: basic, effective January 1 premium, effective January 3 plus, effective January 2 The third change arrives late. Once all three changes are known, the valid-time history is: Tier Valid from, inclusive Val…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/antony502189max/between-can-double-count-a-fact-at-an-scd2-version-boundary-42a6

## Related notes
- [[2026-10-21-free-sql-practice-why-sumdistinct-doesnt-fix-inflated-payment-totals]]
- [[2026-09-29-the-not-in-trap-why-your-sql-query-returns-zero-rows]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-10-22-a-single-sql-constraint-can-save-your-database-from-bad-data-do-you-know-which-one]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-08-05-reconstructing-wallet-journeys-across-dex-frontends-one-chain-at-a-time]]
