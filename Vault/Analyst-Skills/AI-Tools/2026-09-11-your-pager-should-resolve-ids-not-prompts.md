---
title: Your Pager Should Resolve IDs, Not Prompts
date: '2026-09-11'
source: https://dev.to/appcpp_9071/your-pager-should-resolve-ids-not-prompts-3o16
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-09-09-t0-is-observe-only-bind-alert-classes-to-a-clock-and-a-command-budget]]'
- '[[2026-09-08-make-escalation-cheaper-than-restart-a-three-lane-on-call-runbook]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
status: unread
---

> **TL;DR:** Your pager should resolve a catalog ID, not a prompt, and that is the whole runbook. If the alert class has no pinned command, you do not improvise inside a production shell. You escalate with the catalog hash, and you k…

## What’s new and why it matters
Your pager should resolve a catalog ID, not a prompt, and that is the whole runbook. If the alert class has no pinned command, you do not improvise inside a production shell. You escalate with the catalog hash, and you keep the mutating path closed until a human pins again. Drafts belong on a laptop at a desk, not in a root shell while error budgets burn. Why does this keep coming up? Agent-style loops are fashionable, and they look helpful until they invent kubectl flags from a guess. Are you really going to let a completion model choose selectors while customers are paging you? I am not, and…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/appcpp_9071/your-pager-should-resolve-ids-not-prompts-3o16

## Related notes
- [[2026-09-09-t0-is-observe-only-bind-alert-classes-to-a-clock-and-a-command-budget]]
- [[2026-09-08-make-escalation-cheaper-than-restart-a-three-lane-on-call-runbook]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-09-08-charge-wait-time-to-the-same-job]]
