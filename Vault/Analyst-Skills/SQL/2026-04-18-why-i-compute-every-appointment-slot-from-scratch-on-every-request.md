---
title: Why I Compute Every Appointment Slot from Scratch on Every Request
date: '2026-04-18'
source: https://dev.to/kingsleyonoh/why-i-compute-every-appointment-slot-from-scratch-on-every-request-3al6
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
status: unread
---

> **TL;DR:** The obvious approach to appointment scheduling is a lookup table. Run a job at midnight. Generate every possible slot for the next two weeks. Store them in a slots table. When a patient asks what's available, query the t…

## What’s new and why it matters
The obvious approach to appointment scheduling is a lookup table. Run a job at midnight. Generate every possible slot for the next two weeks. Store them in a slots table. When a patient asks what's available, query the table. When someone books, mark the row as taken. I built the opposite. The Clinical Scheduling Engine has no slot table. Every time a patient asks "what's available Thursday?", the system loads all constraints from the database, computes valid slots in real time, scores each one, and returns a sorted list. Nothing is pre-generated. Nothing is cached except availability windows…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kingsleyonoh/why-i-compute-every-appointment-slot-from-scratch-on-every-request-3al6

## Related notes
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-03-15-data-quality-testing-how-bruin-and-dbt-take-different-paths-to-the-same-goal]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
