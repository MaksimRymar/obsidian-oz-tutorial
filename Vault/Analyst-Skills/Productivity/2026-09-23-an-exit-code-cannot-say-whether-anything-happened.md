---
title: An Exit Code Cannot Say Whether Anything Happened
date: '2026-09-23'
source: https://dev.to/megapixel99/an-exit-code-cannot-say-whether-anything-happened-4nbk
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-16-48-hour-field-notes-all-green-nothing-ran]]'
status: unread
---

> **TL;DR:** Code: Megapixel99/didrun Exit code 0 means "I did not fail". A suite of ten thousand assertions and a suite that collected nothing both report it; no amount of reading the number harder will separate them. That is how a…

## What’s new and why it matters
Code: Megapixel99/didrun Exit code 0 means "I did not fail". A suite of ten thousand assertions and a suite that collected nothing both report it; no amount of reading the number harder will separate them. That is how a check silently stops checking and nobody finds out for a year. The glob stops matching, the marker deselects everything, the step keeps exiting 0, and green is what everyone was looking for. The measured example, from didrun 's README rather than from folklore: go test ./... on a tree with no test files prints [no test files] and exits 0. Wrapped as didrun --expect "^ok " -- go…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/megapixel99/an-exit-code-cannot-say-whether-anything-happened-4nbk

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-16-48-hour-field-notes-all-green-nothing-ran]]
