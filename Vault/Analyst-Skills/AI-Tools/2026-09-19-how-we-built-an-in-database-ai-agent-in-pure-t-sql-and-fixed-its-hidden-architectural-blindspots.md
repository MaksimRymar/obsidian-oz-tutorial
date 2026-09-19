---
title: How We Built an In-Database AI Agent in Pure T-SQL (And Fixed Its Hidden Architectural
  Blindspots)
date: '2026-09-19'
source: https://dev.to/rick_hoek_c401925e5aec039/how-we-built-an-in-database-ai-agent-in-pure-t-sql-and-fixed-its-hidden-architectural-blindspots-3dpn
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]'
- '[[2026-08-12-semantic-drift-the-hidden-failure-mode-of-enterprise-ai-analytics]]'
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-08-07-your-text-to-sql-model-isnt-as-wrong-as-your-benchmark-says-the-gold-sql-is]]'
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** An AI agent doesn't need a heavy Python microservice, a complex LangChain orchestrator, or an external background daemon. In our architecture, ask_ai is an autonomous agent that lives entirely inside a SQL Server databas…

## What’s new and why it matters
An AI agent doesn't need a heavy Python microservice, a complex LangChain orchestrator, or an external background daemon. In our architecture, ask_ai is an autonomous agent that lives entirely inside a SQL Server database schema ( {app}_proj ) [28, 29]. Its core engine ( sp_openai_agent ) is a tight 332-line WHILE loop written in pure T-SQL: it fetches an execution step, invokes an HTTP endpoint via sp_ask_ai_http ( sp_invoke_external_rest_endpoint ), parses JSON tool calls, executes dbo.sp_ask_ai_run_tool , and repeats [28]. There is no external daemon or scheduler—its tools are stored proced…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rick_hoek_c401925e5aec039/how-we-built-an-in-database-ai-agent-in-pure-t-sql-and-fixed-its-hidden-architectural-blindspots-3dpn

## Related notes
- [[2026-05-08-from-2-hours-to-3-minutes-eliminating-missed-tests-in-ai-memory-consistency-testing]]
- [[2026-08-12-semantic-drift-the-hidden-failure-mode-of-enterprise-ai-analytics]]
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-08-07-your-text-to-sql-model-isnt-as-wrong-as-your-benchmark-says-the-gold-sql-is]]
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
