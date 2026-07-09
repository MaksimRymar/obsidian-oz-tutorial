---
title: Compilable and Executable Pseudocode (spec) Solves AI Coding Hallucinations
date: '2026-07-09'
source: https://dev.to/esproc_spl/compilable-and-executable-pseudocode-spec-solves-ai-coding-hallucinations-5ghk
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-19-in-some-scenarios-relying-on-llms-to-generate-sql-is-neither-rigorous-nor-reliableright-way-to-teach-llms-to-generate-sq]]'
- '[[2026-06-25-when-ai-generated-sql-becomes-untrustworthy-how-to-restore-confidence-in-our-data]]'
- '[[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]'
- '[[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
status: unread
---

> **TL;DR:** The AI-generated SQL – no one dares to say they fully “understand” it First, look at the following SQL query, which aims to find credit card customers whose transaction amount has increased for three consecutive months:…

## What’s new and why it matters
The AI-generated SQL – no one dares to say they fully “understand” it First, look at the following SQL query, which aims to find credit card customers whose transaction amount has increased for three consecutive months: WITH ranked AS ( SELECT customer_id, month, amount, LAG(amount,1) OVER(PARTITION BY customer_id ORDER BY month) as prev_1, LAG(amount,2) OVER(PARTITION BY customer_id ORDER BY month) as prev_2 FROM transactions ) SELECT customer_id, COUNT(*) FROM ranked WHERE amount > prev_1 AND prev_1 > prev_2 AND prev_1 IS NOT NULL AND prev_2 IS NOT NULL GROUP BY customer_id HAVING COUNT(*) >…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/esproc_spl/compilable-and-executable-pseudocode-spec-solves-ai-coding-hallucinations-5ghk

## Related notes
- [[2026-05-19-in-some-scenarios-relying-on-llms-to-generate-sql-is-neither-rigorous-nor-reliableright-way-to-teach-llms-to-generate-sq]]
- [[2026-06-25-when-ai-generated-sql-becomes-untrustworthy-how-to-restore-confidence-in-our-data]]
- [[2026-06-10-day-10-of-100-days-of-clickhouse-what-makes-clickhouse-sql-different]]
- [[2026-06-19-oracle-ora-00934-error-causes-and-solutions-complete-guide]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
