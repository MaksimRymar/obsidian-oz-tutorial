---
title: I ran 4 AI agents on yesterday's PRs. Two real security bugs surfaced.
date: '2026-06-09'
source: https://dev.to/arvavit/i-ran-4-ai-agents-on-yesterdays-prs-two-real-security-bugs-surfaced-43dl
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-03-26-what-is-mutation-testing-a-practical-guide-for-qa-engineers]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]'
status: unread
---

> **TL;DR:** After every coding session I run a 4-agent parallel audit on the diff I just shipped. A recent session of mine was seven PRs landing a new daily-challenge feature on my open-source LMS. Two of the audit findings were rea…

## What’s new and why it matters
After every coding session I run a 4-agent parallel audit on the diff I just shipped. A recent session of mine was seven PRs landing a new daily-challenge feature on my open-source LMS. Two of the audit findings were real security or integrity bugs that my human review missed. This is the playbook. The four agents I split the audit into four narrow roles. Narrow because a generalist agent tells you everything is fine; a specialist with a clear mandate tells you what is broken. Cleanup agent. Looks for leftover patterns from the work just done: dead references to removed roles, unused i18n keys…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/arvavit/i-ran-4-ai-agents-on-yesterdays-prs-two-real-security-bugs-surfaced-43dl

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-03-26-what-is-mutation-testing-a-practical-guide-for-qa-engineers]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-05-12-10-sql-changes-one-took-30-seconds-it-cut-query-time-by-85]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-04-16-duckdb-in-the-wild-what-6-minutes-of-benchmarking-across-4-machines-taught-me-about-real-world-performance]]
