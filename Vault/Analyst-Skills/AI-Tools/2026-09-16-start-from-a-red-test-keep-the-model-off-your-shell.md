---
title: Start From a Red Test. Keep the Model Off Your Shell.
date: '2026-09-16'
source: https://dev.to/aiio_8140/start-from-a-red-test-keep-the-model-off-your-shell-p4d
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-09-pin-agent-tools-to-a-checked-in-schema-before-the-first-call]]'
- '[[2026-09-08-your-agent-will-invent-timeouts-pin-them-in-a-contract-test-first]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-09-11-scratch-box-the-agent-loop-promote-the-diff-only-when-the-hash-matches]]'
status: unread
---

> **TL;DR:** The model does not get a shell. It does not get your working tree. It gets a failing test node, a handful of AST signatures, and a path allowlist. You keep merge. Want the agent to “just fix the repo”? That is how a help…

## What’s new and why it matters
The model does not get a shell. It does not get your working tree. It gets a failing test node, a handful of AST signatures, and a path allowlist. You keep merge. Want the agent to “just fix the repo”? That is how a helper rewrite deletes a fixture and “simplifies” your config. Engineering is the gate, not the prompt. This walkthrough is a from-zero loop you can run on a laptop. Each stage has a command and a pass/fail check. No fake latency numbers. No invented model names. What you will have when it works A tiny broken Python package. A red pytest node that you wrote by hand. A job file that…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aiio_8140/start-from-a-red-test-keep-the-model-off-your-shell-p4d

## Related notes
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-09-pin-agent-tools-to-a-checked-in-schema-before-the-first-call]]
- [[2026-09-08-your-agent-will-invent-timeouts-pin-them-in-a-contract-test-first]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-09-11-scratch-box-the-agent-loop-promote-the-diff-only-when-the-hash-matches]]
