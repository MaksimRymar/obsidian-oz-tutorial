---
title: 'Closing the Tax Gap with a Data Model: Invoice Traceability in SQL'
date: '2026-08-17'
source: https://dev.to/ricardo_demelo_2a17a8dd9/closing-the-tax-gap-with-a-data-model-invoice-traceability-in-sql-62i
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
status: unread
---

> **TL;DR:** The U.S. tax gap—the difference between taxes owed and taxes paid on time—runs about $696 billion a year, and most of it is underreported business income. To a policy analyst that is an enforcement problem. To anyone who…

## What’s new and why it matters
The U.S. tax gap—the difference between taxes owed and taxes paid on time—runs about $696 billion a year, and most of it is underreported business income. To a policy analyst that is an enforcement problem. To anyone who works with data, it looks like something more familiar: a join that never happens. There is no common key connecting the invoice a business issues, the payment it receives, and the amount it eventually reports. Each lives in its own silo—invoicing software, the bank feed, the tax workpapers—so when the three numbers disagree, nobody sees it until an audit reconstructs the year…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ricardo_demelo_2a17a8dd9/closing-the-tax-gap-with-a-data-model-invoice-traceability-in-sql-62i

## Related notes
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-06-10-sql-for-data-analysis-the-10-query-patterns-that-matter]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-06-13-top-12-sql-interview-problems-for-data-engineers-with-answers]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
