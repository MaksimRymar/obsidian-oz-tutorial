---
title: How many tokens does your Claude Code setup burn before you type anything?
  A 60-line audit script
date: '2026-10-06'
source: https://dev.to/quiethand098/how-many-tokens-does-your-claude-code-setup-burn-before-you-type-anything-a-60-line-audit-script-2go9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-16-whats-eating-your-claude-code-context-window-i-wrote-a-500-line-python-script-to-find-out]]'
- '[[2026-05-17-devmcp-context-a-simple-ai-memory-layer-for-your-agent]]'
- '[[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-09-24-papermill-notebook-pipelines-parametrized-scheduled-version-controlled-notebooks]]'
status: unread
---

> **TL;DR:** Claude Code loads your CLAUDE.md , the name and description of every skill, and the tool schemas of every MCP server into context at the start of each session. That is a fixed cost on every conversation, and it is easy t…

## What’s new and why it matters
Claude Code loads your CLAUDE.md , the name and description of every skill, and the tool schemas of every MCP server into context at the start of each session. That is a fixed cost on every conversation, and it is easy to forget about. I wrote a small zero-dependency Python script that estimates it (characters divided by four, so treat it as a rough guide). Run it curl -O https://raw.githubusercontent.com/quiethand098/claude-code-starter-kit/main/ccaudit/ccaudit.py python3 ccaudit.py path/to/project It lists: CLAUDE.md size in tokens and lines, with a warning above ~1500 tokens each skill's pr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/quiethand098/how-many-tokens-does-your-claude-code-setup-burn-before-you-type-anything-a-60-line-audit-script-2go9

## Related notes
- [[2026-04-16-whats-eating-your-claude-code-context-window-i-wrote-a-500-line-python-script-to-find-out]]
- [[2026-05-17-devmcp-context-a-simple-ai-memory-layer-for-your-agent]]
- [[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-09-24-papermill-notebook-pipelines-parametrized-scheduled-version-controlled-notebooks]]
