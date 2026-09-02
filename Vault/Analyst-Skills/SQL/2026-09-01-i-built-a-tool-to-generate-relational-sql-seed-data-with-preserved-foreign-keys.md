---
title: I built a tool to generate relational SQL seed data with preserved foreign
  keys.
date: '2026-09-01'
source: https://dev.to/dhanush_gowda_f54b58cdea6/i-built-a-tool-to-generate-relational-sql-seed-data-with-preserved-foreign-keys-kia
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-how-to-choose-the-right-sql-database-for-your-project]]'
- '[[2026-08-17-why-i-built-seedsql-generating-schema-aware-synthetic-data-without-leaking-pii]]'
- '[[2026-07-02-generate-insert-statements-from-excel-bulk-sql-script-export]]'
- '[[2026-03-30-dataai-a-local-ai-database-client-from-plain-language-to-executable-sql]]'
- '[[2026-04-20-sql-vs-nosql-a-decision-framework-that-actually-works]]'
- '[[2026-08-10-why-uuid-v4-is-killing-your-database-indexes-and-how-uuid-v7-fixes-it]]'
status: unread
---

> **TL;DR:** Hand-writing mock SQL data for local testing is slow, and using LLMs breaks down when you need thousands of rows with strict relational constraints. To solve this, I built SeedSQL—a free tool to generate referentially ac…

## What’s new and why it matters
Hand-writing mock SQL data for local testing is slow, and using LLMs breaks down when you need thousands of rows with strict relational constraints. To solve this, I built SeedSQL—a free tool to generate referentially accurate synthetic data in seconds. Why I Built ItMocking local database schemas usually causes three main headaches: Broken Foreign Keys: Standard generators treat tables independently, creating orphaned relationships (Users $\rightarrow$ Orders). AI Limits: Prompting LLMs for large datasets gets slow, hits token caps, and yields non-deterministic outputs. Formatting Hassles: Cl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dhanush_gowda_f54b58cdea6/i-built-a-tool-to-generate-relational-sql-seed-data-with-preserved-foreign-keys-kia

## Related notes
- [[2026-06-15-how-to-choose-the-right-sql-database-for-your-project]]
- [[2026-08-17-why-i-built-seedsql-generating-schema-aware-synthetic-data-without-leaking-pii]]
- [[2026-07-02-generate-insert-statements-from-excel-bulk-sql-script-export]]
- [[2026-03-30-dataai-a-local-ai-database-client-from-plain-language-to-executable-sql]]
- [[2026-04-20-sql-vs-nosql-a-decision-framework-that-actually-works]]
- [[2026-08-10-why-uuid-v4-is-killing-your-database-indexes-and-how-uuid-v7-fixes-it]]
