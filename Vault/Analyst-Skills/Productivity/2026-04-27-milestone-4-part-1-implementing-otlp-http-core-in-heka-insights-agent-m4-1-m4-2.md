---
title: 'Milestone 4 (Part 1): Implementing OTLP HTTP Core in Heka Insights Agent (M4-1,
  M4-2)'
date: '2026-04-27'
source: https://dev.to/munirfarhan/milestone-4-part-1-implementing-otlp-http-core-in-heka-insights-agent-m4-1-m4-2-2a79
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-04-06-pydantic-ai-tutorial-how-i-build-type-safe-ai-agents-that-actually-work-in-production]]'
- '[[2026-03-04-bulletproof-data-pipelines-adding-schema-validation-to-nike-scrapers]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-03-02-9-python-libraries-that-reduced-a-one-month-ai-development-cycle-to-just-3-days]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]'
status: unread
---

> **TL;DR:** Milestone 4 (Part 1): Implementing OTLP HTTP Core in Heka Insights Agent (M4-1, M4-2) Heka Insights Agent already had a canonical metrics pipeline from Milestone 3. In this part of Milestone 4, I implemented the OTLP HTT…

## What’s new and why it matters
Milestone 4 (Part 1): Implementing OTLP HTTP Core in Heka Insights Agent (M4-1, M4-2) Heka Insights Agent already had a canonical metrics pipeline from Milestone 3. In this part of Milestone 4, I implemented the OTLP HTTP core in two focused steps: M4-1 : Canonical metrics -> OTLP payload mapping layer M4-2 : OTLP HTTP request sender and exporter wiring This post covers only these two items. Auth headers, resource attributes, retry/compression controls are intentionally deferred to later M4 tasks. Why This Split Matters By separating mapping from transport, we get: stable internal metric model…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/munirfarhan/milestone-4-part-1-implementing-otlp-http-core-in-heka-insights-agent-m4-1-m4-2-2a79

## Related notes
- [[2026-04-06-pydantic-ai-tutorial-how-i-build-type-safe-ai-agents-that-actually-work-in-production]]
- [[2026-03-04-bulletproof-data-pipelines-adding-schema-validation-to-nike-scrapers]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-03-02-9-python-libraries-that-reduced-a-one-month-ai-development-cycle-to-just-3-days]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]
