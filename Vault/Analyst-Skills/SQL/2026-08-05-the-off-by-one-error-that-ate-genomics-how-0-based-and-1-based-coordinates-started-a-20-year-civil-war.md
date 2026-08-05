---
title: 'The off-by-one error that ate genomics: how 0 based and 1 based coordinates
  started a 20-year civil war'
date: '2026-08-05'
source: https://dev.to/nadiabaig/the-off-by-one-error-that-ate-genomics-how-0-based-and-1-based-coordinates-started-a-20-year-civil-2lhb
domain: SQL
relevance: 🟡
tags:
- '#career'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-05-19-in-some-scenarios-relying-on-llms-to-generate-sql-is-neither-rigorous-nor-reliableright-way-to-teach-llms-to-generate-sq]]'
status: unread
---

> **TL;DR:** I once removed the first base of every gene in a dataset. Nobody noticed for two days. The bug was seven characters long: I had converted a VCF coordinate into a BED interval by subtracting 1 from start and forgotten tha…

## What’s new and why it matters
I once removed the first base of every gene in a dataset. Nobody noticed for two days. The bug was seven characters long: I had converted a VCF coordinate into a BED interval by subtracting 1 from start and forgotten that BED intervals are already 0-based and half-open. My "correction" was a corruption. I wish this story were unusual. It isn't. Bioinformatics has, over about twenty years of organic growth, built the most impressive collection of off-by-one hazards in modern software. Here's the story of why and the survival rules I now live by. Why coordinates matter in biology A genome is a v…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nadiabaig/the-off-by-one-error-that-ate-genomics-how-0-based-and-1-based-coordinates-started-a-20-year-civil-2lhb

## Related notes
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-05-19-in-some-scenarios-relying-on-llms-to-generate-sql-is-neither-rigorous-nor-reliableright-way-to-teach-llms-to-generate-sq]]
