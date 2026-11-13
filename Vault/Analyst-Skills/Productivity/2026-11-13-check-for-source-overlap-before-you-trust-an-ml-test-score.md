---
title: Check for source overlap before you trust an ML test score
date: '2026-11-13'
source: https://dev.to/nanchuangresearch/check-for-source-overlap-before-you-trust-an-ml-test-score-288f
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-11-11-catch-unexpected-missing-value-codes-in-a-research-csv]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-10-29-use-insert-with-check-and-update-using-to-allow-owner-on-create-but-block-owner-transfers]]'
status: unread
---

> **TL;DR:** A dataset can have unique row IDs and still leak. For example, a microscopy image might be exported as several crops. A row-level random split can then put crops from the same source image in both train and test. The exp…

## What’s new and why it matters
A dataset can have unique row IDs and still leak. For example, a microscopy image might be exported as several crops. A row-level random split can then put crops from the same source image in both train and test. The experiment would measure performance on partly familiar sources. Keep a group ID that reflects the unit you want to generalize to. Depending on your study, that might be the original image, device, site, or participant. Decide which unit matters before assigning splits. For prospective use, record the time cutoff as well. Here is a runnable Python check using synthetic split rows.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nanchuangresearch/check-for-source-overlap-before-you-trust-an-ml-test-score-288f

## Related notes
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-11-11-catch-unexpected-missing-value-codes-in-a-research-csv]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-08-31-how-to-reconcile-two-tables-in-sql-when-the-row-counts-match]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-10-29-use-insert-with-check-and-update-using-to-allow-owner-on-create-but-block-owner-transfers]]
