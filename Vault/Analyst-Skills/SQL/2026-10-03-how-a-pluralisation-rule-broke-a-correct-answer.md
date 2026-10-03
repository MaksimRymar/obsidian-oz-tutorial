---
title: How a Pluralisation Rule Broke a Correct Answer
date: '2026-10-03'
source: https://dev.to/megapixel99/how-a-pluralisation-rule-broke-a-correct-answer-2c0p
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-09-27-how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows]]'
- '[[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]'
- '[[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]'
- '[[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]'
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
status: unread
---

> **TL;DR:** appgen is a tool of mine that turns a sentence into a running application with no language model in the generating path. Give it "a support desk system with priorities and comments" and it writes a dependency-free Python…

## What’s new and why it matters
appgen is a tool of mine that turns a sentence into a running application with no language model in the generating path. Give it "a support desk system with priorities and comments" and it writes a dependency-free Python file, starts it, and drives every feature you asked for over real HTTP before showing it to you. One of the things it has to decide is the entity : the noun the generated app calls a row, which becomes a table name, a form field and a URL path. The checker that judges a finished artifact has two halves. The first starts the program and proves it stores and returns a record. Th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/megapixel99/how-a-pluralisation-rule-broke-a-correct-answer-2c0p

## Related notes
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-09-27-how-to-catch-a-missing-index-in-a-test-when-your-test-table-has-20-rows]]
- [[2026-09-05-enforcing-data-invariants-in-odoo-model-constraints-migrations-and-tests-that-actually-cover-the-fix]]
- [[2026-08-11-code-interpreter-is-infrastructure-not-a-prompt]]
- [[2026-08-20-a-benchmark-is-only-as-good-as-the-model-you-use-to-grade-it]]
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
