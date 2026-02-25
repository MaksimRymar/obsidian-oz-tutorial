---
title: I built an audit plugin to audit Claude Code plugins
date: '2026-02-25'
source: https://dev.to/nestedcat/i-built-an-audit-plugin-to-audit-claude-code-plugins-4oon
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#tool'
- '#tutorial'
related:
- '[[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]'
- '[[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]'
- '[[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]'
- '[[2026-02-23-distributed-locking-in-python]]'
- '[[2026-02-25-beyond-to-do-lists-building-a-closed-loop-health-agent-with-langgraph-and-google-calendar]]'
- '[[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]'
status: unread
---

> **TL;DR:** Claude Code’s plugin system is incredibly powerful, but it’s easy to lose track of what’s actually running in your environment. After a week of adding marketplace tools and writing custom local agents, I ran into two iss…

## What’s new and why it matters
Claude Code’s plugin system is incredibly powerful, but it’s easy to lose track of what’s actually running in your environment. After a week of adding marketplace tools and writing custom local agents, I ran into two issues: Command Amnesia: Forgetting the exact names of tools and how to invoke them. Hidden Hooks: Not knowing which plugins registered PostToolUse hooks or high-risk permissions like raw Bash access. To solve this, I built plugin-audit — a tool designed to give you a clear inventory and security overview of your workspace. 🛠️ The Commands The plugin provides a complete toolkit to…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/nestedcat/i-built-an-audit-plugin-to-audit-claude-code-plugins-4oon

## Related notes
- [[2026-02-24-your-ai-agents-have-5-months-to-comply-with-the-eu-ai-act-heres-what-youre-missing]]
- [[2026-02-22-md-files-connector-stop-losing-track-of-your-markdown-docs]]
- [[2026-02-22-stop-wiring-dependencies-by-hand---meet-injectq-python-di-done-right]]
- [[2026-02-23-distributed-locking-in-python]]
- [[2026-02-25-beyond-to-do-lists-building-a-closed-loop-health-agent-with-langgraph-and-google-calendar]]
- [[2026-02-22-building-a-fully-local-offline-trading-research-memory-agent-with-zvec]]
