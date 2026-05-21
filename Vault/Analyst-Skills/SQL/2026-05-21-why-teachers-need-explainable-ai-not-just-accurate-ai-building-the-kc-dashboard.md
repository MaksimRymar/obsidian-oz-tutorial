---
title: Why teachers need explainable AI, not just accurate AI — building the KC dashboard
date: '2026-05-21'
source: https://dev.to/orieken/why-teachers-need-explainable-ai-not-just-accurate-ai-building-the-kc-dashboard-4iga
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-05-21-attempt-history-in-the-teacher-dashboard-the-scalar-subquery-pattern]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]'
- '[[2026-05-21-prompt-engineering-for-teacher-insights-with-claude-structured-json-and-graceful-fallbacks]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]'
status: unread
---

> **TL;DR:** What We Built NumPath's teacher dashboard previously showed one number per student: 7-day accuracy. A teacher looking at "Emma — 43%" has no idea whether Emma is struggling with borrowing, place value, number sense, or a…

## What’s new and why it matters
What We Built NumPath's teacher dashboard previously showed one number per student: 7-day accuracy. A teacher looking at "Emma — 43%" has no idea whether Emma is struggling with borrowing, place value, number sense, or all three. The number is technically correct and completely unactionable. In this post I'll walk through how we added a Knowledge Component (KC) mastery panel to the dashboard — colour-coded progress bars per skill that expand to show p_mastery %, mastery level label, and opportunity count. The backend piece is a single endpoint backed by a left-join use case. The research reaso…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/orieken/why-teachers-need-explainable-ai-not-just-accurate-ai-building-the-kc-dashboard-4iga

## Related notes
- [[2026-05-21-attempt-history-in-the-teacher-dashboard-the-scalar-subquery-pattern]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]
- [[2026-05-21-prompt-engineering-for-teacher-insights-with-claude-structured-json-and-graceful-fallbacks]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-26-i-built-a-multi-agent-system-without-governance-heres-the-3-layer-stack-i-wish-id-had]]
