---
title: Should you guess on the Bocconi admission test? A short Python simulation
date: '2026-10-12'
source: https://dev.to/intellixtutoring/should-you-guess-on-the-bocconi-admission-test-a-short-python-simulation-331d
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]'
- '[[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]'
- '[[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
status: unread
---

> **TL;DR:** Students preparing for the Bocconi admission test ask me the same question every year: if I don't know the answer, should I leave it blank? The scoring rule makes guessing look risky. A correct answer is +1, a blank is 0…

## What’s new and why it matters
Students preparing for the Bocconi admission test ask me the same question every year: if I don't know the answer, should I leave it blank? The scoring rule makes guessing look risky. A correct answer is +1, a blank is 0 and a wrong answer is −0.2. The test has 50 questions in 75 minutes, and if your total after penalties is below 17, your application is not considered at all. You can settle the question with a few lines of maths, then check it with a simulation. One guess A blind guess on a question with n options is right with probability 1/n and wrong otherwise, so its expected value is E =…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/intellixtutoring/should-you-guess-on-the-bocconi-admission-test-a-short-python-simulation-331d

## Related notes
- [[2026-08-11-sql-aliases-how-to-read-a-query-out-loud]]
- [[2026-09-09-when-one-query-isnt-enough-a-love-letter-to-ctes-and-subqueries-in-postgresql]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-10-09-x-x---1-and-three-other-bit-tricks-and-the-one-that-lies-about-negative-numbers]]
- [[2026-09-25-5-sql-patterns-that-run-fine-and-still-return-the-wrong-answer]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
