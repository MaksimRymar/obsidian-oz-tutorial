---
title: 'I built AegisBrain: A local memory bus and token arbitrage engine for AI coding
  agents'
date: '2026-11-10'
source: https://dev.to/priyanshu_ghosh_bed532788/i-built-aegisbrain-a-local-memory-bus-and-token-arbitrage-engine-for-ai-coding-agents-4ml9
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-27-same-feature-two-diffs-100-vs-57-i-built-a-gate-that-scores-ai-code-changes]]'
- '[[2026-10-19-i-built-a-workflow-that-checks-whether-my-ai-agents-context-was-enough-then-proves-it-with-my-own-tests]]'
- '[[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]'
- '[[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]'
- '[[2026-08-10-sqlite-fts5-is-faster-than-whoosh-so-why-would-you-ever-use-a-pure-python-search-engine]]'
- '[[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]'
status: unread
---

> **TL;DR:** I built AegisBrain (GPLv3) to solve two practical frustrations I kept encountering while using AI coding agents (Claude Code, Gemini CLI, Cursor, and Antigravity): Context Amnesia & Token Waste: Every time an agent start…

## What’s new and why it matters
I built AegisBrain (GPLv3) to solve two practical frustrations I kept encountering while using AI coding agents (Claude Code, Gemini CLI, Cursor, and Antigravity): Context Amnesia & Token Waste: Every time an agent starts a new session or compacts context, it typically crawls multi-megabyte JSONL session transcripts (often 40k–60k tokens) just to recall past architectural decisions, rules, and invariants. This wastes tokens and increases latency. Frontier Token Waste on Boilerplate: Paying frontier model API pricing to generate repetitive boilerplate, DTOs, and unit test suites felt inefficien…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/priyanshu_ghosh_bed532788/i-built-aegisbrain-a-local-memory-bus-and-token-arbitrage-engine-for-ai-coding-agents-4ml9

## Related notes
- [[2026-10-27-same-feature-two-diffs-100-vs-57-i-built-a-gate-that-scores-ai-code-changes]]
- [[2026-10-19-i-built-a-workflow-that-checks-whether-my-ai-agents-context-was-enough-then-proves-it-with-my-own-tests]]
- [[2026-07-30-i-wrote-integration-tests-for-my-mcp-failure-library-heres-the-pattern-that-caught-3-hidden-bugs]]
- [[2026-10-06-mcp-vs-custom-rest-tooling-security-and-the-latest-mcp-architecture]]
- [[2026-08-10-sqlite-fts5-is-faster-than-whoosh-so-why-would-you-ever-use-a-pure-python-search-engine]]
- [[2026-03-17-i-built-a-cognitive-layer-for-ai-agents-that-learns-without-llm-calls]]
