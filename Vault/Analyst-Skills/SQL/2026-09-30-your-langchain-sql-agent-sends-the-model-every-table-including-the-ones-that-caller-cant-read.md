---
title: Your LangChain SQL agent sends the model every table, including the ones that
  caller can't read
date: '2026-09-30'
source: https://dev.to/ashish_sinha_5241c7673d93/your-langchain-sql-agent-sends-the-model-every-table-including-the-ones-that-caller-cant-read-56oo
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]'
- '[[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]'
status: unread
---

> **TL;DR:** A LangChain SQL agent hands the model your schema and asks it to write SQL. On a demo database with eight tables that is fine. On a real one it breaks in two ways at once. The schema outgrows the context window. I wrote…

## What’s new and why it matters
A LangChain SQL agent hands the model your schema and asks it to write SQL. On a demo database with eight tables that is fine. On a real one it breaks in two ways at once. The schema outgrows the context window. I wrote about this before, on a warehouse with 1,245 tables — the table listing alone did not fit, and describing every table with an LLM to help retrieval made it worse , not better. And the model sees tables the caller is not allowed to read. This one is quieter and worse. SQLDatabase.get_table_info() returns what the connection can see, not what the person asking can see. If your ap…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ashish_sinha_5241c7673d93/your-langchain-sql-agent-sends-the-model-every-table-including-the-ones-that-caller-cant-read-56oo

## Related notes
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-19-the-arabic-pdf-bug-was-never-in-my-code-it-was-the-library-version]]
- [[2026-09-06-the-julius-ai-free-plan-what-the-free-credits-actually-get-you]]
