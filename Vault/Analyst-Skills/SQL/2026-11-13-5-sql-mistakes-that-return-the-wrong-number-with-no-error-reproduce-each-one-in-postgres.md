---
title: 5 SQL mistakes that return the wrong number with no error (reproduce each one
  in Postgres)
date: '2026-11-13'
source: https://dev.to/factqlai/5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres-4nk1
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-03-build-a-knowledge-layer-for-sql-agents-with-okf-part-2]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]'
- '[[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]'
status: unread
---

> **TL;DR:** More and more SQL gets written by AI now, inside chat tools, agents and "ask your data" features. Most of it runs. That's the problem: the dangerous mistakes aren't the ones that throw an error. They're the ones that run…

## What’s new and why it matters
More and more SQL gets written by AI now, inside chat tools, agents and "ask your data" features. Most of it runs. That's the problem: the dangerous mistakes aren't the ones that throw an error. They're the ones that run fine and return a number that looks right. Below are five of them. Each comes with a tiny Postgres setup you can paste into psql , the query that gets it wrong, the query that gets it right, and the thing you'd have to look at to notice. Setup (30 seconds) CREATE DATABASE silent_bugs ; \ c silent_bugs SET TIME ZONE 'UTC' ; CREATE TABLE orders ( id int PRIMARY KEY , status text…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/factqlai/5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres-4nk1

## Related notes
- [[2026-10-03-build-a-knowledge-layer-for-sql-agents-with-okf-part-2]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-10-26-sql-joins-explained-inner-left-right-and-full-with-examples]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-10-06-i-scanned-1152-dbt-models-for-joins-that-inflate-sum-here-is-what-i-found]]
- [[2026-11-12-ai-brand-tracking-a-practical-check-you-can-run-today-by-yourself]]
