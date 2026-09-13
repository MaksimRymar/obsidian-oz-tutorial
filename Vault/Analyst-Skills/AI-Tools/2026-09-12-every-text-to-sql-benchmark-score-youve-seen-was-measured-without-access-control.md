---
title: Every text-to-SQL benchmark score you've seen was measured without access control
date: '2026-09-12'
source: https://dev.to/ashish_sinha_5241c7673d93/every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control-37h
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
status: unread
---

> **TL;DR:** Spider, BIRD, LiveSQLBench. If you have evaluated a text-to-SQL system in the last five years you have quoted a number from one of them. All three ask the same question: given a schema and an English question, does the s…

## What’s new and why it matters
Spider, BIRD, LiveSQLBench. If you have evaluated a text-to-SQL system in the last five years you have quoted a number from one of them. All three ask the same question: given a schema and an English question, does the system produce SQL that returns the right rows? None of them ask who is asking. Every score you have seen was produced by a system with unrestricted read access to the entire database. That is not how anyone runs one in production, and a paper accepted to SIGMOD 2027 has now measured what happens when you close the gap. The paper Benchmarking Text-to-SQL under Role-Based Access…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ashish_sinha_5241c7673d93/every-text-to-sql-benchmark-score-youve-seen-was-measured-without-access-control-37h

## Related notes
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-27-a-longmemeval-s-number-you-can-reproduce]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
