---
title: I Tried to Analyze SQL Lineage Across 15 Databases — Everything Broke Until
  I Did This
date: '2026-04-04'
source: https://dev.to/leo_gu_475098bd7f84e326ed/i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this-m5j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]'
- '[[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]'
- '[[2026-03-25-stop-googling-dax-formulas-here-are-the-5-i-actually-use-to-solve-business-problems]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]'
- '[[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]'
status: unread
---

> **TL;DR:** The problem nobody talks about If you’ve ever worked with SQL at scale, you’ve probably run into this: Queries spanning multiple schemas dbt models referencing each other Views built on top of views Different SQL dialect…

## What’s new and why it matters
The problem nobody talks about If you’ve ever worked with SQL at scale, you’ve probably run into this: Queries spanning multiple schemas dbt models referencing each other Views built on top of views Different SQL dialects (Snowflake, BigQuery, Spark…) And then someone asks: “Where does this column actually come from?” At that moment, everything falls apart. Not because the answer doesn’t exist — but because your tools can’t give it to you . I tried to solve it the “normal” way I went through the usual stack: dbt lineage graphs Database-native tools SQL IDEs like DataGrip and DBeaver They work……

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/leo_gu_475098bd7f84e326ed/i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this-m5j

## Related notes
- [[2026-03-11-i-built-a-zero-friction-sqlite-playground-for-my-students]]
- [[2026-03-10-data-forge-vs-mockaroo-vs-fakerjs-i-tested-all-3-so-you-dont-have-to]]
- [[2026-03-25-stop-googling-dax-formulas-here-are-the-5-i-actually-use-to-solve-business-problems]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]
- [[2026-04-02-ctes-vs-subqueries-in-sql-which-one-should-you-use]]
