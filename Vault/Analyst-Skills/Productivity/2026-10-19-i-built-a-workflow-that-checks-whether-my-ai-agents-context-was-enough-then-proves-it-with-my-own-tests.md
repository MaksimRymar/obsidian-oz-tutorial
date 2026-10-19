---
title: I built a workflow that checks whether my AI agent's context was enough, then
  proves it with my own tests
date: '2026-10-19'
source: https://dev.to/littlestjames82sys/i-built-a-workflow-that-checks-whether-my-ai-agents-context-was-enough-then-proves-it-with-my-own-4214
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-09-02-your-agent-request-touches-12-containers-only-one-of-them-runs-a-model]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-05-30-simple-sql-tool]]'
- '[[2026-10-11-my-backtest-re-runs-when-i-save-the-strategy-file-and-shows-which-trades-changed]]'
- '[[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]'
status: unread
---

> **TL;DR:** When I give an AI coding agent a task, I never actually know if the context I sent it was enough. So I built the check. The stack is four small tools, all Python standard library, all MIT, all local: GhostSlice cuts a pr…

## What’s new and why it matters
When I give an AI coding agent a task, I never actually know if the context I sent it was enough. So I built the check. The stack is four small tools, all Python standard library, all MIT, all local: GhostSlice cuts a project down to a task bundle and reports the token cut. On my own bench repo: 74,692 tokens full, 29,926 sliced. GhostVerify checks the bundle against the task before an agent runs, and says gaps_found when something reachable is missing. GhostBench runs the same task full vs sliced and, when you give it a test command, executes your tests in a contained runner (scrubbed environ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/littlestjames82sys/i-built-a-workflow-that-checks-whether-my-ai-agents-context-was-enough-then-proves-it-with-my-own-4214

## Related notes
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-09-02-your-agent-request-touches-12-containers-only-one-of-them-runs-a-model]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-05-30-simple-sql-tool]]
- [[2026-10-11-my-backtest-re-runs-when-i-save-the-strategy-file-and-shows-which-trades-changed]]
- [[2026-10-15-see-every-google-ad-a-competitor-runs-from-just-their-domain-curl-python-n8n]]
