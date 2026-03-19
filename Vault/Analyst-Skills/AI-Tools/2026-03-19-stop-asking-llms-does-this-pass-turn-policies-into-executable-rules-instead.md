---
title: Stop Asking LLMs “Does This Pass?” — Turn Policies Into Executable Rules Instead
date: '2026-03-19'
source: https://dev.to/kanwaloswal/stop-asking-llms-does-this-pass-turn-policies-into-executable-rules-instead-16of
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-03-18-building-cddbs-part-3-scoring-llm-output-without-another-llm]]'
- '[[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]'
- '[[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]'
- '[[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]'
- '[[2026-03-17-surrealdb-why-joins-are-so-2010-and-how-graphs-change-everything-part-3]]'
status: unread
---

> **TL;DR:** If you’ve worked with LLMs in real systems, you’ve probably tried something like this: “Here’s a policy document. Here’s some input data. Does this meet the policy?” It works surprisingly well… at first. But as soon as y…

## What’s new and why it matters
If you’ve worked with LLMs in real systems, you’ve probably tried something like this: “Here’s a policy document. Here’s some input data. Does this meet the policy?” It works surprisingly well… at first. But as soon as you move beyond demos, a few problems start to show up: Results vary depending on phrasing or context It’s hard to explain why a decision was made The only audit trail is prompt + response Re-running the same input doesn’t always guarantee the same output This becomes a real issue in domains like: financial services compliance eligibility systems underwriting Where decisions nee…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kanwaloswal/stop-asking-llms-does-this-pass-turn-policies-into-executable-rules-instead-16of

## Related notes
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-03-18-building-cddbs-part-3-scoring-llm-output-without-another-llm]]
- [[2026-03-10-building-an-ai-tool-that-generates-sql-queries-from-natural-language]]
- [[2026-03-01-stop-manually-entering-medical-data-how-to-automate-pdf-lab-reports-with-layoutparser-ocr]]
- [[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]
- [[2026-03-17-surrealdb-why-joins-are-so-2010-and-how-graphs-change-everything-part-3]]
