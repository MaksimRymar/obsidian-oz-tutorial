---
title: My Doc-Drift Checker Has Two Different Ideas of "Documented," and Only Uses
  the Wrong One
date: '2026-08-13'
source: https://dev.to/enjoy_kumawat/my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one-1ao7
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-12-my-comment-reply-pipeline-picks-one-winner-per-thread-two-commenters-broke-that]]'
- '[[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]'
- '[[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]'
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]'
status: unread
---

> **TL;DR:** This repo has a script, scripts/check_key_facts.py , whose whole job is catching the thing every project accumulates and nobody notices: a real file on disk that the project's own reference doc never mentions. It runs, i…

## What’s new and why it matters
This repo has a script, scripts/check_key_facts.py , whose whole job is catching the thing every project accumulates and nobody notices: a real file on disk that the project's own reference doc never mentions. It runs, it lists what's missing from key_facts.md 's Project Files table, and I've trusted its clean output more than once as a reason not to go re-read the table by hand. I went back into it today for an unrelated reason and noticed it actually defines two functions for "is this file documented," and they don't agree with each other. def documented_files (): text = KEY_FACTS . read_tex…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one-1ao7

## Related notes
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-12-my-comment-reply-pipeline-picks-one-winner-per-thread-two-commenters-broke-that]]
- [[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]
- [[2026-08-09-my-mcp-servers-two-credential-checks-were-flagged-missing-five-days-ago-nobody-fixed-them]]
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-07-19-my-comment-reply-bot-hit-a-wall-the-docs-never-mentioned-that-wall-turned-out-to-be-a-security-feature]]
