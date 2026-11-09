---
title: green tests don't cover the branch that leaks
date: '2026-11-09'
source: https://dev.to/parsam/green-tests-dont-cover-the-branch-that-leaks-5fga
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-06-20-green-unit-tests-are-a-comfort-blanket]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]'
- '[[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]'
- '[[2026-09-21-an-agent-claim-is-open-until-a-child-span-closes-it]]'
- '[[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]'
status: unread
---

> **TL;DR:** agent-written tests mostly test the path the agent wrote, which is the success path. so the bugs that survive are the ones that only run when something fails. the cleanest example going around IBM ContextForge, issue #18…

## What’s new and why it matters
agent-written tests mostly test the path the agent wrote, which is the success path. so the bugs that survive are the ones that only run when something fails. the cleanest example going around IBM ContextForge, issue #1885 . the session cleanup looked like this finally : db . commit () # can raise db . close () # never reached if it does finally guarantees the block starts, not that every line in it finishes. if commit() throws, python leaves the block right there and close() never runs. every test was green. under a 3,000 user load test, postgres showed this state | count --------------------…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/parsam/green-tests-dont-cover-the-branch-that-leaks-5fga

## Related notes
- [[2026-06-20-green-unit-tests-are-a-comfort-blanket]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-10-22-i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli]]
- [[2026-07-18-one-compaction-four-actions-one-block-compaction-safety-is-a-property-of-the-pair]]
- [[2026-09-21-an-agent-claim-is-open-until-a-child-span-closes-it]]
- [[2026-10-02-how-i-turn-ai-images-into-print-ready-vector-stickers-no-illustrator-no-gpu]]
