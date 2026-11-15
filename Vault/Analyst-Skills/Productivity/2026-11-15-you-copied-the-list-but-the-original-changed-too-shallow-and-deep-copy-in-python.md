---
title: You copied the list, but the original changed too. Shallow and deep copy in
  Python
date: '2026-11-15'
source: https://dev.to/talentopsystems/you-copied-the-list-but-the-original-changed-too-shallow-and-deep-copy-in-python-5hkn
domain: Productivity
relevance: 🟡
tags:
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-10-31-modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-08-22-build-an-overnight-bug-bounty-recon-pipeline-with-python-step-by-step]]'
- '[[2026-10-22-sql-ties-python-at-58-what-it-means-for-data-engineer-interviews]]'
- '[[2026-09-25-if-a-list-endpoint-returns-exactly-as-many-rows-as-you-asked-for-you-have-a-bug]]'
- '[[2026-03-15-easy-query-the-most-powerful-orm-for-java]]'
status: unread
---

> **TL;DR:** Checked against official sources on November 15, 2026 You make a copy of a list. You change the copy. Then you look at the first list, and it changed too. Nothing is broken. Python did what it was told. The copy was only…

## What’s new and why it matters
Checked against official sources on November 15, 2026 You make a copy of a list. You change the copy. Then you look at the first list, and it changed too. Nothing is broken. Python did what it was told. The copy was only one level deep. Everything below was run in Python 3.13.5. The bug in six lines a = [ [ 1 , 2 ] , [ 3 , 4 ] ] b = a . copy ( ) b [ 0 ] . append ( 99 ) print ( a ) It prints: [ [ 1 , 2 , 99 ] , [ 3 , 4 ] ] We changed b , and a shows the new number. Why? What a shallow copy really does a.copy() makes a new outer list. But the inner lists are not copied. The new list just points…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/talentopsystems/you-copied-the-list-but-the-original-changed-too-shallow-and-deep-copy-in-python-5hkn

## Related notes
- [[2026-10-31-modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-08-22-build-an-overnight-bug-bounty-recon-pipeline-with-python-step-by-step]]
- [[2026-10-22-sql-ties-python-at-58-what-it-means-for-data-engineer-interviews]]
- [[2026-09-25-if-a-list-endpoint-returns-exactly-as-many-rows-as-you-asked-for-you-have-a-bug]]
- [[2026-03-15-easy-query-the-most-powerful-orm-for-java]]
