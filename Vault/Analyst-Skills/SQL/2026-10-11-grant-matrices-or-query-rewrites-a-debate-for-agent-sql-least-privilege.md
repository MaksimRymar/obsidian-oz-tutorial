---
title: 'Grant Matrices or Query Rewrites: A Debate for Agent SQL Least Privilege'
date: '2026-10-11'
source: https://dev.to/dataio_4921/grant-matrices-or-query-rewrites-a-debate-for-agent-sql-least-privilege-3db9
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]'
- '[[2026-09-15-parse-sql-migrations-into-a-column-reference-then-sign-retention-and-pii-outside-the-model]]'
- '[[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]'
status: unread
---

> **TL;DR:** This account previously published a night-shift story about an agent query that locked a production table. The lock was the visible failure, but the missing debate was which privilege path allowed the statement to run at…

## What’s new and why it matters
This account previously published a night-shift story about an agent query that locked a production table. The lock was the visible failure, but the missing debate was which privilege path allowed the statement to run at all. A reporting agent can still ask for a temporary superuser role when a narrower view would answer the question. Reviewers need an explicit rule before they choose between a new grant and a query rewrite. Why least privilege is the debate Recent developer discussion has stressed that model quality can improve while the surrounding software controls stay unchanged. That sign…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/dataio_4921/grant-matrices-or-query-rewrites-a-debate-for-agent-sql-least-privilege-3db9

## Related notes
- [[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]
- [[2026-09-15-parse-sql-migrations-into-a-column-reference-then-sign-retention-and-pii-outside-the-model]]
- [[2026-08-14-why-ai-generated-migrations-need-a-different-gate-than-code-patches]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-31-temp-table-vs-view-in-sql-a-saved-answer-or-a-saved-question]]
