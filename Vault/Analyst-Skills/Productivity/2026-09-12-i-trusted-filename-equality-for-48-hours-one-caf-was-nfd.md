---
title: I Trusted Filename Equality for 48 Hours. One café Was NFD.
date: '2026-09-12'
source: https://dev.to/codepy_1473/i-trusted-filename-equality-for-48-hours-one-cafe-was-nfd-3oci
domain: Productivity
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-03-the-script-exited-0-on-my-laptop-the-free-server-returned-127]]'
- '[[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]'
- '[[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
status: unread
---

> **TL;DR:** I spent a full forty-eight hours staring at one static folder that refused to match between two machines. The chat preview showed café-logo.png in both trees, and my tired eyes agreed with that preview. Did I really need…

## What’s new and why it matters
I spent a full forty-eight hours staring at one static folder that refused to match between two machines. The chat preview showed café-logo.png in both trees, and my tired eyes agreed with that preview. Did I really need another listdir pass after the rename helper landed in the generated patch? I thought a visual match was enough evidence, and that lazy assumption burned two working days. The loader used a plain Python string as a dict key, then called Path.exists() on a concatenated name. Locally the file looked present, and the unit test that used the same literal stayed green. On the secon…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codepy_1473/i-trusted-filename-equality-for-48-hours-one-cafe-was-nfd-3oci

## Related notes
- [[2026-09-03-the-script-exited-0-on-my-laptop-the-free-server-returned-127]]
- [[2026-08-18-a-generated-sql-query-got-faster-by-returning-fewer-rows-test-that-before-you-merge-it]]
- [[2026-08-18-a-free-model-vs-30-security-advisory-records-an-accuracy-test-you-can-rerun]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
