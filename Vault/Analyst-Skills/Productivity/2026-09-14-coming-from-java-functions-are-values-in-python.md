---
title: 'Coming from Java: functions are values in Python'
date: '2026-09-14'
source: https://dev.to/ljgeorgiou/coming-from-java-functions-are-values-in-python-31i
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-03-07-quarks-outlines-python-emulating-callable-objects]]'
- '[[2026-09-08-write-code-once-use-it-forever-python-functions-explained]]'
- '[[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
status: unread
---

> **TL;DR:** I have recently started to learn python, and coming from Java there are a few interesting things I have found about functions. The first thing that stuck out to me is that in Python, functions are values. What I mean by…

## What’s new and why it matters
I have recently started to learn python, and coming from Java there are a few interesting things I have found about functions. The first thing that stuck out to me is that in Python, functions are values. What I mean by that, is a function is a thing that you can store, just like you can store a number or a string. For example, let's look at this simple function below which squares a number: def square ( item : int ) -> int : return item * item This simple function can be assigned to a new variable (an alias): square_2 = square Therefore, if we wanted to square a number we could either use squ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ljgeorgiou/coming-from-java-functions-are-values-in-python-31i

## Related notes
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-03-07-quarks-outlines-python-emulating-callable-objects]]
- [[2026-09-08-write-code-once-use-it-forever-python-functions-explained]]
- [[2026-08-31-i-left-an-ai-agent-running-unattended-for-a-day-here-is-everything-that-broke]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
