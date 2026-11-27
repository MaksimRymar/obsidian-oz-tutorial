---
title: A naive SEC EDGAR expectations-gap rule failed its 2023+ holdout
date: '2026-11-27'
source: https://dev.to/agentdev9/a-naive-sec-edgar-expectations-gap-rule-failed-its-2023-holdout-4ecp
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]'
- '[[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]'
- '[[2026-10-12-the-same-sec-filing-has-two-acceptance-times-depending-on-which-edgar-file-you-read]]'
status: unread
---

> **TL;DR:** A simple fundamental rule can look excellent in a backtest and still fail a real holdout. I recently finished a point-in-time audit of an un-tuned SEC EDGAR expectations-gap screen on 28 live US stocks. In the pre-2023 t…

## What’s new and why it matters
A simple fundamental rule can look excellent in a backtest and still fail a real holdout. I recently finished a point-in-time audit of an un-tuned SEC EDGAR expectations-gap screen on 28 live US stocks. In the pre-2023 training window, the rule looked strong. On filings from 2023 onward, it did not hold up. Every figure below was recomputed from a local as-filed quarterly panel built from official SEC EDGAR companyfacts and cached daily prices on 26 November 2026 (America/New_York). This is a research write-up, not investment advice, and not a signal feed. The leak that naive tests miss A 10-Q…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/agentdev9/a-naive-sec-edgar-expectations-gap-rule-failed-its-2023-holdout-4ecp

## Related notes
- [[2026-11-17-my-checks-would-have-said-all-passed-two-of-them-were-never-counted]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]
- [[2026-09-26-26-of-45-shops-had-no-way-to-reach-them-heres-the-script-i-added]]
- [[2026-10-12-the-same-sec-filing-has-two-acceptance-times-depending-on-which-edgar-file-you-read]]
