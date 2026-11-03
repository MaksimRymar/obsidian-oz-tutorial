---
title: 'Know What Your Agent''s Tools Can Do to You: Scanning MCP Servers Before You
  Install Them'
date: '2026-11-03'
source: https://dev.to/ranadhir19/know-what-your-agents-tools-can-do-to-you-scanning-mcp-servers-before-you-install-them-21jk
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#python'
- '#tool'
related:
- '[[2026-09-03-building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]'
- '[[2026-08-02-i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys]]'
- '[[2026-10-19-bulk-generate-images-from-a-list-of-prompts-with-one-api-call-flux-no-api-key]]'
- '[[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]'
status: unread
---

> **TL;DR:** In an April 2026 audit, 27 detections from MCP security scanners boiled down to 6 genuine concerns. The scanners weren't missing attacks — they were crying wolf, which in a CI pipeline is the same failure wearing a diffe…

## What’s new and why it matters
In an April 2026 audit, 27 detections from MCP security scanners boiled down to 6 genuine concerns. The scanners weren't missing attacks — they were crying wolf, which in a CI pipeline is the same failure wearing a different coat. So I built a scanner whose first feature is its own error profile: every rule publishes a measured precision from a labelled corpus of planted positives and near-miss traps. This is how it works, what it catches — tool poisoning, rug pulls, dangerous sinks, hardcoded secrets — and where its numbers say it still gets things wrong. One command before you install Sentin…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ranadhir19/know-what-your-agents-tools-can-do-to-you-scanning-mcp-servers-before-you-install-them-21jk

## Related notes
- [[2026-09-03-building-an-ast-code-verifier-without-networkx-gitpython-or-any-dependencies]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-06-15-a-40-line-llm-based-bash-command-executor-in-python]]
- [[2026-08-02-i-built-an-open-source-osint-tool-that-runs-55-modules-with-zero-api-keys]]
- [[2026-10-19-bulk-generate-images-from-a-list-of-prompts-with-one-api-call-flux-no-api-key]]
- [[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]
