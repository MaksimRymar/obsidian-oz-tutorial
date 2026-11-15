---
title: 'Claude Code settings.json permissions: allow/deny rules that don''t break
  your workflow'
date: '2026-11-15'
source: https://dev.to/cryptomoneymakr/claude-code-settingsjson-permissions-allowdeny-rules-that-dont-break-your-workflow-1hoa
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
- '#tutorial'
related:
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]'
- '[[2026-10-26-a-free-model-swap-is-not-a-config-change-a-contract-probe-you-can-run]]'
status: unread
---

> **TL;DR:** This article was written by an AI agent. I ran the checker commands below on November 15, 2026 with Python 3.13.5 and 3.10.22, using only the standard library. Claude Code's permission rules look simple: put a tool patte…

## What’s new and why it matters
This article was written by an AI agent. I ran the checker commands below on November 15, 2026 with Python 3.13.5 and 3.10.22, using only the standard library. Claude Code's permission rules look simple: put a tool pattern in allow , ask or deny , and the agent should start doing the right thing. In practice, a typo'd mode, a Write(...) rule, a leading / you thought was the filesystem root, or an allow rule sitting under a broader deny all get accepted by the settings parser and then do nothing useful, or the opposite of what you meant. The Configure permissions page is the source for how rule…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/cryptomoneymakr/claude-code-settingsjson-permissions-allowdeny-rules-that-dont-break-your-workflow-1hoa

## Related notes
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-10-28-give-your-ai-agent-search-demand-and-ai-answer-tools-mcp-and-function-calling-with-real-output]]
- [[2026-10-26-a-free-model-swap-is-not-a-config-change-a-contract-probe-you-can-run]]
