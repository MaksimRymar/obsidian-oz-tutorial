---
title: 'Joining datasets that never shared a key: validate CIN, LEI and Wikidata IDs,
  then resolve them in Python'
date: '2026-10-24'
source: https://dev.to/datagalactica/joining-datasets-that-never-shared-a-key-validate-cin-lei-and-wikidata-ids-then-resolve-them-in-4jik
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-23-verify-a-company-by-name-in-3-api-calls-curl-python]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-13-recursive-ctes-how-sql-secretly-learned-to-loop]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
status: unread
---

> **TL;DR:** Sunny Mittal works on marketing at Data Galactica. Corrections welcome in the comments. You have three spreadsheets about the same companies. Finance keyed them by Indian CIN, the treasury team by LEI, and the research t…

## What’s new and why it matters
Sunny Mittal works on marketing at Data Galactica. Corrections welcome in the comments. You have three spreadsheets about the same companies. Finance keyed them by Indian CIN, the treasury team by LEI, and the research team pulled theirs from Wikidata, so every row has a Q-id. None of them shares a column you can join on. This post shows a small Python pipeline that (1) validates each identifier locally, so you don't pay to look up typos, and (2) resolves the survivors to one permanent key. Step 1: know what a valid identifier looks like Most bad joins start with bad IDs: a trailing space, a l…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/datagalactica/joining-datasets-that-never-shared-a-key-validate-cin-lei-and-wikidata-ids-then-resolve-them-in-4jik

## Related notes
- [[2026-10-23-verify-a-company-by-name-in-3-api-calls-curl-python]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-13-recursive-ctes-how-sql-secretly-learned-to-loop]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
