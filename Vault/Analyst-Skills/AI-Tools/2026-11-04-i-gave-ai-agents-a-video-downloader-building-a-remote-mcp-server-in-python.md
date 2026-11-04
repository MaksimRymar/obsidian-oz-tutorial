---
title: 'I gave AI agents a video downloader: building a remote MCP server in Python'
date: '2026-11-04'
source: https://dev.to/qamar_aftab_533855f09824f/i-gave-ai-agents-a-video-downloader-building-a-remote-mcp-server-in-python-5eb5
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-09-21-building-an-mcp-server-for-your-django-app-what-we-learned-doing-it-for-real]]'
- '[[2026-04-25-i-stopped-fighting-the-reddit-api-so-i-built-supermcp-to-read-it-for-me]]'
- '[[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]'
- '[[2026-05-02-ai-sql-assistant-or-mcp-database-server-they-are-not-the-same-thing]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
status: unread
---

> **TL;DR:** AI assistants can write code and summarise articles, but when I asked one to "download this video" it had no way to do it. I had already built SaveDock , a free video and audio downloader on Django, yt-dlp and Celery, so…

## What’s new and why it matters
AI assistants can write code and summarise articles, but when I asked one to "download this video" it had no way to do it. I had already built SaveDock , a free video and audio downloader on Django, yt-dlp and Celery, so I gave agents a way to use it: an MCP server. What is MCP? The Model Context Protocol (MCP) is an open standard that lets an AI client, such as Claude or Cursor, call tools that live on a server. The client lists the tools, reads their descriptions, and decides when to use them. You don't write a plugin for each assistant. You write one server. The design: a thin adapter, not…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/qamar_aftab_533855f09824f/i-gave-ai-agents-a-video-downloader-building-a-remote-mcp-server-in-python-5eb5

## Related notes
- [[2026-09-21-building-an-mcp-server-for-your-django-app-what-we-learned-doing-it-for-real]]
- [[2026-04-25-i-stopped-fighting-the-reddit-api-so-i-built-supermcp-to-read-it-for-me]]
- [[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]
- [[2026-05-02-ai-sql-assistant-or-mcp-database-server-they-are-not-the-same-thing]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
