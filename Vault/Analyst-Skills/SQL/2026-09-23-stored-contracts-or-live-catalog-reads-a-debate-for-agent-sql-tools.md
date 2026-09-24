---
title: 'Stored Contracts or Live Catalog Reads: A Debate for Agent SQL Tools'
date: '2026-09-23'
source: https://dev.to/dataio_4921/stored-contracts-or-live-catalog-reads-a-debate-for-agent-sql-tools-3hd9
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-07-workshop-validate-tool-results-before-they-enter-agent-memory-in-75-minutes]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-09-09-diagnostic-findings-or-auto-rewrites-a-gate-for-sql-review-agents]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]'
status: unread
---

> **TL;DR:** A reconstructed agent-SQL incident usually starts with a quiet catalog query rather than a dramatic production lock. The agent lists columns from information_schema , then writes a join that looks syntactically polite to…

## What’s new and why it matters
A reconstructed agent-SQL incident usually starts with a quiet catalog query rather than a dramatic production lock. The agent lists columns from information_schema , then writes a join that looks syntactically polite to reviewers. That join still touches a relation the product owner never intended to expose through the agent role. The failure is an interface design choice, not merely a weak language-model sample. Teams that let models reach PostgreSQL tend to land on one of two tool designs. The first design publishes a small set of stored contracts and refuses any other statement text. The s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataio_4921/stored-contracts-or-live-catalog-reads-a-debate-for-agent-sql-tools-3hd9

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-07-workshop-validate-tool-results-before-they-enter-agent-memory-in-75-minutes]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-09-09-diagnostic-findings-or-auto-rewrites-a-gate-for-sql-review-agents]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-08-14-schema-linting-vs-migration-linting-which-database-problems-each-one-can-see]]
