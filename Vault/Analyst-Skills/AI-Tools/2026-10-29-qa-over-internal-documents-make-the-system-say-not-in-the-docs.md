---
title: 'Q&A over internal documents: make the system say "not in the docs"'
date: '2026-10-29'
source: https://dev.to/slava_kotenev_159/qa-over-internal-documents-make-the-system-say-not-in-the-docs-22oh
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#support-analytics'
- '#tool'
related:
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]'
- '[[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-28-what-has-to-be-true-before-you-trust-an-ai-data-agent]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
status: unread
---

> **TL;DR:** An assistant that answers questions about your documents will be wrong sometimes. What destroys trust is not the wrong answer, it is the confident wrong answer to a question the documents never covered. So the first desi…

## What’s new and why it matters
An assistant that answers questions about your documents will be wrong sometimes. What destroys trust is not the wrong answer, it is the confident wrong answer to a question the documents never covered. So the first design question is not "how good is retrieval?" but "when does the system refuse?" Here is a small demo that treats refusal as a first-class result. The data is public and the numbers are test numbers, not a client result. What the demo does One function, KB.answer(question) , returns three things: the best passage as the citation, a confidence that it really holds the answer, and…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/slava_kotenev_159/qa-over-internal-documents-make-the-system-say-not-in-the-docs-22oh

## Related notes
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-06-12-build-a-rag-chatbot-from-scratch-in-about-40-lines-of-python]]
- [[2026-09-23-38-of-an-analysts-questions-get-no-records-found-when-the-data-is-right-there]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-28-what-has-to-be-true-before-you-trust-an-ai-data-agent]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
