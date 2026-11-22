---
title: 'The same workload cost ¥43,712 or ¥45,767: auditing an LLM cost ledger that
  disagrees with itself'
date: '2026-11-22'
source: https://dev.to/soccerdream_ai/the-same-workload-cost-y43712-or-y45767-auditing-an-llm-cost-ledger-that-disagrees-with-itself-53j9
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]'
- '[[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
status: unread
---

> **TL;DR:** Every team shipping LLM features builds a per-call log, a daily aggregate and a dashboard, at different times and from different assumptions. Then someone asks "what did last month cost" and you get two numbers four perc…

## What’s new and why it matters
Every team shipping LLM features builds a per-call log, a daily aggregate and a dashboard, at different times and from different assumptions. Then someone asks "what did last month cost" and you get two numbers four percent apart, with nobody able to say which is right. This is an audit of that situation: 2.3 million model calls over three months, one line-item table, one rollup table, and a disagreement of ¥2,055.24. The interesting part is not the gap's size but that it decomposes into a deletion and a freeze, while everything else reconciles to the cent. Two grains of truth ai_call_logs hol…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/soccerdream_ai/the-same-workload-cost-y43712-or-y45767-auditing-an-llm-cost-ledger-that-disagrees-with-itself-53j9

## Related notes
- [[2026-09-08-charge-wait-time-to-the-same-job]]
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-10-27-48-hour-field-notes-my-prompt-budget-was-in-characters-and-the-overflow-never-raised]]
- [[2026-08-30-sql-date-functions-how-to-group-by-month-without-losing-one]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
