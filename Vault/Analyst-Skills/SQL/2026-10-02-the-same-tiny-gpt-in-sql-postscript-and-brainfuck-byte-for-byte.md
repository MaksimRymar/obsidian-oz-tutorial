---
title: The same tiny GPT in SQL, PostScript and Brainfuck, byte for byte
date: '2026-10-02'
source: https://dev.to/nmicic/the-same-gpt-in-sql-postscript-and-brainfuck-byte-for-byte-59lc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
- '[[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]'
- '[[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]'
- '[[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]'
status: unread
---

> **TL;DR:** This post continues the int-llm hobby experiments from my earlier post . The earlier repositories are int-llm (Q16.48 fixed-point training and TinyLlama inference), int-llm-precision-ladder (reduced stored weight precisi…

## What’s new and why it matters
This post continues the int-llm hobby experiments from my earlier post . The earlier repositories are int-llm (Q16.48 fixed-point training and TinyLlama inference), int-llm-precision-ladder (reduced stored weight precision checked against the Q16.48 reference), int-llm-coordinate-permutation (reversible coordinate permutations of Llama checkpoints), and int-llm-viz (visualization of the integer GPT weights and inference path). Those projects produced a C program whose output is deterministic down to the last byte. This post describes three new repositories that reproduce that output in SQL, Po…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/nmicic/the-same-gpt-in-sql-postscript-and-brainfuck-byte-for-byte-59lc

## Related notes
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-07-22-when-to-trust-ai-generated-sql-and-when-not-to]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
- [[2026-08-30-give-your-agent-patch-a-determinism-budget-seed-locked-properties-pinned-fixtures-a-freeze-registry]]
- [[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]
- [[2026-08-21-null-in-sql-why-null-finds-nothing-and-what-to-write-instead]]
