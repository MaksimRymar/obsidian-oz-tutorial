---
title: I Faked My Own Drug Valuation. 17 Lines of Python Caught Me.
date: '2026-11-24'
source: https://dev.to/dr_delta234/i-faked-my-own-drug-valuation-17-lines-of-python-caught-me-3kph
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-12-how-to-build-a-telegram-ai-bot-that-summarizes-links-for-free-full-code]]'
- '[[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]'
- '[[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]'
- '[[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]'
- '[[2026-11-09-pydantic-catch-bad-data-before-it-reaches-your-database]]'
- '[[2026-10-04-i-let-an-ai-audit-my-password-vault-it-lied-to-me-with-total-confidence]]'
status: unread
---

> **TL;DR:** I build a drug valuation app called Somota. This week I tried to cheat on my own numbers, on camera, to see whether the app would catch me. Video: https://youtu.be/_qJZJFU8xTo The setup In a drug licensing deal, a valuat…

## What’s new and why it matters
I build a drug valuation app called Somota. This week I tried to cheat on my own numbers, on camera, to see whether the app would catch me. Video: https://youtu.be/_qJZJFU8xTo The setup In a drug licensing deal, a valuation is usually a big spreadsheet that gets emailed between two companies, bankers and lawyers. Months later somebody asks which version everybody agreed on, and nobody can prove it. So every valuation in Somota is now signed as a receipt: Take every input (odds of success, costs, sales, discount rate) and serialize it as canonical JSON: sorted keys, no spaces. Hash it with SHA-…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dr_delta234/i-faked-my-own-drug-valuation-17-lines-of-python-caught-me-3kph

## Related notes
- [[2026-08-12-how-to-build-a-telegram-ai-bot-that-summarizes-links-for-free-full-code]]
- [[2026-09-23-one-real-scan-counts-a-hundred-ranking-a-curation-queue-by-your-own-users]]
- [[2026-06-15-my-sigma-scanner-cant-count-so-i-wrote-that-down-instead-of-faking-it]]
- [[2026-10-26-how-to-check-your-ais-data-answers-evals-for-each-stage]]
- [[2026-11-09-pydantic-catch-bad-data-before-it-reaches-your-database]]
- [[2026-10-04-i-let-an-ai-audit-my-password-vault-it-lied-to-me-with-total-confidence]]
