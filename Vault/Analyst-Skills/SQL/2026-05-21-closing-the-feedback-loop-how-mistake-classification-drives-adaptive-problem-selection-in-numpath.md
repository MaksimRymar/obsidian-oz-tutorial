---
title: 'Closing the feedback loop: how mistake classification drives adaptive problem
  selection in NumPath'
date: '2026-05-21'
source: https://dev.to/orieken/closing-the-feedback-loop-how-mistake-classification-drives-adaptive-problem-selection-in-numpath-5ce9
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-21-why-teachers-need-explainable-ai-not-just-accurate-ai-building-the-kc-dashboard]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-05-21-attempt-history-in-the-teacher-dashboard-the-scalar-subquery-pattern]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
status: unread
---

> **TL;DR:** What We Built NumPath is an AI math tutor for children with dyscalculia. At its core is an adaptive engine that picks the next problem for each student based on their Bayesian Knowledge Tracing (BKT) mastery estimate. In…

## What’s new and why it matters
What We Built NumPath is an AI math tutor for children with dyscalculia. At its core is an adaptive engine that picks the next problem for each student based on their Bayesian Knowledge Tracing (BKT) mastery estimate. In this post I'll walk through a problem we had — and solved — in the rule-based phase: classified mistakes were being logged but completely ignored by the selection engine. The fix was a 60-line change across two files. The research implication is significant. The Problem: a diagnostic signal going nowhere Our MistakeClassifier already tagged every wrong answer with a structured…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/orieken/closing-the-feedback-loop-how-mistake-classification-drives-adaptive-problem-selection-in-numpath-5ce9

## Related notes
- [[2026-05-21-why-teachers-need-explainable-ai-not-just-accurate-ai-building-the-kc-dashboard]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-05-21-attempt-history-in-the-teacher-dashboard-the-scalar-subquery-pattern]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
