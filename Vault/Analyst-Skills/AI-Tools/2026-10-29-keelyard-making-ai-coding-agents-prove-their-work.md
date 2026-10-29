---
title: 'keelyard: making AI coding agents prove their work'
date: '2026-10-29'
source: https://dev.to/akobirjontulqinovfuture/keelyard-making-ai-coding-agents-prove-their-work-1j30
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-15-on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-10-06-we-caught-our-own-ai-security-scanner-making-up-vulnerabilities]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-05-22-how-i-use-windsurf-for-fast-prototyping-and-codex-for-multi-file-cleanup]]'
status: unread
---

> **TL;DR:** I'm a solo developer from Uzbekistan. Most of what I ship (Telegram bots and mini apps for small businesses) I build together with AI coding agents. They're fast, but they have one habit that cost me hours: they say "don…

## What’s new and why it matters
I'm a solo developer from Uzbekistan. Most of what I ship (Telegram bots and mini apps for small businesses) I build together with AI coding agents. They're fast, but they have one habit that cost me hours: they say "done" when the work isn't done. Tests still red. Sometimes tests quietly removed. keelyard is my fix. It's a Python CLI plus an MCP server that plugs into Claude Code, Codex and OpenCode. What it does Proof gate. If the agent changed files, it can't finish until the tests pass on the current files. The evidence is labeled: test-verified, command-succeeded or agent-claimed. Deleted…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/akobirjontulqinovfuture/keelyard-making-ai-coding-agents-prove-their-work-1j30

## Related notes
- [[2026-10-15-on-windows-four-processes-appending-to-one-file-lost-37-of-200-lines]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-10-06-we-caught-our-own-ai-security-scanner-making-up-vulnerabilities]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-05-22-how-i-use-windsurf-for-fast-prototyping-and-codex-for-multi-file-cleanup]]
