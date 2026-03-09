---
title: How to Fix pyright-lsp on Claude Code for Windows (The Complete Guide)
date: '2026-03-09'
source: https://dev.to/magnuscole/how-to-fix-pyright-lsp-on-claude-code-for-windows-the-complete-guide-3013
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-03-01-async-python-made-simple-a-practical-guide-to-asyncio]]'
- '[[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]'
status: unread
---

> **TL;DR:** If you've tried to enable the pyright LSP plugin in Claude Code on Windows and hit a wall, this post is for you. After several hours of debugging, I discovered three separate bugs that compound on Windows. Here's the com…

## What’s new and why it matters
If you've tried to enable the pyright LSP plugin in Claude Code on Windows and hit a wall, this post is for you. After several hours of debugging, I discovered three separate bugs that compound on Windows. Here's the complete, tested fix. The Problem You add this to ~/.claude/settings.json : { "enabledPlugins" : { "pyright-lsp@claude-plugins-official" : true } } Or you run: /plugin install pyright-lsp@claude-plugins-official And you get: Plugin "pyright-lsp" not found in any marketplace Or, after fixing that, you run into: ENOENT: no such file or directory, uv_spawn 'pyright-langserver' Here's…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/magnuscole/how-to-fix-pyright-lsp-on-claude-code-for-windows-the-complete-guide-3013

## Related notes
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-03-01-async-python-made-simple-a-practical-guide-to-asyncio]]
- [[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]
