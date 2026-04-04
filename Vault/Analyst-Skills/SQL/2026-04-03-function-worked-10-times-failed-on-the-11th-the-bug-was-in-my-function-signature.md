---
title: Function worked 10 times. Failed on the 11th. The bug was in my function signature.
date: '2026-04-03'
source: https://dev.to/nicodev__/function-worked-10-times-failed-on-the-11th-the-bug-was-in-my-function-signature-2o4l
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-25-what-is-tool-chaining-in-llms-why-it-breaks-and-how-to-think-about-orchestration]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-02-24-i-built-a-free-model-drift-detection-api-no-signup-required]]'
- '[[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-03-13-using-marshmallow-method-fields-for-complex-nested-schemas-in-flask]]'
status: unread
---

> **TL;DR:** Function worked 10 times. Failed on the 11th. The bug was in my function signature. I had a Python function processing user submissions. Worked perfectly for the first 10 calls during testing. Called it the 11th time and…

## What’s new and why it matters
Function worked 10 times. Failed on the 11th. The bug was in my function signature. I had a Python function processing user submissions. Worked perfectly for the first 10 calls during testing. Called it the 11th time and suddenly got duplicate data where there shouldn't be any. No error message. Just wrong output. Simple data processor Takes a list of items, filters them, returns results: def process_items ( items , results = []): for item in items : if item [ ' status ' ] == ' active ' : results . append ( item ) return results # Usage batch1 = process_items ([{ ' id ' : 1 , ' status ' : ' ac…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nicodev__/function-worked-10-times-failed-on-the-11th-the-bug-was-in-my-function-signature-2o4l

## Related notes
- [[2026-03-25-what-is-tool-chaining-in-llms-why-it-breaks-and-how-to-think-about-orchestration]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-02-24-i-built-a-free-model-drift-detection-api-no-signup-required]]
- [[2026-03-26-finding-the-missing-indexes-your-queries-are-begging-for]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-03-13-using-marshmallow-method-fields-for-complex-nested-schemas-in-flask]]
