---
title: 'Canada''s open baby-food data: a 1000x unit label, a 10x table slip, and lead
  vs the FDA''s action levels'
date: '2026-10-30'
source: https://dev.to/munimv2/canadas-open-baby-food-data-a-1000x-unit-label-a-10x-table-slip-and-lead-vs-the-fdas-action-1492
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
related:
- '[[2026-10-21-the-number-theory-law-i-stumbled-into-turned-out-to-be-additive----two-independent-defects-add-up-exactly]]'
- '[[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]'
- '[[2026-10-25-do-popular-pypi-packages-rely-on-os-independent-no-the-long-tail-does-81-vs-72-the-head-names-real-platforms]]'
- '[[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
status: unread
---

> **TL;DR:** The Canadian Food Inspection Agency (CFIA) tests food for infants and children every year in its Children's Food Project, and it publishes one per-sample CSV per year on open.canada.ca, next to a report page with printed…

## What’s new and why it matters
The Canadian Food Inspection Agency (CFIA) tests food for infants and children every year in its Children's Food Project, and it publishes one per-sample CSV per year on open.canada.ca, next to a report page with printed tables. That is rare and valuable: anyone can check the printed numbers against the raw data. So we did, for aflatoxin M1 (a mould toxin that reaches milk) in six years of files, and for lead in six more. Every check was pre-registered: the predictions and the grading code were public on GitHub before any result value was read. A sealed compute job then graded them on SHA-256-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/munimv2/canadas-open-baby-food-data-a-1000x-unit-label-a-10x-table-slip-and-lead-vs-the-fdas-action-1492

## Related notes
- [[2026-10-21-the-number-theory-law-i-stumbled-into-turned-out-to-be-additive----two-independent-defects-add-up-exactly]]
- [[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]
- [[2026-10-25-do-popular-pypi-packages-rely-on-os-independent-no-the-long-tail-does-81-vs-72-the-head-names-real-platforms]]
- [[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
