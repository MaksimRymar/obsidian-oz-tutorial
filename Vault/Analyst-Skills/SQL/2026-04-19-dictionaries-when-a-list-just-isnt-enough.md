---
title: 'Dictionaries: When a List Just Isn''t Enough'
date: '2026-04-19'
source: https://dev.to/yakhilesh/dictionaries-when-a-list-just-isnt-enough-27o9
domain: SQL
relevance: 🟡
tags:
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-19-build-your-own-types-classes-explained-simply]]'
- '[[2026-04-19-reading-files-without-breaking-everything]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-03-26-create-tables]]'
- '[[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** You have a list of five numbers. person = [ " Alex " , 25 , " Mumbai " , True , " alex@email.com " ] Quick question. What is person[3] ? You have to count. Index 0 is the name. Index 1 is age. Index 2 is city. Index 3 is…

## What’s new and why it matters
You have a list of five numbers. person = [ " Alex " , 25 , " Mumbai " , True , " alex@email.com " ] Quick question. What is person[3] ? You have to count. Index 0 is the name. Index 1 is age. Index 2 is city. Index 3 is... the boolean? What does True mean here? Is that married? Is that a student? Is that something else entirely? You wrote this code yourself and you already can't remember what index 3 means. Now imagine coming back to this code three weeks later. This is the exact problem dictionaries solve. Instead of accessing data by position, you access it by name. Instead of person[3] you…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/yakhilesh/dictionaries-when-a-list-just-isnt-enough-27o9

## Related notes
- [[2026-04-19-build-your-own-types-classes-explained-simply]]
- [[2026-04-19-reading-files-without-breaking-everything]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-03-26-create-tables]]
- [[2026-03-13-i-built-and-launched-a-mobile-app-in-3-months-as-a-solo-engineer-heres-exactly-what-happened]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
