---
title: Test the next effect, not just the first tool call
date: '2026-09-14'
source: https://dev.to/neerazz/test-the-next-effect-not-just-the-first-tool-call-2g36
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-pin-agent-tools-to-a-checked-in-schema-before-the-first-call]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-08-if-your-agent-wrote-the-test-ignore-the-green-build]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
status: unread
---

> **TL;DR:** A tool labeled “read documentation” can trigger work after the first request. How do you keep that first approval from becoming permission for everything that follows? Start with a tiny local example. It will not launch…

## What’s new and why it matters
A tool labeled “read documentation” can trigger work after the first request. How do you keep that first approval from becoming permission for everything that follows? Start with a tiny local example. It will not launch a documentation builder or reach the internet. It models two separate requests: a permitted documentation destination and an outbound destination that is not permitted. The second request gets its own decision. This is a Boundary Receipt: a teaching record that answers what a task can change, who authorized that effect, and what evidence shows the decision was followed. It is n…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/neerazz/test-the-next-effect-not-just-the-first-tool-call-2g36

## Related notes
- [[2026-09-09-pin-agent-tools-to-a-checked-in-schema-before-the-first-call]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-08-if-your-agent-wrote-the-test-ignore-the-green-build]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
