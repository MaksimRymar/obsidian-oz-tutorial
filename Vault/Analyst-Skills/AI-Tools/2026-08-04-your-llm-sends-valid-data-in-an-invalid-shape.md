---
title: Your LLM sends valid data in an invalid shape
date: '2026-08-04'
source: https://dev.to/favur/your-llm-sends-valid-data-in-an-invalid-shape-2p9n
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-05-26-from-screen-recording-to-test-cases-in-seconds-meet-clipcase]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-06-10-your-schema-validation-passes-and-the-agent-still-picks-the-wrong-tool-the-bug-is-semantic]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
status: unread
---

> **TL;DR:** A model never hands your tool a typed object. It hands you text that claims to describe one, and everything between that text and your validated arguments is a parse you control. How forgiving that parse should be is the…

## What’s new and why it matters
A model never hands your tool a typed object. It hands you text that claims to describe one, and everything between that text and your validated arguments is a parse you control. How forgiving that parse should be is the whole design question at the boundary, and the answer is not the same in both directions. Arrays that arrive as strings containing arrays Values that are not JSON and parse perfectly anyway Arguments that are still streaming when validation wants them whole The quiet fallback that turns a clean rejection into a confusing error Our harness is the worked example throughout, and…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/favur/your-llm-sends-valid-data-in-an-invalid-shape-2p9n

## Related notes
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-05-26-from-screen-recording-to-test-cases-in-seconds-meet-clipcase]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-06-10-your-schema-validation-passes-and-the-agent-still-picks-the-wrong-tool-the-bug-is-semantic]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
