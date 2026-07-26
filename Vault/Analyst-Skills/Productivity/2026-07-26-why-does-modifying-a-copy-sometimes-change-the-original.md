---
title: Why Does Modifying a Copy Sometimes Change the Original?
date: '2026-07-26'
source: https://dev.to/storvus/why-does-modifying-a-copy-sometimes-change-the-original-181p
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-07-03-why-does-a-list-change-in-two-variables]]'
- '[[2026-04-22-mastering-python-lists-through-real-world-use-a-practical-developers-guide]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]'
- '[[2026-03-07-quarks-outlines-python-emulating-callable-objects]]'
- '[[2026-06-15-cross-row-validation-risk-in-postgresql-check-constraints]]'
status: unread
---

> **TL;DR:** We assume you already know how to write simple Python programs and understand basic syntax (if, for, functions, lists). Here, we're not discussing how to use the language, but why it works the way it does. Try to guess w…

## What’s new and why it matters
We assume you already know how to write simple Python programs and understand basic syntax (if, for, functions, lists). Here, we're not discussing how to use the language, but why it works the way it does. Try to guess what this code prints. numbers = [[ 1 , 2 ], [ 3 , 4 ]] copy = numbers . copy () copy [ 0 ]. append ( 99 ) print ( numbers ) If you take the word copy literally, the answer seems obvious. We modified the copy. So the original should stay unchanged. Many people expect: [[ 1 , 2 ], [ 3 , 4 ]] But Python prints: [[ 1 , 2 , 99 ], [ 3 , 4 ]] That seems rather strange. We modified the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/storvus/why-does-modifying-a-copy-sometimes-change-the-original-181p

## Related notes
- [[2026-07-03-why-does-a-list-change-in-two-variables]]
- [[2026-04-22-mastering-python-lists-through-real-world-use-a-practical-developers-guide]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-06-13-select-final-and-optimize-final-are-not-the-same-thing]]
- [[2026-03-07-quarks-outlines-python-emulating-callable-objects]]
- [[2026-06-15-cross-row-validation-risk-in-postgresql-check-constraints]]
