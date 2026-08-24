---
title: Three Severity Levels, Not Pass/Fail — and Why Severity Decides Where the Rule
  Lives
date: '2026-08-23'
source: https://dev.to/marcus1968/three-severity-levels-not-passfail-and-why-severity-decides-where-the-rule-lives-ecn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-07-16-checking-data-quality-with-sql-a-configurable-framework-for-spotting-bad-data-generically]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-08-16-review-sql-migrations-in-30-seconds-seed-migrate-compare]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Most data quality systems don't die of bad checks. They die of a missing field in the rule model: the severity. A missing country code in three out of 80,000 rows blocks the nightly load, someone switches the check off "…

## What’s new and why it matters
Most data quality systems don't die of bad checks. They die of a missing field in the rule model: the severity. A missing country code in three out of 80,000 rows blocks the nightly load, someone switches the check off "temporarily", and from that moment everything runs unchecked. Steering data quality with severity levels instead of binary pass/fail escapes that trap. And severity can do more: it decides whether a rule belongs in the target schema as a constraint or in the pipeline. Key takeaways: Binary pass/fail ends in one of two dead ends: either a triviality blocks the whole load, or eve…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/marcus1968/three-severity-levels-not-passfail-and-why-severity-decides-where-the-rule-lives-ecn

## Related notes
- [[2026-07-16-checking-data-quality-with-sql-a-configurable-framework-for-spotting-bad-data-generically]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-08-16-review-sql-migrations-in-30-seconds-seed-migrate-compare]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
