---
title: Scratch-Box the Agent Loop. Promote the Diff Only When the Hash Matches.
date: '2026-09-11'
source: https://dev.to/aiio_8140/scratch-box-the-agent-loop-promote-the-diff-only-when-the-hash-matches-bhn
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-13-stop-asking-coding-models-to-write-code-test-whether-they-can-review-a-patch]]'
- '[[2026-09-03-prove-every-readme-command-before-you-let-a-model-rewrite-it]]'
- '[[2026-09-09-pin-agent-tools-to-a-checked-in-schema-before-the-first-call]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
status: unread
---

> **TL;DR:** Stop applying agent diffs on the laptop that holds your secrets. Freeze a fixture, run the loop on a scratch box, and promote the tree only when the output hash matches the lock you already checked in. Everything else is…

## What’s new and why it matters
Stop applying agent diffs on the laptop that holds your secrets. Freeze a fixture, run the loop on a scratch box, and promote the tree only when the output hash matches the lock you already checked in. Everything else is theater. You already know the failure. A free remote model “fixes” a test. It also rewrites a Makefile target you still needed, and git status looks like a yard sale. Why would you let an untrusted compiler write into the same tree you deploy from? This is a from-zero walkthrough. Each stage has a command and a verification step. The model never touches your working copy. It e…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aiio_8140/scratch-box-the-agent-loop-promote-the-diff-only-when-the-hash-matches-bhn

## Related notes
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-13-stop-asking-coding-models-to-write-code-test-whether-they-can-review-a-patch]]
- [[2026-09-03-prove-every-readme-command-before-you-let-a-model-rewrite-it]]
- [[2026-09-09-pin-agent-tools-to-a-checked-in-schema-before-the-first-call]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
