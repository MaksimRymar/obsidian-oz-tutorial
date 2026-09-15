---
title: 'Nano Banana 2 Lite in Kiro CLI 3: MCP 2.0, the New Interactions API, and Headless
  Permissions'
date: '2026-09-15'
source: https://dev.to/aws-builders/nano-banana-2-lite-in-kiro-cli-3-mcp-20-the-new-interactions-api-and-headless-permissions-hhb
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-08-10-my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]'
- '[[2026-09-10-i-got-tired-of-my-ai-agents-fighting-over-one-repo-so-i-built-taskpods]]'
status: unread
---

> **TL;DR:** This article provides a step by step update guide for a Python MCP server that drives Google Nano Banana 2 Lite ( gemini-3.1-flash-lite-image ) through the Gemini Interactions API, running inside Kiro CLI 3. Two dependen…

## What’s new and why it matters
This article provides a step by step update guide for a Python MCP server that drives Google Nano Banana 2 Lite ( gemini-3.1-flash-lite-image ) through the Gemini Interactions API, running inside Kiro CLI 3. Two dependency lines moved underneath the server: the MCP Python SDK went to 2.x, and the Interactions API dropped the schema that google-genai 1.x speaks. The server is then registered with Kiro, given a permission rule, and validated end to end against the live API from a headless Kiro 3 session. https://github.com/xbill9/nb2lite-kiro Haven't You Done This One Before? What is old is new…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aws-builders/nano-banana-2-lite-in-kiro-cli-3-mcp-20-the-new-interactions-api-and-headless-permissions-hhb

## Related notes
- [[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-08-10-my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]
- [[2026-09-10-i-got-tired-of-my-ai-agents-fighting-over-one-repo-so-i-built-taskpods]]
