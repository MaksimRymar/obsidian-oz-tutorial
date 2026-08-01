---
title: My Publish Script Truncates Tags to 4. My MCP Tool That Does the Same Job Never
  Learned That Rule.
date: '2026-08-01'
source: https://dev.to/enjoy_kumawat/my-publish-script-truncates-tags-to-4-my-mcp-tool-that-does-the-same-job-never-learned-that-rule-59ao
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
related:
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
- '[[2026-07-16-my-repo-had-two-scripts-that-hit-the-same-api-only-one-still-matched-what-i-actually-do]]'
- '[[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]'
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
status: unread
---

> **TL;DR:** This repo has two completely separate code paths that create a DEV.to article. One is publish_devto.py , a standalone script the scheduled publishing routine calls directly. The other is create_article , a tool on the MC…

## What’s new and why it matters
This repo has two completely separate code paths that create a DEV.to article. One is publish_devto.py , a standalone script the scheduled publishing routine calls directly. The other is create_article , a tool on the MCP server, meant for interactive use from Claude Desktop. They post to the same endpoint, build almost the same JSON payload, and — until today — only one of them knew DEV.to rejects more than 4 tags. # publish_devto.py tags = [ t . strip () for t in meta . get ( " tags " , "" ). replace ( " , " , " " ). split () if t . strip ()][: 4 ] # server.py, create_article — before the fi…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-publish-script-truncates-tags-to-4-my-mcp-tool-that-does-the-same-job-never-learned-that-rule-59ao

## Related notes
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
- [[2026-07-16-my-repo-had-two-scripts-that-hit-the-same-api-only-one-still-matched-what-i-actually-do]]
- [[2026-07-06-i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it]]
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
