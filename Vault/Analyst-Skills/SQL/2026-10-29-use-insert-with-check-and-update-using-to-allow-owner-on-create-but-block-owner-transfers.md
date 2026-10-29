---
title: Use INSERT WITH CHECK and UPDATE USING to allow owner-on-create but block owner
  transfers
date: '2026-10-29'
source: https://dev.to/chriserodriguez/use-insert-with-check-and-update-using-to-allow-owner-on-create-but-block-owner-transfers-49ie
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
related:
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-09-02-why-serverless-engineers-already-understand-containers]]'
- '[[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]'
- '[[2026-08-04-sqlazymerge-multiple-tables-into-single-rows-by-common-id]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-06-15-cross-row-validation-risk-in-postgresql-check-constraints]]'
status: unread
---

> **TL;DR:** Problem and goal You want a table where callers can create rows that name themselves as owner, may edit other fields on rows they own, and must never transfer ownership via UPDATE. The trick is enforcing different rules…

## What’s new and why it matters
Problem and goal You want a table where callers can create rows that name themselves as owner, may edit other fields on rows they own, and must never transfer ownership via UPDATE. The trick is enforcing different rules at creation time and at modification time. How PostgreSQL helps Row-level security separates selection and storage checks into USING and WITH CHECK. INSERT policies run WITH CHECK (they validate the proposed row). UPDATE policies can include both USING (which decides which existing rows the caller may target) and WITH CHECK (which validates the post-update row). That split is e…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/chriserodriguez/use-insert-with-check-and-update-using-to-allow-owner-on-create-but-block-owner-transfers-49ie

## Related notes
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-09-02-why-serverless-engineers-already-understand-containers]]
- [[2026-06-12-indexes-quickstart-using-postgresql-15-sec-read]]
- [[2026-08-04-sqlazymerge-multiple-tables-into-single-rows-by-common-id]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-06-15-cross-row-validation-risk-in-postgresql-check-constraints]]
