---
title: Why We Never Let an LLM Talk Directly to Our Database (A Teams + Copilot +
  MySQL Case Study)
date: '2026-08-19'
source: https://dev.to/alexhadley/why-we-never-let-an-llm-talk-directly-to-our-database-a-teams-copilot-mysql-case-study-3c6g
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-06-10-your-database-is-fast-your-queries-are-slow]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]'
status: unread
---

> **TL;DR:** TLDR Letting a chatbot generate SQL and fire it straight at a production database works great in a demo and falls apart the first week in production. This post walks through the setup we actually use: Microsoft Teams as…

## What’s new and why it matters
TLDR Letting a chatbot generate SQL and fire it straight at a production database works great in a demo and falls apart the first week in production. This post walks through the setup we actually use: Microsoft Teams as the chat window, a Copilot Agent that turns a question into a draft query, a custom API sitting in between that decides what's actually allowed to run, and MySQL underneath that never talks to anything except that API. Four things break naive "LLM-to-SQL" setups almost immediately: Plain English is full of unstated assumptions ("this month," "region," "sales" all mean different…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/alexhadley/why-we-never-let-an-llm-talk-directly-to-our-database-a-teams-copilot-mysql-case-study-3c6g

## Related notes
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-06-10-your-database-is-fast-your-queries-are-slow]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-07-02-beyond-tryexcept-advanced-exception-handling-patterns-every-ai-engineer-should-know]]
