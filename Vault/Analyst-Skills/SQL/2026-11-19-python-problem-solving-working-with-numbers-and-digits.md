---
title: 'Python Problem Solving: Working with Numbers and Digits'
date: '2026-11-19'
source: https://dev.to/megalraja/python-problem-solving-working-with-numbers-and-digits-53i8
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-06-11-problems-can-be-solved-using-modulo-and-float-operators]]'
- '[[2026-07-03-why-does-a-list-change-in-two-variables]]'
- '[[2026-03-15-count-commas-in-range---leetcode-3870-solution]]'
- '[[2026-09-19-how-i-built-a-visual-python-calculator-in-the-terminal]]'
- '[[2026-06-28-the-python-interview-roadmap-what-to-learn-in-what-order-before-someone-asks-you-about-the-gil]]'
- '[[2026-02-26-beginner-friendly-guide---leetcode-problem-1404-c-python-javascript]]'
status: unread
---

> **TL;DR:** Let's solve a simple Python problem using a while loop. 1. Can we count the number of digits in a given number? Example: num = 12345 Solution: First, introduce a variable called count and initialize it to 0 . num = 12345…

## What’s new and why it matters
Let's solve a simple Python problem using a while loop. 1. Can we count the number of digits in a given number? Example: num = 12345 Solution: First, introduce a variable called count and initialize it to 0 . num = 12345 count = 0 # Initial value is zero while num != 0 : num = num // 10 # Removes the last digit count += 1 print ( "Number of digits:" , count ) Explanation: num = num // 10 removes the last digit from the number. count += 1 increases the count by 1. The loop continues until the number becomes 0. Output: Number of digits: 5 That's it! We counted the total number of digits using a…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/megalraja/python-problem-solving-working-with-numbers-and-digits-53i8

## Related notes
- [[2026-06-11-problems-can-be-solved-using-modulo-and-float-operators]]
- [[2026-07-03-why-does-a-list-change-in-two-variables]]
- [[2026-03-15-count-commas-in-range---leetcode-3870-solution]]
- [[2026-09-19-how-i-built-a-visual-python-calculator-in-the-terminal]]
- [[2026-06-28-the-python-interview-roadmap-what-to-learn-in-what-order-before-someone-asks-you-about-the-gil]]
- [[2026-02-26-beginner-friendly-guide---leetcode-problem-1404-c-python-javascript]]
