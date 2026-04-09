---
title: The model looked great on validation until one real invoice broke four assumptions
date: '2026-04-09'
source: https://dev.to/angu10/the-model-looked-great-on-validation-until-one-real-invoice-broke-four-assumptions-5g2l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]'
- '[[2026-03-25-stop-googling-dax-formulas-here-are-the-5-i-actually-use-to-solve-business-problems]]'
status: unread
---

> **TL;DR:** An empirical note on what synthetic invoice data taught a Gemma fine-tune, what it hid, and how one real document exposed the gap. I fine-tuned a small Gemma model to parse Indian invoices because I wanted a path that wa…

## What’s new and why it matters
An empirical note on what synthetic invoice data taught a Gemma fine-tune, what it hid, and how one real document exposed the gap. I fine-tuned a small Gemma model to parse Indian invoices because I wanted a path that was cheaper, more private, and easier to deploy than calling a hosted API for every document. The training metrics looked excellent. Then I ran the model on one real invoice. It got the total right, the supplier right, the address right, and still failed in four ways that would make the output unusable in a real finance workflow. That invoice was more useful than another few hund…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/angu10/the-model-looked-great-on-validation-until-one-real-invoice-broke-four-assumptions-5g2l

## Related notes
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-03-11-i-thought-my-rails-query-was-fine-until-null-ate-my-data]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]
- [[2026-03-25-stop-googling-dax-formulas-here-are-the-5-i-actually-use-to-solve-business-problems]]
