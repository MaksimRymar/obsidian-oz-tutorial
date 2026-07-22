---
title: 'The Tech Stack Behind a Canadian Healthcare SaaS: ChartPilot Phase 2'
date: '2026-07-22'
source: https://dev.to/dhiraj_chatpar_e54b46b388/the-tech-stack-behind-a-canadian-healthcare-saas-chartpilot-phase-2-3k73
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-04-20-how-i-built-a-game-agnostic-platform-with-11-modules-using-nextjs-15-and-fastapi]]'
- '[[2026-07-14-mastering-fastapi-async-logging-structured-rotating-and-workerready-logs-for-highperformance-apps]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
status: unread
---

> **TL;DR:** The Tech Stack Behind a Canadian Healthcare SaaS: ChartPilot Phase 2 We just completed Phase 2 of ChartPilot — a clinical documentation SaaS for Canadian healthcare organizations. The compliance requirements were non-tri…

## What’s new and why it matters
The Tech Stack Behind a Canadian Healthcare SaaS: ChartPilot Phase 2 We just completed Phase 2 of ChartPilot — a clinical documentation SaaS for Canadian healthcare organizations. The compliance requirements were non-trivial: PHIPA, PIPEDA, BCPIPA, and a dozen other acronyms. Here's the full stack and the decisions behind it. The Core Requirements Data residency : All data must stay in Canada (no US hyperscaler sub-processors) Encryption at rest and in transit : AES-256, TLS 1.3 Audit logging : Every read/write must be logged with timestamp, user, and action Access controls : Role-based with m…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dhiraj_chatpar_e54b46b388/the-tech-stack-behind-a-canadian-healthcare-saas-chartpilot-phase-2-3k73

## Related notes
- [[2026-04-20-how-i-built-a-game-agnostic-platform-with-11-modules-using-nextjs-15-and-fastapi]]
- [[2026-07-14-mastering-fastapi-async-logging-structured-rotating-and-workerready-logs-for-highperformance-apps]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
