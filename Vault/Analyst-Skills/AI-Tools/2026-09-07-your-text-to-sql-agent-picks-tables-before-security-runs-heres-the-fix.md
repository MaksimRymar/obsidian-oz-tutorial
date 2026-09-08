---
title: Your text-to-SQL agent picks tables before security runs. Here’s the fix.
date: '2026-09-07'
source: https://dev.to/ashish_sinha_5241c7673d93/your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix-11bb
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#sql'
- '#tool'
related:
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]'
- '[[2026-08-06-explain-plan-as-a-lint-for-llm-generated-sql]]'
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** I build text-to-SQL agents on Oracle and Postgres for a living. Every one of them had the same bug, and it wasn’t in my code. It was in the order of operations. The bug The schema goes into the prompt before the query ru…

## What’s new and why it matters
I build text-to-SQL agents on Oracle and Postgres for a living. Every one of them had the same bug, and it wasn’t in my code. It was in the order of operations. The bug The schema goes into the prompt before the query runs. Row-level security runs when the query runs. So the model sees a table the user can’t read, writes perfectly valid SQL against it, the database returns zero rows, and the agent says “no records found”. A wrong answer, delivered with confidence. Vanna (23k stars, archived March 2026) applied identity exactly there: at execution, after the model had seen everything. The fix A…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ashish_sinha_5241c7673d93/your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix-11bb

## Related notes
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-08-31-running-total-in-sql-the-window-frame-that-decides-the-answer]]
- [[2026-08-06-explain-plan-as-a-lint-for-llm-generated-sql]]
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
