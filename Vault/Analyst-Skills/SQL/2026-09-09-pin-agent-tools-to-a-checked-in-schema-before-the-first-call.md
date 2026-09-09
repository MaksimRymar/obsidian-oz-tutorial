---
title: Pin Agent Tools to a Checked-In Schema Before the First Call
date: '2026-09-09'
source: https://dev.to/aiio_8140/pin-agent-tools-to-a-checked-in-schema-before-the-first-call-2pl0
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
- '[[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]'
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
status: unread
---

> **TL;DR:** If the model can name a tool that is not in your repo, you do not have an agent. You have a confused intern with root. Pin the tool list, hash it, and drop every call that does not match. That is the whole article. The r…

## What’s new and why it matters
If the model can name a tool that is not in your repo, you do not have an agent. You have a confused intern with root. Pin the tool list, hash it, and drop every call that does not match. That is the whole article. The rest is a from-zero walkthrough you can run on a laptop. Want a remote box later? Fine. The proxy still lives next to your code. Why start here? Because every flashy agent demo hides the same leak. The model invents a tool, a path, a “helpful” side effect. Your loop shrugs and calls it. I do not shrug. Do you? What you will build A tiny three-file loop: tools.schema.json — the o…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/aiio_8140/pin-agent-tools-to-a-checked-in-schema-before-the-first-call-2pl0

## Related notes
- [[2026-09-08-give-the-model-one-json-job-run-everything-else-yourself]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
- [[2026-08-04-you-cant-unit-test-an-llm-heres-what-i-built-instead]]
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
