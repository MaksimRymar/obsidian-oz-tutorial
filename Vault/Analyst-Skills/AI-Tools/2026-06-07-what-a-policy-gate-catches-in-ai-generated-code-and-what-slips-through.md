---
title: What a policy gate catches in AI-generated code, and what slips through
date: '2026-06-07'
source: https://dev.to/vorsken/what-a-policy-gate-catches-in-ai-generated-code-and-what-slips-through-4n97
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-04-29-postgresql-subquery-and-cte-optimization]]'
- '[[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]'
- '[[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]'
- '[[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]'
status: unread
---

> **TL;DR:** I maintain an open-source GitHub Action called vorsken. It does one thing: scan the diff on a pull request with Semgrep, apply a fixed policy, and return BLOCK, FLAG, or PASS. No dashboard, no model that drifts over time…

## What’s new and why it matters
I maintain an open-source GitHub Action called vorsken. It does one thing: scan the diff on a pull request with Semgrep, apply a fixed policy, and return BLOCK, FLAG, or PASS. No dashboard, no model that drifts over time. Rules at ERROR/HIGH/CRITICAL severity block the merge, WARNING/MEDIUM flag it, the rest pass. Same diff, same verdict. The usual pitch for a tool like this is that it catches the SQL injection your AI assistant wrote. I wanted to see what it actually catches against real assistant output, so I generated 28 functions and ran them through. The test Seven backend tasks: a FastAP…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/vorsken/what-a-policy-gate-catches-in-ai-generated-code-and-what-slips-through-4n97

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-04-29-postgresql-subquery-and-cte-optimization]]
- [[2026-02-23-flask-vs-nodejs-choosing-the-right-backend-framework-for-2026]]
- [[2026-06-04-i-built-a-cache-engine-from-scratch-in-python-and-o1-lfu-eviction-is-sneakier-than-lru]]
- [[2026-04-04-i-tried-to-analyze-sql-lineage-across-15-databases-everything-broke-until-i-did-this]]
