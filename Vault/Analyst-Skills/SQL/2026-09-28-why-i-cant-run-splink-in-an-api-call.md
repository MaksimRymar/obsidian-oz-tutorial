---
title: Why I can't run Splink in an API call
date: '2026-09-28'
source: https://dev.to/hannune/why-i-cant-run-splink-in-an-api-call-4gm8
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-06-25-what-actually-happens-when-you-type-what-is-python-into-chatgpt]]'
status: unread
---

> **TL;DR:** I got confused about this for longer than I expected. The 2asy.ai news pipeline uses Splink. Company mentions come in with each article batch, Splink runs pairwise comparison against everything already in the registry, c…

## What’s new and why it matters
I got confused about this for longer than I expected. The 2asy.ai news pipeline uses Splink. Company mentions come in with each article batch, Splink runs pairwise comparison against everything already in the registry, clusters form, the registry updates. Usually takes about 90 seconds. Sometimes longer. Nobody is waiting for it. When I started building the ER API, I thought the API would just be a lighter version of that. Call Splink, get a match, return it. The response latency problem hit me within the first day of prototyping. Splink's actual comparison work involves blocking across the fu…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/hannune/why-i-cant-run-splink-in-an-api-call-4gm8

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-06-25-what-actually-happens-when-you-type-what-is-python-into-chatgpt]]
