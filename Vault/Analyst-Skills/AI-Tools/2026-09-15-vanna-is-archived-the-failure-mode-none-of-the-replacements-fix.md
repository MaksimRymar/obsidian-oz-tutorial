---
title: Vanna is archived. The failure mode none of the replacements fix.
date: '2026-09-15'
source: https://dev.to/ashish_sinha_5241c7673d93/vanna-is-archived-the-failure-mode-none-of-the-replacements-fix-4l3i
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#career'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
- '[[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]'
- '[[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]'
- '[[2026-06-17-how-to-add-policy-enforcement-to-a-langgraph-agent-before-it-does-something-dumb]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
status: unread
---

> **TL;DR:** Someone in finance asks your text-to-SQL agent what the compensation band is for a role they're hiring for. The agent writes correct SQL. The query runs. Row-level security strips every row. The user is told: No records…

## What’s new and why it matters
Someone in finance asks your text-to-SQL agent what the compensation band is for a role they're hiring for. The agent writes correct SQL. The query runs. Row-level security strips every row. The user is told: No records found. That answer is wrong, and it is wrong in the worst available way. There are records. The user simply isn't allowed to see them. Nothing in the chain can tell the difference between "this data does not exist" and "you may not have this data" — so the system picks the first and says it with confidence. Your logs show a successful query. Your RLS policy shows it working exa…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/ashish_sinha_5241c7673d93/vanna-is-archived-the-failure-mode-none-of-the-replacements-fix-4l3i

## Related notes
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
- [[2026-08-28-an-erd-mcp-server-ai-agents-that-follow-your-naming-standard]]
- [[2026-08-11-the-text-to-sql-demo-takes-an-afternoon-the-other-90-is-why-you-should-buy-it]]
- [[2026-06-17-how-to-add-policy-enforcement-to-a-langgraph-agent-before-it-does-something-dumb]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
