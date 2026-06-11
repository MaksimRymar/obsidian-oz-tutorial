---
title: 'PII masking in Polars: MaskOps 2.0, and two metrics that lied to me'
date: '2026-06-11'
source: https://dev.to/fcarvajalbrown/pii-masking-in-polars-maskops-20-and-two-metrics-that-lied-to-me-2bh3
domain: Python
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#tableau'
- '#tool'
related:
- '[[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-05-06-how-to-optimize-bigquery-costs-real-techniques-that-work]]'
- '[[2026-05-20-top-10-agentic-ai-frameworks-compared-langgraph-vs-crewai-vs-autogen-vs-benchmarks-inside]]'
- '[[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
status: unread
---

> **TL;DR:** MaskOps 2.0 shipped this week. Before I told anyone, I looked at my own numbers. Two of them were lying to me — in opposite directions. MaskOps is a Rust plugin for Polars that does PII masking inside the dataframe — RUT…

## What’s new and why it matters
MaskOps 2.0 shipped this week. Before I told anyone, I looked at my own numbers. Two of them were lying to me — in opposite directions. MaskOps is a Rust plugin for Polars that does PII masking inside the dataframe — RUT, CPF, credit cards, IBANs, and twenty-odd more families — air-gapped, with no network call, ever. If you have reached for Microsoft Presidio and found it carries no Latin American identifiers, that is the gap MaskOps fills: check-digit-validated RUT, CPF, and CURP detection alongside the EU, US, and APAC families, as a native Polars expression. Version 2.0 is the enterprise li…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/fcarvajalbrown/pii-masking-in-polars-maskops-20-and-two-metrics-that-lied-to-me-2bh3

## Related notes
- [[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-05-06-how-to-optimize-bigquery-costs-real-techniques-that-work]]
- [[2026-05-20-top-10-agentic-ai-frameworks-compared-langgraph-vs-crewai-vs-autogen-vs-benchmarks-inside]]
- [[2026-05-31-i-built-a-release-intelligence-agent-in-4-days-with-coral-groq-and-claude-code-heres-the-exact-route]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
