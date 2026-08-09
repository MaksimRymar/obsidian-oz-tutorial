---
title: '"My MCP Server''s Two Credential Checks Were Flagged Missing Five Days Ago.
  Nobody Fixed Them."'
date: '2026-08-09'
source: https://dev.to/enjoy_kumawat/my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them-4lgk
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-01-my-publish-script-truncates-tags-to-4-my-mcp-tool-that-does-the-same-job-never-learned-that-rule]]'
- '[[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]'
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
status: unread
---

> **TL;DR:** I keep a work log for this repo — every bug I find and fix gets an entry in docs/project_notes/issues.md , with enough detail that a future session (or a future me) doesn't have to rediscover the same thing twice. Today…

## What’s new and why it matters
I keep a work log for this repo — every bug I find and fix gets an entry in docs/project_notes/issues.md , with enough detail that a future session (or a future me) doesn't have to rediscover the same thing twice. Today I went back and actually reread one of those entries instead of just trusting that logging a gap meant it got closed. It didn't. The entry, from five days ago, was auditing a completely different bug (a hardcoded relative path in server.py ). Buried in its notes was one line: "did not add friendlier error messages for a missing credential beyond the path fix — a separate, unrep…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them-4lgk

## Related notes
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-01-my-publish-script-truncates-tags-to-4-my-mcp-tool-that-does-the-same-job-never-learned-that-rule]]
- [[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
