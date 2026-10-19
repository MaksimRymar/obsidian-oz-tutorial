---
title: Three-way reconciliation as a data integrity check for law firm trust accounts
date: '2026-10-19'
source: https://dev.to/damin_mutti_e213ac1a11bf4/three-way-reconciliation-as-a-data-integrity-check-for-law-firm-trust-accounts-2ln8
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-09-09-six-tables-out-of-260]]'
status: unread
---

> **TL;DR:** A three-way trust reconciliation compares the trust bank statement's closing balance, the trust liability in the general ledger, and the sum of the per-client trust ledgers. All three must be equal at month end. Treated…

## What’s new and why it matters
A three-way trust reconciliation compares the trust bank statement's closing balance, the trust liability in the general ledger, and the sum of the per-client trust ledgers. All three must be equal at month end. Treated as data, it's an invariant across three independent sources, and when one disagrees, the pattern of who disagrees tells you which record is bad. Most state bars expect this check monthly, and the rules vary by state, so read this as a data model, not legal advice. I run ZeraBooks, and this is how we think about the books side of it. Figures are made up. Separate the money in th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/damin_mutti_e213ac1a11bf4/three-way-reconciliation-as-a-data-integrity-check-for-law-firm-trust-accounts-2ln8

## Related notes
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-13-snowflake-sql-patterns-for-revenue-reporting]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-09-09-six-tables-out-of-260]]
