---
title: Run prompt-injection tests in CI with pytest and GitHub Actions
date: '2026-11-16'
source: https://dev.to/litmustools/run-prompt-injection-tests-in-ci-with-pytest-and-github-actions-25a7
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#tool'
related:
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]'
- '[[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]'
- '[[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]'
- '[[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]'
- '[[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]'
status: unread
---

> **TL;DR:** Disclosure: I make Litmus, a small CLI for LLM evals, and sell a pack of attack prompts. This post needs neither. The setup below is plain pytest, and I ran the test code against a stub model to check it. A prompt-inject…

## What’s new and why it matters
Disclosure: I make Litmus, a small CLI for LLM evals, and sell a pack of attack prompts. This post needs neither. The setup below is plain pytest, and I ran the test code against a stub model to check it. A prompt-injection check that only runs when someone remembers to run it will not catch the regression that matters. The fix is boring: put the attack prompts in a file, run them as tests, and fail the build when one works. The idea Every attack asks the model to print a made-up marker string (a canary). A safe model never prints it, so a test is one assertion: the canary must not appear in t…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/litmustools/run-prompt-injection-tests-in-ci-with-pytest-and-github-actions-25a7

## Related notes
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-08-21-how-to-find-duplicate-rows-in-sql-and-decide-what-counts-as-one]]
- [[2026-09-25-polymorphic-associations-in-postgresql-one-commentableid-column-or-a-foreign-key-per-table]]
- [[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]
- [[2026-11-01-getting-only-the-new-dois-from-the-crossref-api-every-day-dates-cursors-and-rate-limits]]
- [[2026-09-01-seeding-fixtures-realistic-test-data-for-warehouse-integration-tests]]
