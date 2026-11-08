---
title: '48-Hour Field Notes: Same Prompt, Two JSON Shapes, and a Validator That Passed
  Both'
date: '2026-11-08'
source: https://dev.to/codepy_1473/48-hour-field-notes-same-prompt-two-json-shapes-and-a-validator-that-passed-both-a21
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]'
- '[[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]'
status: unread
---

> **TL;DR:** Six hundred markdown files landed in an inbox folder, and my only job was to turn them into a one-page morning report. The plan looked trivial: send each file to a model, get back four fields, append a line of JSONL, ren…

## What’s new and why it matters
Six hundred markdown files landed in an inbox folder, and my only job was to turn them into a one-page morning report. The plan looked trivial: send each file to a model, get back four fields, append a line of JSONL, render a table. I gave myself forty-eight hours to make that loop boring, so like an idiot I built the happy path first. The happy path held for about six hours. The full run exited 0, the report rendered, and nobody on the receiving end noticed that one column had quietly stopped meaning anything. These are the field notes: what I tried, where it broke, and the small harness I wo…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/codepy_1473/48-hour-field-notes-same-prompt-two-json-shapes-and-a-validator-that-passed-both-a21

## Related notes
- [[2026-10-15-free-draft-volume-or-paid-first-passes-a-debate-for-agent-sql-budgets]]
- [[2026-10-26-48-hour-field-notes-my-free-box-looked-slow-until-i-logged-the-gap-between-requests]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-07-21-my-gitignore-had-a-blanket-rule-one-file-broke-it-and-no-pattern-would-have-caught-that]]
