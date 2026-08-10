---
title: I Measured What My Curated MCP Tool Output Is Actually Saving
date: '2026-08-10'
source: https://dev.to/enjoy_kumawat/i-measured-what-my-curated-mcp-tool-output-is-actually-saving-4f36
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
- '[[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-10-why-senior-data-engineers-write-sql-differently]]'
- '[[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]'
- '[[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]'
status: unread
---

> **TL;DR:** Every tool in my Developer Presence MCP server returns a hand-picked dict, never the raw API response. I did that from day one because it felt obviously correct — why hand a model twenty fields when it needs six. I never…

## What’s new and why it matters
Every tool in my Developer Presence MCP server returns a hand-picked dict, never the raw API response. I did that from day one because it felt obviously correct — why hand a model twenty fields when it needs six. I never actually measured what it was saving. I finally ran the numbers this morning, on real data from my own account, and the size of the gap surprised me enough that I want to show the actual breakdown instead of just asserting "less is more." the tool in question list_articles in server.py wraps DEV.to's /articles/me/published endpoint: @mcp.tool () def list_articles ( per_page :…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/i-measured-what-my-curated-mcp-tool-output-is-actually-saving-4f36

## Related notes
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
- [[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-10-why-senior-data-engineers-write-sql-differently]]
- [[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]
- [[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]
