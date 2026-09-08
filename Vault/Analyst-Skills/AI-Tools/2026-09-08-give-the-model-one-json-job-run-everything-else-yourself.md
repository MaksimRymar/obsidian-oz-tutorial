---
title: Give the Model One JSON Job. Run Everything Else Yourself.
date: '2026-09-08'
source: https://dev.to/aiio_8140/give-the-model-one-json-job-run-everything-else-yourself-26ie
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-08-17-build-a-tiny-model-ledger-before-spending-free-tokens]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
status: unread
---

> **TL;DR:** Most agent messes are not “the model is dumb.” The model was allowed to drive the whole loop. Planning, file edits, test commands, retries. All of it. That is how invented paths and silent extra files show up. So I stopp…

## What’s new and why it matters
Most agent messes are not “the model is dumb.” The model was allowed to drive the whole loop. Planning, file edits, test commands, retries. All of it. That is how invented paths and silent extra files show up. So I stopped doing that. The model gets one job: fill a JSON contract. Then a local validator, a path allowlist, and ordinary git/test commands do the rest. If the contract is wrong, nothing is written. Fail closed. Boring on purpose. Why wrap a language model around git and pytest at all? Those tools already know how to say no. What this tutorial builds A from-zero pipeline you can run…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aiio_8140/give-the-model-one-json-job-run-everything-else-yourself-26ie

## Related notes
- [[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-08-17-build-a-tiny-model-ledger-before-spending-free-tokens]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-06-a-select-only-prompt-is-not-a-sandbox-bounding-agent-generated-sql]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
