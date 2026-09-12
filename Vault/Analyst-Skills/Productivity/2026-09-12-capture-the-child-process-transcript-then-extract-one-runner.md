---
title: Capture the Child Process Transcript. Then Extract One Runner.
date: '2026-09-12'
source: https://dev.to/hackrs_6393/capture-the-child-process-transcript-then-extract-one-runner-422h
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-03-record-four-cli-channels-before-you-change-one-flag]]'
- '[[2026-09-06-a-behavior-ledger-makes-one-file-refactors-honest]]'
- '[[2026-09-08-ledger-one-entrypoint-before-you-touch-the-mess]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
status: unread
---

> **TL;DR:** A child-process wrapper hides a four-part contract. Argv, cwd, env, and streams must stay stable. Extract a runner only after transcript tests lock them. Messy modules wrap subprocess.run in ad-hoc helpers. Those helpers…

## What’s new and why it matters
A child-process wrapper hides a four-part contract. Argv, cwd, env, and streams must stay stable. Extract a runner only after transcript tests lock them. Messy modules wrap subprocess.run in ad-hoc helpers. Those helpers then grow flags and path hacks. Reviewers later accept a cleanup that reorders argv. Production then fails on a missing env key. Stderr order can also flip under check=True. The failure looks random without a frozen transcript. This workflow records one golden transcript first. It then allows one runner extract. The method stays local, testable, and intentionally small. The fo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hackrs_6393/capture-the-child-process-transcript-then-extract-one-runner-422h

## Related notes
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-03-record-four-cli-channels-before-you-change-one-flag]]
- [[2026-09-06-a-behavior-ledger-makes-one-file-refactors-honest]]
- [[2026-09-08-ledger-one-entrypoint-before-you-touch-the-mess]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
