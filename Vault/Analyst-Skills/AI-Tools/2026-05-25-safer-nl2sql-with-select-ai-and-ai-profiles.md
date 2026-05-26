---
title: Safer NL2SQL with Select AI and AI Profiles
date: '2026-05-25'
source: https://dev.to/oracledevs/safer-nl2sql-with-select-ai-and-ai-profiles-18jc
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-02-sql-joins-explained-case-example]]'
- '[[2026-05-02-ai-sql-assistant-or-mcp-database-server-they-are-not-the-same-thing]]'
- '[[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-02-joins-and-window-functions-made-super-simple]]'
status: unread
---

> **TL;DR:** Key Takeaways AI Profiles bind the model to a defined list of database objects. With enforce_object_list enabled, generated SQL cannot reach tables you did not explicitly name — scope is a constraint, not just a suggesti…

## What’s new and why it matters
Key Takeaways AI Profiles bind the model to a defined list of database objects. With enforce_object_list enabled, generated SQL cannot reach tables you did not explicitly name — scope is a constraint, not just a suggestion. SHOWSQL returns the candidate SQL without executing it, using schema metadata rather than table data. You see what the assistant intends before any data moves or any query runs. EXPLAINSQL surfaces the model's reasoning — the join choices, date windows, and grouping logic — so reviewers can catch wrong assumptions before they become surprises in a result set. DISABLE_DATA_A…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/oracledevs/safer-nl2sql-with-select-ai-and-ai-profiles-18jc

## Related notes
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-02-sql-joins-explained-case-example]]
- [[2026-05-02-ai-sql-assistant-or-mcp-database-server-they-are-not-the-same-thing]]
- [[2026-04-19-sql-joins-explained-simply---a-beginners-guide]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-02-joins-and-window-functions-made-super-simple]]
