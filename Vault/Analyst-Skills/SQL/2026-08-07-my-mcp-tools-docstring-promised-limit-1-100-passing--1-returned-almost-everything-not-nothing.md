---
title: '"My MCP Tool''s Docstring Promised ''limit: 1-100.'' Passing -1 Returned Almost
  Everything, Not Nothing."'
date: '2026-08-07'
source: https://dev.to/enjoy_kumawat/my-mcp-tools-docstring-promised-limit-1-100-passing-1-returned-almost-everything-not-3f47
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]'
- '[[2026-06-17-how-to-add-policy-enforcement-to-a-langgraph-agent-before-it-does-something-dumb]]'
status: unread
---

> **TL;DR:** Every audit of server.py I've done before this one went looking for a specific bug shape first — a missing except block, a docstring's claimed API parameter GitHub silently ignores, a sort= value that isn't actually supp…

## What’s new and why it matters
Every audit of server.py I've done before this one went looking for a specific bug shape first — a missing except block, a docstring's claimed API parameter GitHub silently ignores, a sort= value that isn't actually supported. Those are all things you find by reading a function against something external: the real API's documented contract, the pattern another file in the repo already fixed. This one I found by reading a function against nothing but itself, and asking what happens at the edges of the range its own docstring claims to accept. list_repos is one of the eight MCP tools this accoun…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-mcp-tools-docstring-promised-limit-1-100-passing-1-returned-almost-everything-not-3f47

## Related notes
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]
- [[2026-06-17-how-to-add-policy-enforcement-to-a-langgraph-agent-before-it-does-something-dumb]]
