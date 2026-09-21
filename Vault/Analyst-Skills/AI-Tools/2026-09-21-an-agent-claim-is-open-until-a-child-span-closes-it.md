---
title: An Agent Claim Is Open Until a Child Span Closes It
date: '2026-09-21'
source: https://dev.to/codepro_3283/an-agent-claim-is-open-until-a-child-span-closes-it-1g9b
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
- '[[2026-09-07-gate-agent-success-on-closed-spans]]'
- '[[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
status: unread
---

> **TL;DR:** An assistant transcript is a press release. A child span is a receipt. If the model says it ran the test suite and the trace has no child span for that tool under the generation that made the claim, the run is not done.…

## What’s new and why it matters
An assistant transcript is a press release. A child span is a receipt. If the model says it ran the test suite and the trace has no child span for that tool under the generation that made the claim, the run is not done. The claim is still open, the same way a merge request stays open when CI never started. Teams keep scoring agent runs from the last paragraph of the chat. That paragraph is generated text. It can describe a successful pytest invocation, a patched module, and a green exit code while the tool layer never executed. Walk the span tree instead of grading the prose, and the mismatch…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/codepro_3283/an-agent-claim-is-open-until-a-child-span-closes-it-1g9b

## Related notes
- [[2026-09-08-charge-wait-time-to-the-same-job]]
- [[2026-09-07-gate-agent-success-on-closed-spans]]
- [[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
