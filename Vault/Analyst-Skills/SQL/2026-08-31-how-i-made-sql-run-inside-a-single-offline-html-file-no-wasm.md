---
title: How I made SQL run inside a single, offline HTML file (no WASM)
date: '2026-08-31'
source: https://dev.to/aurelionakamura/how-i-made-sql-run-inside-a-single-offline-html-file-no-wasm-3fk9
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]'
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-06-28-data-analysis-sql-asking-the-right-questions-and-using-the-right-tools]]'
status: unread
---

> **TL;DR:** There's a whole genre of "single-file HTML data viewer" tools: you point them at a CSV and they emit one .html file you can email, drop on a share drive, or open on an air-gapped machine. They're great for looking at dat…

## What’s new and why it matters
There's a whole genre of "single-file HTML data viewer" tools: you point them at a CSV and they emit one .html file you can email, drop on a share drive, or open on an air-gapped machine. They're great for looking at data. But the moment you want to actually ask a question — "how many rows per category?", "top 10 by revenue?" — you're back to sorting columns by hand or re-exporting from a real database. So for dataloupe I added a real SQL console inside the generated file. No server, no WASM download, no network request. Here's how, and why it stays honest about the "single file, works offline…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aurelionakamura/how-i-made-sql-run-inside-a-single-offline-html-file-no-wasm-3fk9

## Related notes
- [[2026-08-20-read-only-by-design-letting-ai-explore-your-database-without-the-risk-of-writes]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-05-18-wrong-answer-is-the-worst-feedback-you-can-give-a-sql-learner-so-i-built-something-better]]
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-06-28-data-analysis-sql-asking-the-right-questions-and-using-the-right-tools]]
