---
title: Why SQLite FTS5's default tokenizer drops your Japanese substrings (and the
  one-line fix)
date: '2026-06-09'
source: https://dev.to/omochi_dev/why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix-1k2d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]'
- '[[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]'
- '[[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]'
status: unread
---

> **TL;DR:** If you're building any kind of personal-memory layer on top of SQLite — Claude Code conversation history, notes app, indexed knowledge base — there's a sharp edge in FTS5 that takes most people by surprise the first time…

## What’s new and why it matters
If you're building any kind of personal-memory layer on top of SQLite — Claude Code conversation history, notes app, indexed knowledge base — there's a sharp edge in FTS5 that takes most people by surprise the first time they hit it. The default tokenizer ( unicode61 ) silently drops most Japanese substring queries. The fix is one line of SQL. But the failure mode is invisible enough that you can ship a personal search tool, use it for weeks, and never realize half your content is unreachable. This post walks through: The failure, reproducible in 20 lines of Python The one-line fix ( tokenize=…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/omochi_dev/why-sqlite-fts5s-default-tokenizer-drops-your-japanese-substrings-and-the-one-line-fix-1k2d

## Related notes
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-24-sql-like-and-wildcards-pattern-matching-made-simple]]
- [[2026-03-30-build-a-productionready-sql-evaluation-engine-for-llms]]
- [[2026-05-22-i-built-a-type-safe-sql-library-for-bun-no-orm-no-codegen-just-sql-using-claude-code]]
