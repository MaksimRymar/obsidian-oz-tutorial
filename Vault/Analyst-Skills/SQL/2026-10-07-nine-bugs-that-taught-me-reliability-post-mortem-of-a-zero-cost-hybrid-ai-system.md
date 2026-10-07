---
title: 'Nine Bugs That Taught Me Reliability: Post-Mortem of a Zero-Cost Hybrid AI
  System'
date: '2026-10-07'
source: https://dev.to/arielchangdev/nine-bugs-that-taught-me-reliability-post-mortem-of-a-zero-cost-hybrid-ai-system-4bce
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** canonical_url: https://arielchangdev.github.io/angelina-finance-agent/ Building a hybrid local+cloud AI system under two hard rules — $0 cost and never break production. The interesting part wasn't the happy path; it was…

## What’s new and why it matters
canonical_url: https://arielchangdev.github.io/angelina-finance-agent/ Building a hybrid local+cloud AI system under two hard rules — $0 cost and never break production. The interesting part wasn't the happy path; it was the 9 production bugs and what each taught me about where reliability actually lives. A war-stories write-up. The system was fun to design. The interesting part was the nine ways it quietly broke — and what each one taught me about where reliability actually lives. I spent a few months building and operating a small AI agent under two rules that never moved: It must cost exact…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/arielchangdev/nine-bugs-that-taught-me-reliability-post-mortem-of-a-zero-cost-hybrid-ai-system-4bce

## Related notes
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-09-28-i-kept-hitting-supabase-errors-so-i-built-a-scanner-for-the-legacy-api-key-deprecation-published-false]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
