---
title: The normalization step that breaks before your ER model does
date: '2026-09-25'
source: https://dev.to/hannune/the-normalization-step-that-breaks-before-your-er-model-does-38ia
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
related:
- '[[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]'
- '[[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]'
- '[[2026-07-05-i-tested-every-chinese-ai-model-so-you-dont-have-to]]'
- '[[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]'
status: unread
---

> **TL;DR:** I spent three weeks tuning near-threshold match scores before realizing the pairs I was most worried about weren't getting bad scores. They weren't generating candidate pairs at all. The thing I thought would fix it didn…

## What’s new and why it matters
I spent three weeks tuning near-threshold match scores before realizing the pairs I was most worried about weren't getting bad scores. They weren't generating candidate pairs at all. The thing I thought would fix it didn't. My first guess was blocking key design. I'd read enough about the invisibility of blocking errors that I figured the issue had to be there. I checked the blocking key function, checked the bucket sizes, didn't see anything obviously wrong. The pairs I was looking for were just absent. Then I added a simple audit: take 30 pairs that should match, print the blocking keys side…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hannune/the-normalization-step-that-breaks-before-your-er-model-does-38ia

## Related notes
- [[2026-07-15-i-built-with-both-apis-as-a-bootcamp-grad-heres-what-actually-matters]]
- [[2026-04-22-i-kept-forgetting-to-delete-my-venvs-so-i-built-a-gui-for-it]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-09-24-should-you-pay-rs-50000-to-1-lakh-for-a-sql-course-when-free-is-available]]
- [[2026-07-05-i-tested-every-chinese-ai-model-so-you-dont-have-to]]
- [[2026-03-14-i-was-tired-of-parsing-xbrl-so-i-built-a-sec-edgar-api]]
