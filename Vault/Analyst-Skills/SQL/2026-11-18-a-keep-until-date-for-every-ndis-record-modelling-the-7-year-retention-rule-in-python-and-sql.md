---
title: 'A keep-until date for every NDIS record: modelling the 7-year retention rule
  in Python and SQL'
date: '2026-11-18'
source: https://dev.to/rostery/a-keep-until-date-for-every-ndis-record-modelling-the-7-year-retention-rule-in-python-and-sql-2ooa
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tableau'
- '#tool'
- '#tutorial'
related:
- '[[2026-11-16-modelling-the-ndis-90-day-claim-limit-in-python-day-counts-working-day-deadlines-and-a-slack-score-for-every-unpaid-line]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]'
status: unread
---

> **TL;DR:** Originally based on our guide to NDIS record keeping and the 7-year rule on rostery.com.au. This version is rewritten for developers, data people and anyone who looks after the systems that hold NDIS records. General inf…

## What’s new and why it matters
Originally based on our guide to NDIS record keeping and the 7-year rule on rostery.com.au. This version is rewritten for developers, data people and anyone who looks after the systems that hold NDIS records. General information only, not legal advice. The date arithmetic and a few edge cases below are our reading of the Act; the NDIA hasn't published guidance on them. Australia's National Disability Insurance Scheme (NDIS) pays providers for supports delivered to participants. In August 2026 Parliament added a new section 45B to the NDIS Act, which tells a provider how long to keep the record…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rostery/a-keep-until-date-for-every-ndis-record-modelling-the-7-year-retention-rule-in-python-and-sql-2ooa

## Related notes
- [[2026-11-16-modelling-the-ndis-90-day-claim-limit-in-python-day-counts-working-day-deadlines-and-a-slack-score-for-every-unpaid-line]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-08-22-where-to-get-a-sample-database-to-practice-sql-and-how-to-check-it-loaded]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]
