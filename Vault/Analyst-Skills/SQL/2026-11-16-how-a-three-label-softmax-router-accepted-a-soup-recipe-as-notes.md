---
title: How a three-label softmax router accepted a soup recipe as notes
date: '2026-11-16'
source: https://dev.to/widechaos/how-a-three-label-softmax-router-accepted-a-soup-recipe-as-notes-104p
domain: SQL
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]'
- '[[2026-10-07-when-my-house-price-model-hit-100-accuracy-i-should-have-been-worried]]'
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]'
status: unread
---

> **TL;DR:** I kept this failure in the fixed commit bd2a30de287fe419b7d31838b40f5ae4d2d70061 . "Suggest a soup recipe." does not belong to weather, calendar, or notes, but the saved test prediction for ood-template-4-en has top_rout…

## What’s new and why it matters
I kept this failure in the fixed commit bd2a30de287fe419b7d31838b40f5ae4d2d70061 . "Suggest a soup recipe." does not belong to weather, calendar, or notes, but the saved test prediction for ood-template-4-en has top_route equal to notes, a maximum of 0.486, and accepted true at the 0.4 threshold. This package is small. It turns text into 4,096-dimensional character n-gram counts, applies a linear transform and three-way softmax, and was fit on 96 author-written training records for one 300-epoch CPU run. The 204 synthetic records split into 96 training, 54 validation, and 54 test; the original…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/widechaos/how-a-three-label-softmax-router-accepted-a-soup-recipe-as-notes-104p

## Related notes
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-10-30-count-accepted-jobs-not-successful-api-calls-when-comparing-ai-workflows]]
- [[2026-10-07-when-my-house-price-model-hit-100-accuracy-i-should-have-been-worried]]
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]
