---
title: Using an LLM to filter data from tables
date: '2026-11-16'
source: https://dev.to/fthiella/using-an-llm-to-filter-data-from-tables-13ff
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tableau'
- '#tool'
related:
- '[[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-10-03-hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
status: unread
---

> **TL;DR:** An LLM is perfectly capable of converting natural language into SQL. You just ask it. And that is exactly the problem. If you expose this on the web, with access to a real database, you are putting a probabilistic text g…

## What’s new and why it matters
An LLM is perfectly capable of converting natural language into SQL. You just ask it. And that is exactly the problem. If you expose this on the web, with access to a real database, you are putting a probabilistic text generator where a compiler should be. Sometimes it works, sometimes it fails. And when it fails, it does so in unpredictable, often silent, and potentially catastrophic ways: it hallucinates column names. For example, it writes users.full_name when you have first_name and last_name. The query explodes, or it gives you a reassuringly wrong result; it picks the wrong operator, lik…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/fthiella/using-an-llm-to-filter-data-from-tables-13ff

## Related notes
- [[2026-06-15-why-text-to-sql-needs-join-path-context-not-just-schema]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-10-03-hiding-the-table-is-not-enough-your-llm-can-still-see-the-salary-column]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-09-15-sql-joins-explained]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
