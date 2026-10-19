---
title: 0.920 on the benchmark. Zero findings on Juice Shop.
date: '2026-10-19'
source: https://dev.to/janissary/0920-on-the-benchmark-zero-findings-on-juice-shop-2nf8
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]'
- '[[2026-10-09-how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time]]'
- '[[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]'
status: unread
---

> **TL;DR:** Three days ago I published JANISSARY's benchmark results: F1 0.920, precision 1.000 on the OWASP Benchmark DAST-applicable subset. Zero false positives across 2,258 cases. Today I ran it against OWASP Juice Shop. It foun…

## What’s new and why it matters
Three days ago I published JANISSARY's benchmark results: F1 0.920, precision 1.000 on the OWASP Benchmark DAST-applicable subset. Zero false positives across 2,258 cases. Today I ran it against OWASP Juice Shop. It found 39 vulnerabilities. All 39 were wrong. And it missed the SQL injection I already knew was in the search endpoint. Both of those things are true. This post is about why. What the benchmark actually promises The benchmark tests detection on a corpus of Java servlets. Each servlet either is or isn't vulnerable to a specific class. The scanner gets no source access. JANISSARY sco…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/janissary/0920-on-the-benchmark-zero-findings-on-juice-shop-2nf8

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-21-sql-nulls-demystified-what-they-are-and-how-to-handle-them]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-09-24-my-alert-fired-7-times-across-1963-pairs-i-assumed-the-thresholds-were-too-high-they-were-and-it-didnt-matter]]
- [[2026-10-09-how-to-test-tool-calling-in-your-ai-agent-one-decision-at-a-time]]
- [[2026-08-11-sql-joins-how-to-join-two-tables-without-losing-or-doubling-rows]]
