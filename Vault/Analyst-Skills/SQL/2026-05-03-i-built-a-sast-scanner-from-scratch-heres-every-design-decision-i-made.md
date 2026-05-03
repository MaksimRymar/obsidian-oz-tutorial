---
title: I Built a SAST Scanner From Scratch — Here's Every Design Decision I Made
date: '2026-05-03'
source: https://dev.to/pgmpofu/i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made-5454
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-20-sql-formatting-best-practices-write-clean-readable-queries]]'
- '[[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
status: unread
---

> **TL;DR:** When most developers want to scan their code for security vulnerabilities, they install Semgrep or Snyk and call it a day. I did the opposite. I built one from scratch. Not because the existing tools are bad — they're ex…

## What’s new and why it matters
When most developers want to scan their code for security vulnerabilities, they install Semgrep or Snyk and call it a day. I did the opposite. I built one from scratch. Not because the existing tools are bad — they're excellent. But because I'm transitioning from 13 years of software engineering into application security, and I wanted to understand what a SAST tool actually is underneath the hood. What decisions go into building one? What tradeoffs do you make? What does "language-agnostic" really mean when you have to implement it yourself? This is the story of those decisions. Some were obvi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/pgmpofu/i-built-a-sast-scanner-from-scratch-heres-every-design-decision-i-made-5454

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-20-sql-formatting-best-practices-write-clean-readable-queries]]
- [[2026-03-30-your-sql-client-is-a-relic-heres-what-a-duckdb-native-ide-looks-like]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
