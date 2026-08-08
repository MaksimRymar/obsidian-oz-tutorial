---
title: My MCP Tool Fetches Before It Writes and Logs Every Change. It Never Checked
  Whether There Was Anything to Change.
date: '2026-08-08'
source: https://dev.to/enjoy_kumawat/my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-243m
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]'
- '[[2026-07-07-the-caller-heard-silence-for-two-seconds-before-the-agent-spoke]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
status: unread
---

> **TL;DR:** Two fixes ago, update_article — one of the tools in this repo's MCP server — got hardened twice. The first time, because it took a bare integer article_id , PUT whatever fields you gave it straight to the DEV.to API, and…

## What’s new and why it matters
Two fixes ago, update_article — one of the tools in this repo's MCP server — got hardened twice. The first time, because it took a bare integer article_id , PUT whatever fields you gave it straight to the DEV.to API, and if the id was wrong it would silently overwrite a live published post with nothing left behind to prove it happened. That fix added a fetch-before-write step and a JSONL audit log. The second time, because the diff the log recorded was a hardcoded {title, published} pair regardless of what you actually changed — a body_markdown -only edit showed up in the log as "nothing chang…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-243m

## Related notes
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-05-i-got-tired-of-writing-the-same-history-table-boilerplate-so-i-built-a-postgres-extension]]
- [[2026-07-07-the-caller-heard-silence-for-two-seconds-before-the-agent-spoke]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
