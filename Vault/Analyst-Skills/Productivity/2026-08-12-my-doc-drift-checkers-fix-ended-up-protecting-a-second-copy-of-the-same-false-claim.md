---
title: My Doc-Drift Checker's Fix Ended Up Protecting a Second Copy of the Same False
  Claim
date: '2026-08-12'
source: https://dev.to/enjoy_kumawat/my-doc-drift-checkers-fix-ended-up-protecting-a-second-copy-of-the-same-false-claim-2e85
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]'
- '[[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-08-10-my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet]]'
- '[[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]'
status: unread
---

> **TL;DR:** A week ago I wrote about a script in this repo, update_profile.py , that documentation claimed was a real, working part of the codebase. It never was — git log --all --diff-filter=A -- update_profile.py comes back comple…

## What’s new and why it matters
A week ago I wrote about a script in this repo, update_profile.py , that documentation claimed was a real, working part of the codebase. It never was — git log --all --diff-filter=A -- update_profile.py comes back completely empty across the repo's full history. I fixed the doc that said otherwise, added a checker ( scripts/check_key_facts.py ) so it couldn't drift back, wrote it up, and moved on. Today I went back to recheck my own work before writing something new, and found the same false claim, word for identical word in spirit, still sitting uncorrected one section below the fix. The chec…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/enjoy_kumawat/my-doc-drift-checkers-fix-ended-up-protecting-a-second-copy-of-the-same-false-claim-2e85

## Related notes
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-07-my-mcp-tools-docstring-promised-limit-1-100-passing--1-returned-almost-everything-not-nothing]]
- [[2026-08-09-my-comment-reply-pipeline-was-feeding-me-garbled-html-entities-instead-of-the-actual-comment]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-08-10-my-fix-commit-cited-a-bugsmd-entry-that-didnt-exist-yet]]
- [[2026-08-08-my-mcp-tool-fetches-before-it-writes-and-logs-every-change-it-never-checked-whether-there-was-anything-to-change]]
