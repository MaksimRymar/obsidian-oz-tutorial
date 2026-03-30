---
title: Recursion
date: '2026-03-30'
source: https://dev.to/keerthigap/recursion-2d67
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-02-26-beginner-friendly-guide---leetcode-problem-1404-c-python-javascript]]'
- '[[2026-02-23-beginner-friendly-guide-check-if-a-string-contains-all-binary-codes-of-size-k---problem-1461-c-python-javascript]]'
- '[[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]'
- '[[2026-02-27-beginner-friendly-guide-minimum-operations-to-equalize-binary-string---problem-3666-c-python-javascript]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-02-28-deep-dive-into-the-langbot-plugin-system-process-isolation-event-driven-hooks-component-architecture]]'
status: unread
---

> **TL;DR:** What is Recursion? Recursion means a function calls itself to solve a problem. Every recursive function has two main parts: Base Case → stops the function Recursive Call → calls the function again 1) 1 1 1 1 1 Flowchart…

## What’s new and why it matters
What is Recursion? Recursion means a function calls itself to solve a problem. Every recursive function has two main parts: Base Case → stops the function Recursive Call → calls the function again 1) 1 1 1 1 1 Flowchart Python def display ( num ): if num <= 5 : print ( 1 , end = " " ) display ( num + 1 ) display ( 1 ) Output: JavaScript function display ( num ) { if ( num <= 5 ) { console . log ( " 1 " ); display ( num + 1 ); } } display ( 1 ); Java public class Main { public static void main ( String [] args ) { display ( 1 ); } public static void display ( int num ) { if ( num <= 5 ) { Syste…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/keerthigap/recursion-2d67

## Related notes
- [[2026-02-26-beginner-friendly-guide---leetcode-problem-1404-c-python-javascript]]
- [[2026-02-23-beginner-friendly-guide-check-if-a-string-contains-all-binary-codes-of-size-k---problem-1461-c-python-javascript]]
- [[2026-03-06-beginner-friendly-guide-check-if-binary-string-has-at-most-one-segment-of-ones---problem-1784-c-python-javascript]]
- [[2026-02-27-beginner-friendly-guide-minimum-operations-to-equalize-binary-string---problem-3666-c-python-javascript]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-02-28-deep-dive-into-the-langbot-plugin-system-process-isolation-event-driven-hooks-component-architecture]]
