---
title: I Built a Bot That Reproduces GitHub Bugs Automatically — Here's What Broke
  (and What I Learned)
date: '2026-08-28'
source: https://dev.to/qxmcu/i-built-a-bot-that-reproduces-github-bugs-automatically-heres-what-broke-and-what-i-learned-3b12
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#tableau'
- '#tool'
related:
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-06-17-struggling-with-boyce-codd-normal-form-as-a-junior-developer]]'
- '[[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]'
- '[[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]'
status: unread
---

> **TL;DR:** The problem As a maintainer, even a solo one on a small project, the most time-consuming part of fixing a bug usually isn't writing the fix. It's reproducing it. Someone files an issue, the description is vague, and you…

## What’s new and why it matters
The problem As a maintainer, even a solo one on a small project, the most time-consuming part of fixing a bug usually isn't writing the fix. It's reproducing it. Someone files an issue, the description is vague, and you spend twenty minutes just trying to get your machine into the same broken state theirs is in before you can even start debugging. I wanted that step gone. What I built Ghost Hunter is an open-source CLI + webhook bot that automates bug reproduction on GitHub. Comment bot/reproduce on any issue, and it: Parses the issue text with an LLM to extract environment details and repro s…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/qxmcu/i-built-a-bot-that-reproduces-github-bugs-automatically-heres-what-broke-and-what-i-learned-3b12

## Related notes
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-06-17-struggling-with-boyce-codd-normal-form-as-a-junior-developer]]
- [[2026-05-31-i-didnt-have-a-pc-for-my-database-class-so-i-built-my-own-t-sql-sandbox-in-the-browser]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-06-19-i-built-an-open-source-ai-that-security-reviews-every-pull-request-and-maps-each-bug-to-pci-dss-soc-2-gdpr]]
- [[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]
