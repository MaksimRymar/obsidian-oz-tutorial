---
title: Your annual salary median can mix currencies and pay types
date: '2026-11-08'
source: https://dev.to/dataspryva/your-annual-salary-median-can-mix-currencies-and-pay-types-18l2
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]'
- '[[2026-11-05-224-new-remote-jobs-in-twelve-days-thirty-one-were-posted-in-the-last-24-hours]]'
- '[[2026-06-08-retention-cohort-analysis-with-plain-sql]]'
- '[[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]'
status: unread
---

> **TL;DR:** Your remote-pay chart can have a perfectly valid median and no coherent unit. You're about to put salaryAnnualMin on a slide comparing roles. The column name suggests the awkward conversion work is finished, which is a c…

## What’s new and why it matters
Your remote-pay chart can have a perfectly valid median and no coherent unit. You're about to put salaryAnnualMin on a slide comparing roles. The column name suggests the awkward conversion work is finished, which is a comforting thought until someone asks what the numbers actually measure. Annualised salary fields standardise time, not currency or compensation type. The Actor's salary filters compare published annualised amounts without converting currencies, while salaryType distinguishes base , ote , total-comp and hourly . That median needs more than a successful numeric cast. What does a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dataspryva/your-annual-salary-median-can-mix-currencies-and-pay-types-18l2

## Related notes
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]
- [[2026-11-05-224-new-remote-jobs-in-twelve-days-thirty-one-were-posted-in-the-last-24-hours]]
- [[2026-06-08-retention-cohort-analysis-with-plain-sql]]
- [[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]
