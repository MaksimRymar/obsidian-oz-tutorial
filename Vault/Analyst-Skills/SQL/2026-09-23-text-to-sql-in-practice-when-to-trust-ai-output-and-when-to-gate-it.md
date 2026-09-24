---
title: 'Text-to-SQL in Practice: When to Trust AI Output and When to Gate It'
date: '2026-09-23'
source: https://dev.to/databaseinsights/text-to-sql-in-practice-when-to-trust-ai-output-and-when-to-gate-it-24fe
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-15-sql-joins-explained]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]'
status: unread
---

> **TL;DR:** AI assistants are now a normal part of SQL work. You describe what you need, get a query back in seconds and move on. The problem is not that these queries fail. Most of the time, they run perfectly. The problem is that…

## What’s new and why it matters
AI assistants are now a normal part of SQL work. You describe what you need, get a query back in seconds and move on. The problem is not that these queries fail. Most of the time, they run perfectly. The problem is that a query can run perfectly and still be wrong. This post covers why that happens, how to sort database tasks by risk and how to build guardrails into a normal workflow. Adoption is high, trust is not The Stack Overflow 2025 Developer Survey puts AI adoption at 84% of developers using or planning to use AI tools. The same survey found that 46% of developers distrust the accuracy…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/databaseinsights/text-to-sql-in-practice-when-to-trust-ai-output-and-when-to-gate-it-24fe

## Related notes
- [[2026-09-15-sql-joins-explained]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-08-26-redb-371-props-search-up-to-100x-faster-an-alternative-to-ef-core-or-a-companion-to-it]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]
