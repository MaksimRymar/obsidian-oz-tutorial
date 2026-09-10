---
title: Six Tables Out of 260
date: '2026-09-09'
source: https://dev.to/ashish_sinha_5241c7673d93/six-tables-out-of-260-343a
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]'
- '[[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
- '[[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]'
- '[[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]'
status: unread
---

> **TL;DR:** Every text-to-SQL system has a step nobody writes about. Before the model can generate anything, something has to decide which tables it gets to see, because you cannot put 260 tables in a prompt. That step is usually tr…

## What’s new and why it matters
Every text-to-SQL system has a step nobody writes about. Before the model can generate anything, something has to decide which tables it gets to see, because you cannot put 260 tables in a prompt. That step is usually treated as a retrieval problem: embed the schema, rank by similarity, take the top six. It works well enough on the tidy 40-table schema a demo uses. So I built a schema designed to break it, and ran my own library against it. Here is what happened, including the number I would rather not publish. The test schema 127 objects across three unrelated domains in one database: a healt…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ashish_sinha_5241c7673d93/six-tables-out-of-260-343a

## Related notes
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-05-20-how-to-prompt-ai-tools-to-write-accurate-sql-queries-and-why-most-developers-get-this-wrong]]
- [[2026-09-05-what-actually-happens-in-a-database-index-and-why-half-of-them-do-nothing]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
- [[2026-08-27-i-gave-an-llm-the-keys-to-a-multi-tenant-database]]
- [[2026-08-10-140-bugs-were-hiding-in-one-function-and-my-tests-couldnt-see-any-of-them]]
