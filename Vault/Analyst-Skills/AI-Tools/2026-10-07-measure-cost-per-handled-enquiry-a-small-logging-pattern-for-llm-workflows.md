---
title: 'Measure Cost per Handled Enquiry: A Small Logging Pattern for LLM Workflows'
date: '2026-10-07'
source: https://dev.to/ujjwal_dubey_9/measure-cost-per-handled-enquiry-a-small-logging-pattern-for-llm-workflows-51ni
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]'
- '[[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]'
- '[[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]'
- '[[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** Pre-build cost estimates are guesses. After launch you can measure. The most useful number I know for a small-business workflow is cost per handled enquiry in AI automation : everything it cost to take one customer messa…

## What’s new and why it matters
Pre-build cost estimates are guesses. After launch you can measure. The most useful number I know for a small-business workflow is cost per handled enquiry in AI automation : everything it cost to take one customer message from arrival to a resolved state. Disclosure: I run NxFlowAI, an automation agency. The pattern below is generic. What to count For each enquiry, record: model tokens in and out (per call) messaging events (per message sent, by category, using your provider's billing categories) automation-platform runs or tasks human minutes (time spent approving or rewriting a draft) A min…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ujjwal_dubey_9/measure-cost-per-handled-enquiry-a-small-logging-pattern-for-llm-workflows-51ni

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]
- [[2026-08-11-stop-doing-it-manually-7-ai-automation-workflows-worth-building-this-weekend]]
- [[2026-08-31-subquery-vs-cte-in-sql-same-logic-one-you-can-check]]
- [[2026-09-12-a-30-line-wrapper-that-tells-you-what-every-llm-call-actually-costs]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
