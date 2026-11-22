---
title: Why Claude Code Loses Context After /compact (And How Bi-Temporal Graph Memory
  + AST Drift Locks Fix It)
date: '2026-11-22'
source: https://dev.to/bennialencar/why-claude-code-loses-context-after-compact-and-how-bi-temporal-graph-memory-ast-drift-locks-5fpb
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-07-01-ql-ai-database-solutions-building-a-text-to-sql-pipeline-you-can-actually-run]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]'
status: unread
---

> **TL;DR:** By **Benni Alencar * — Chief AI Systems Architect at Benni OS . Canonical article & interactive benchmarks at benni-os.net .* 1. The Post-Compaction Amnesia Cliff Every engineer running long refactoring or feature-build…

## What’s new and why it matters
By **Benni Alencar * — Chief AI Systems Architect at Benni OS . Canonical article & interactive benchmarks at benni-os.net .* 1. The Post-Compaction Amnesia Cliff Every engineer running long refactoring or feature-build sessions in Claude Code hits the exact same cliff around turn 40. The context meter climbs past 85%, you run /compact (or auto-compaction triggers), and for the next three turns everything looks fine—until the agent silently re-introduces an ORM pattern you explicitly banned 25 minutes ago, mutates a frozen API response schema, or re-attempts a Redis locking strategy you alread…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/bennialencar/why-claude-code-loses-context-after-compact-and-how-bi-temporal-graph-memory-ast-drift-locks-5fpb

## Related notes
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-07-01-ql-ai-database-solutions-building-a-text-to-sql-pipeline-you-can-actually-run]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-11-13-5-sql-mistakes-that-return-the-wrong-number-with-no-error-reproduce-each-one-in-postgres]]
