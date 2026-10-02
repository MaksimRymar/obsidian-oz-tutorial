---
title: The same question, asked three ways
date: '2026-10-02'
source: https://dev.to/skucherenko/the-same-question-asked-three-ways-1c8c
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]'
- '[[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]'
status: unread
---

> **TL;DR:** A RAG system answers a question in two steps. A retriever turns the question into a vector, compares it with the vectors of every passage in the documents, and hands the five closest passages to a language model. The mod…

## What’s new and why it matters
A RAG system answers a question in two steps. A retriever turns the question into a vector, compares it with the vectors of every passage in the documents, and hands the five closest passages to a language model. The model writes the answer from those five. If the passage that holds the answer is not among the five, the model cannot answer, however good it is. In the previous piece I measured that second condition directly and found a question whose answer sat at rank 7. The model only ever saw ranks 1 to 5, so it refused. A reader, Mikhail, had found that question by hand and then found that…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/skucherenko/the-same-question-asked-three-ways-1c8c

## Related notes
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-09-30-a-stored-procedure-can-compile-and-still-change-its-meaning]]
- [[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-07-your-text-to-sql-agent-picks-tables-before-security-runs-heres-the-fix]]
