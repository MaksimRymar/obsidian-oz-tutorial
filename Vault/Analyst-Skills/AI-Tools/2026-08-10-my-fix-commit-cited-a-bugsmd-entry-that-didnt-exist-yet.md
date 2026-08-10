---
title: My Fix Commit Cited a bugs.md Entry That Didn't Exist Yet
date: '2026-08-10'
source: https://dev.to/enjoy_kumawat/my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet-1g5
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]'
- '[[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
status: unread
---

> **TL;DR:** I run a small MCP server and a couple of standalone scripts that publish this exact blog for me, twice a day, on a schedule. Every time one of them breaks, the fix gets written up in docs/project_notes/bugs.md : what bro…

## What’s new and why it matters
I run a small MCP server and a couple of standalone scripts that publish this exact blog for me, twice a day, on a schedule. Every time one of them breaks, the fix gets written up in docs/project_notes/bugs.md : what broke, why, how it was fixed, how to catch it earlier next time. My CLAUDE.md spells out the protocol in one line: "Encountering an error → search bugs.md first." That log is the whole point — it's how a fresh agent session, with no memory of yesterday, doesn't repeat yesterday's mistake. This morning's run found a real bug, fixed it in two files, and then — while writing the fix…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet-1g5

## Related notes
- [[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]
- [[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
