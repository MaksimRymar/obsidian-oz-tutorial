---
title: We caught our own AI security scanner making up vulnerabilities
date: '2026-10-06'
source: https://dev.to/adith_biji_2227c916082ddd/we-caught-our-own-ai-security-scanner-making-up-vulnerabilities-e6i
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-01-my-code-reviewer-scored-a-nonexistent-directory-100100-and-exited-0]]'
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-08-10-my-ai-agent-found-a-5-sigma-result-on-day-one-i-deleted-it]]'
status: unread
---

> **TL;DR:** SecFoo is an open-source CLI that runs AI coding agents (Claude, Copilot, Codex, or a plain API key) as security reviewers against your codebase, tracks findings over time, and serves a local dashboard. One of the agent…

## What’s new and why it matters
SecFoo is an open-source CLI that runs AI coding agents (Claude, Copilot, Codex, or a plain API key) as security reviewers against your codebase, tracks findings over time, and serves a local dashboard. One of the agent options — call it secfoo — is supposed to work with nothing but an OpenAI/Anthropic/Gemini API key, no coding-agent CLI installed. While testing it end-to-end, we found it was fabricating entire security reports. What we found We ran it against a small, intentionally-vulnerable Flask app (the whole codebase is one file, app.py ) and asked it to do a SAST scan. It came back with…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/adith_biji_2227c916082ddd/we-caught-our-own-ai-security-scanner-making-up-vulnerabilities-e6i

## Related notes
- [[2026-10-01-my-code-reviewer-scored-a-nonexistent-directory-100100-and-exited-0]]
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-08-10-my-ai-agent-found-a-5-sigma-result-on-day-one-i-deleted-it]]
