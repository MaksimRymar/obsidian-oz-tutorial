---
title: My Code Reviewer Scored a Nonexistent Directory 100/100 and Exited 0
date: '2026-10-01'
source: https://dev.to/felixwang007/my-code-reviewer-scored-a-nonexistent-directory-100100-and-exited-0-41m0
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-09-03-building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies]]'
status: unread
---

> **TL;DR:** Every skill package I ship — for Claude Code, Cursor, Codex, and a couple of agent marketplaces — has to clear one gate before publishing: its own selftest must exit 0. So this week I ran an audit over the 34 packages si…

## What’s new and why it matters
Every skill package I ship — for Claude Code, Cursor, Codex, and a couple of agent marketplaces — has to clear one gate before publishing: its own selftest must exit 0. So this week I ran an audit over the 34 packages sitting in my skills folder to find out how many actually have that gate. The audit broke twice, in two different ways. Both breakages are the same bug wearing different clothes, and it's the bug that makes agent tooling untrustworthy the moment you put it in CI: a success signal that isn't attached to work actually done. Here's the whole thing, including the raw output. Pass one…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/felixwang007/my-code-reviewer-scored-a-nonexistent-directory-100100-and-exited-0-41m0

## Related notes
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-30-funnel-conversion-in-sql-and-the-step-that-shows-100]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-09-03-building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies]]
