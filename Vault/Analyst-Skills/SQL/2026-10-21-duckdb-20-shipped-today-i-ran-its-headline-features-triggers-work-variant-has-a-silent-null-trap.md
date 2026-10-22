---
title: DuckDB 2.0 shipped today. I ran its headline features — triggers work, VARIANT
  has a silent-NULL trap
date: '2026-10-21'
source: https://dev.to/frankchu/duckdb-20-shipped-today-i-ran-its-headline-features-triggers-work-variant-has-a-silent-null-58hb
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]'
- '[[2026-09-16-what-do-duckdb-and-slayer-have-in-common]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
status: unread
---

> **TL;DR:** DuckDB 2.0.0 LTS, codename "Cinnamon Teal," shipped today (October 21), billed as the project's biggest feature release yet: close to 20,000 commits since 1.5, a polished Quack client-server protocol, asynchronous I/O, a…

## What’s new and why it matters
DuckDB 2.0.0 LTS, codename "Cinnamon Teal," shipped today (October 21), billed as the project's biggest feature release yet: close to 20,000 commits since 1.5, a polished Quack client-server protocol, asynchronous I/O, a first-class VARIANT type, triggers, a new PEG parser as the default, an "agent mode" for the CLI, and support promised until at least October 2027. Launch posts are menus. I wanted a scoreboard. So I installed the Python client — duckdb==2.0.0 , on a 2 vCPU Linux VM — and ran the headline features myself. Most of them work exactly as advertised. One of them has a trap that ret…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/frankchu/duckdb-20-shipped-today-i-ran-its-headline-features-triggers-work-variant-has-a-silent-null-58hb

## Related notes
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-10-16-an-ai-explained-sql-group-by-in-four-lines-one-of-them-is-wrong]]
- [[2026-09-16-what-do-duckdb-and-slayer-have-in-common]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
