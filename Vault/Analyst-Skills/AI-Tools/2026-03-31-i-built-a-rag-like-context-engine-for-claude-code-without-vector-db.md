---
title: I Built a RAG-like Context Engine for Claude Code — Without Vector DB
date: '2026-03-31'
source: https://dev.to/leokim_kr/i-built-a-rag-like-context-engine-for-claude-code-without-vector-db-3k0b
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]'
- '[[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]'
- '[[2026-02-22-agent-memory-a-zero-dependency-memory-system-for-ai-agents]]'
- '[[2026-03-04-how-i-stopped-my-ai-agents-from-getting-dumber-after-10-turns]]'
status: unread
---

> **TL;DR:** The Problem Claude Code reads your CLAUDE.md once at session start. But here's the thing — Vercel's engineering team found that skills-based retrieval was skipped in 56% of eval cases . The model simply didn't invoke the…

## What’s new and why it matters
The Problem Claude Code reads your CLAUDE.md once at session start. But here's the thing — Vercel's engineering team found that skills-based retrieval was skipped in 56% of eval cases . The model simply didn't invoke them. I run Claude Code as my daily coding assistant across 26+ custom resources. After months of watching Claude forget rules, ignore conventions, and skip critical project knowledge, I built a system to fix it. The Solution: Context Feeder Context Feeder is a lightweight context injection engine that runs on Claude Code hooks. It doesn't ask the model what's relevant — it force-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/leokim_kr/i-built-a-rag-like-context-engine-for-claude-code-without-vector-db-3k0b

## Related notes
- [[2026-03-09-i-built-a-real-time-dashboard-for-claude-code-because-i-kept-losing-track-of-my-sessions]]
- [[2026-03-10-build-a-persistent-ai-agent-in-5-minutes-with-python]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]
- [[2026-02-22-agent-memory-a-zero-dependency-memory-system-for-ai-agents]]
- [[2026-03-04-how-i-stopped-my-ai-agents-from-getting-dumber-after-10-turns]]
