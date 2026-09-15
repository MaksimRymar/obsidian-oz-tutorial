---
title: Modeling Liquidity Without a Misleading Score — Johan Wirakarsa, Ph.D.
date: '2026-09-15'
source: https://dev.to/johanwirakarsaphd/modeling-liquidity-without-a-misleading-score-johan-wirakarsa-phd-238c
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-07-20-learn-configuration-precedence-with-empty-missing-and-invalid-values]]'
- '[[2026-08-12-structured-summary-json-schema-for-a-fintech-llm-code-review-api]]'
- '[[2026-07-19-a-csv-quality-report-should-not-echo-the-data-it-rejects]]'
- '[[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]'
- '[[2026-05-20-first-principles]]'
- '[[2026-08-16-keep-a-ledger-of-model-failures-instead-of-trusting-the-release-notes]]'
status: unread
---

> **TL;DR:** Consider a data model with one convenient field: liquidity_score. It is easy to sort and chart, but difficult to interpret. Does it describe market depth, funding access, or cash on a balance sheet? Those mechanisms can…

## What’s new and why it matters
Consider a data model with one convenient field: liquidity_score. It is easy to sort and chart, but difficult to interpret. Does it describe market depth, funding access, or cash on a balance sheet? Those mechanisms can move independently. One score hides the question the data should answer. A better schema keeps the distinctions visible. This Python example uses only the standard library. Its values are synthetic and demonstrate structure, not real market conditions. from dataclasses import dataclass from enum import Enum class FundingState(str, Enum): OPEN = "open" SELECTIVE = "selective" CO…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/johanwirakarsaphd/modeling-liquidity-without-a-misleading-score-johan-wirakarsa-phd-238c

## Related notes
- [[2026-07-20-learn-configuration-precedence-with-empty-missing-and-invalid-values]]
- [[2026-08-12-structured-summary-json-schema-for-a-fintech-llm-code-review-api]]
- [[2026-07-19-a-csv-quality-report-should-not-echo-the-data-it-rejects]]
- [[2026-03-10-calculating-npv-and-irr-in-python-without-numpy-or-scipy]]
- [[2026-05-20-first-principles]]
- [[2026-08-16-keep-a-ledger-of-model-failures-instead-of-trusting-the-release-notes]]
