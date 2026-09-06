---
title: The Agent Invented a status_reason. The Spec Had Never Listed It.
date: '2026-09-06'
source: https://dev.to/codepy_1473/the-agent-invented-a-statusreason-the-spec-had-never-listed-it-2nbh
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#tool'
related:
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
- '[[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
status: unread
---

> **TL;DR:** Have you ever watched a generated HTTP client look finished, then fail the first real fixture you threw at it? I spent forty-eight hours in that loop last week, and the failure mode stayed almost polite. Every request re…

## What’s new and why it matters
Have you ever watched a generated HTTP client look finished, then fail the first real fixture you threw at it? I spent forty-eight hours in that loop last week, and the failure mode stayed almost polite. Every request returned 200, every dataclass carried a type hint, and every mock-based test stayed green. The only bug was a field the upstream API had never promised, and I kept blaming the transport. This is a field notebook, not a product tour. I am writing down what I tried, what broke, and what I would actually repeat. The reduced example below is a local reproduction I kept, not a product…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codepy_1473/the-agent-invented-a-statusreason-the-spec-had-never-listed-it-2nbh

## Related notes
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-08-19-my-batch-job-had-a-100-success-rate-and-a-4-corruption-rate]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
- [[2026-08-06-building-an-mcp-tool-call-test-rig-with-the-python-sdk-in-2026]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
