---
title: 'FAQ: Five Myths About Tests the Agent Wrote for Itself'
date: '2026-09-19'
source: https://dev.to/gitlab_3188/faq-five-myths-about-tests-the-agent-wrote-for-itself-5h8o
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#tool'
related:
- '[[2026-09-16-faq-five-myths-about-the-model-already-saw-the-repo]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-17-characterize-the-report-boundary-before-one-safe-change]]'
- '[[2026-09-16-start-from-a-red-test-keep-the-model-off-your-shell]]'
- '[[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]'
- '[[2026-09-08-if-your-agent-wrote-the-test-ignore-the-green-build]]'
status: unread
---

> **TL;DR:** Who actually graded the agent's homework on that run? I keep seeing the same claim in review threads. The agent wrote tests, they passed, so we ship. That claim is circular because the grader sat nearby. The same session…

## What’s new and why it matters
Who actually graded the agent's homework on that run? I keep seeing the same claim in review threads. The agent wrote tests, they passed, so we ship. That claim is circular because the grader sat nearby. The same session wrote the answers and the key. Why this FAQ exists Green test output is not independent evidence of correctness. The same loop wrote the code and the checks. Ask a harder question before you merge. Did the tests constrain the implementation at all? Or did they photograph whatever the model just invented? I use this FAQ when the test tree appears in one burst. New files in src/…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/gitlab_3188/faq-five-myths-about-tests-the-agent-wrote-for-itself-5h8o

## Related notes
- [[2026-09-16-faq-five-myths-about-the-model-already-saw-the-repo]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-17-characterize-the-report-boundary-before-one-safe-change]]
- [[2026-09-16-start-from-a-red-test-keep-the-model-off-your-shell]]
- [[2026-09-12-unclassified-tests-cannot-green-an-agent-patch]]
- [[2026-09-08-if-your-agent-wrote-the-test-ignore-the-green-build]]
