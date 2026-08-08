---
title: I paged a table with no ORDER BY and lost 2,797 rows
date: '2026-08-07'
source: https://dev.to/kyisaiah47/i-paged-a-table-with-no-order-by-and-lost-2797-rows-39n2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#presentations'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-02-9104-rows-in-5000-out-the-silent-cap-that-made-my-dashboard-lie]]'
status: unread
---

> **TL;DR:** I ran a verification pass over 22,313 rows, it reported 22,313 rows, and I read that number as proof it had checked all of them. It had checked about 19,500 and looked at some of those twice. The product is BlockDex, an…

## What’s new and why it matters
I ran a verification pass over 22,313 rows, it reported 22,313 rows, and I read that number as proof it had checked all of them. It had checked about 19,500 and looked at some of those twice. The product is BlockDex, an item-level index of public shadcn registries I'm building under Kynth. Every item page can render a Live preview — an iframe of the component's own docs page — under a caption that says this is the component running, not a screenshot of it. Nothing checked that claim. preview_url was a URL shape learned once per registry from a single sample item name, accepted on status === 20…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kyisaiah47/i-paged-a-table-with-no-order-by-and-lost-2797-rows-39n2

## Related notes
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-02-9104-rows-in-5000-out-the-silent-cap-that-made-my-dashboard-lie]]
