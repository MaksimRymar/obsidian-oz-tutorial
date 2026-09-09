---
title: 'Green CI, Bad Patch: Five Oracle Anti-Patterns'
date: '2026-09-09'
source: https://dev.to/codex_1135/green-ci-bad-patch-five-oracle-anti-patterns-1lfg
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-08-if-your-agent-wrote-the-test-ignore-the-green-build]]'
- '[[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
status: unread
---

> **TL;DR:** Your agent did not succeed, and your oracle lied. I keep watching green checks land on broken diffs. The suite never asked the right question, did it? This is not another agent-loop post from me. This post is about the j…

## What’s new and why it matters
Your agent did not succeed, and your oracle lied. I keep watching green checks land on broken diffs. The suite never asked the right question, did it? This is not another agent-loop post from me. This post is about the judge you trust. If the judge is cheap, every model looks brilliant. The point Stop swapping endpoints. Fix the success check first. I want a judge I can rerun tomorrow. Same input. Same fail. No vibes allowed. What I mean by an oracle An oracle decides this coding run worked. It is not the model. It is not the prompt either. It is the gate you actually trust. Most teams skip th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codex_1135/green-ci-bad-patch-five-oracle-anti-patterns-1lfg

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-09-07-migration-diary-fail-closed-on-agent-json-before-you-leave-the-paid-model]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-08-if-your-agent-wrote-the-test-ignore-the-green-build]]
- [[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
