---
title: How to Compress Noisy CI/CD and Production Logs Without Losing Stack Traces
  or Exit Codes
date: '2026-11-16'
source: https://dev.to/umutgungor/how-to-compress-noisy-cicd-and-production-logs-without-losing-stack-traces-or-exit-codes-2li2
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#library'
- '#productivity'
- '#python'
- '#tutorial'
related:
- '[[2026-10-24-a-budget-guard-for-llm-agents-in-40-lines-of-python-written-by-an-agent-that-dies-at-0]]'
- '[[2026-11-07-from-database-tables-to-long-term-memory-with-hindsight]]'
- '[[2026-09-18-the-rag-pipeline-i-wouldnt-build-the-same-way-twice]]'
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]'
- '[[2026-11-11-stop-writing-slow-loops-5-vectorized-python-scripts-every-quant-algo-trader-needs-in-2026]]'
status: unread
---

> **TL;DR:** When a test runner, Docker build, or dependency step emits thousands of repeated status lines, ANSI progress-bar redraws, or ConnectionResetError retries, the actual traceback gets buried under megabytes of repetitive sc…

## What’s new and why it matters
When a test runner, Docker build, or dependency step emits thousands of repeated status lines, ANSI progress-bar redraws, or ConnectionResetError retries, the actual traceback gets buried under megabytes of repetitive scrollback. Ad-hoc grep -v or tail -n 200 pipes introduce two dangerous bugs: they slice away surrounding context needed for root-cause triage, and naive shell pipes can swallow the upstream command's non-zero exit code, turning a broken build falsely green. Step 1: Deduplicate repetitive stdout/stderr streams in constant memory A practical stream compressor reads line-by-line fr…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/umutgungor/how-to-compress-noisy-cicd-and-production-logs-without-losing-stack-traces-or-exit-codes-2li2

## Related notes
- [[2026-10-24-a-budget-guard-for-llm-agents-in-40-lines-of-python-written-by-an-agent-that-dies-at-0]]
- [[2026-11-07-from-database-tables-to-long-term-memory-with-hindsight]]
- [[2026-09-18-the-rag-pipeline-i-wouldnt-build-the-same-way-twice]]
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-06-02-claude-api-from-scratch-your-first-working-call-in-30-minutes-2026]]
- [[2026-11-11-stop-writing-slow-loops-5-vectorized-python-scripts-every-quant-algo-trader-needs-in-2026]]
