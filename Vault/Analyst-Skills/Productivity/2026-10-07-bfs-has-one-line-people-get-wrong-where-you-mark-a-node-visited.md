---
title: 'BFS has one line people get wrong: where you mark a node visited'
date: '2026-10-07'
source: https://dev.to/jackson_s_33a25dbcc9fc24e/bfs-has-one-line-people-get-wrong-where-you-mark-a-node-visited-3gc1
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#career'
- '#productivity'
- '#python'
- '#tool'
- '#zendesk'
related:
- '[[2026-10-05-how-to-get-google-search-volume-for-a-list-of-keywords-without-a-google-ads-account]]'
- '[[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]'
- '[[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]'
- '[[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]'
- '[[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]'
- '[[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]'
status: unread
---

> **TL;DR:** Breadth-first search is usually the second graph algorithm anyone learns, and it looks almost too simple: a queue, a loop, a visited set. Most BFS bugs I see come down to one decision in that loop: when you mark a node a…

## What’s new and why it matters
Breadth-first search is usually the second graph algorithm anyone learns, and it looks almost too simple: a queue, a loop, a visited set. Most BFS bugs I see come down to one decision in that loop: when you mark a node as visited . The idea, without code Drop a stone in a pond. The first ripple reaches everything one step away, the second ripple everything two steps away, and so on. BFS explores a graph the same way. It visits every neighbour of the start node, then every neighbour of those, one layer at a time. The queue is what keeps the layers in order. It is first-in, first-out, so every n…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/jackson_s_33a25dbcc9fc24e/bfs-has-one-line-people-get-wrong-where-you-mark-a-node-visited-3gc1

## Related notes
- [[2026-10-05-how-to-get-google-search-volume-for-a-list-of-keywords-without-a-google-ads-account]]
- [[2026-05-09-i-built-a-simple-ai-text-summarizer-in-python]]
- [[2026-06-16-sql-or-python-the-line-is-sharper-than-you-think-with-code]]
- [[2026-09-01-i-raced-six-models-against-each-other-on-digitalocean-inference-the-cheapest-one-won]]
- [[2026-09-27-i-built-an-ai-agent-that-snapshots-every-edit-and-runs-your-tests-before-it-says-done]]
- [[2026-07-24-ai-generated-sql-has-a-silent-failure-problem-heres-a-way-to-catch-it]]
