---
title: Pin Exit Codes Before You Extract One CLI Flag
date: '2026-09-12'
source: https://dev.to/hackrs_6393/pin-exit-codes-before-you-extract-one-cli-flag-499l
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-03-record-four-cli-channels-before-you-change-one-flag]]'
- '[[2026-09-06-a-behavior-ledger-makes-one-file-refactors-honest]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-09-05-hash-the-entrypoint-before-you-extract-one-module]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
status: unread
---

> **TL;DR:** Do not extract a CLI flag from messy code first. Freeze the exit codes and stderr tokens first. Characterization tests make that freeze cheap and repeatable. Messy CLIs fail refactors in three silent ways. Exit codes dri…

## What’s new and why it matters
Do not extract a CLI flag from messy code first. Freeze the exit codes and stderr tokens first. Characterization tests make that freeze cheap and repeatable. Messy CLIs fail refactors in three silent ways. Exit codes drift while callers keep old scripts. Stderr tokens vanish when a logger gets cleaned. Stdout JSON can also shuffle keys after a tiny helper extract. Scripts that parse both streams then fail in CI only. You need a contract that is smaller than the full transcript. The contract that matters A CLI contract is not the source layout. It is the process boundary callers already depend…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hackrs_6393/pin-exit-codes-before-you-extract-one-cli-flag-499l

## Related notes
- [[2026-09-03-record-four-cli-channels-before-you-change-one-flag]]
- [[2026-09-06-a-behavior-ledger-makes-one-file-refactors-honest]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-09-05-hash-the-entrypoint-before-you-extract-one-module]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
