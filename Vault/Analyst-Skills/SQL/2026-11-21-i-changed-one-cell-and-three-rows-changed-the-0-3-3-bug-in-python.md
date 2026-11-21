---
title: 'I Changed One Cell and Three Rows Changed: The [[0] * 3] * 3 Bug in Python'
date: '2026-11-21'
source: https://dev.to/refactorly/i-changed-one-cell-and-three-rows-changed-the-0-3-3-bug-in-python-i0g
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-24-joining-datasets-that-never-shared-a-key-validate-cin-lei-and-wikidata-ids-then-resolve-them-in-python]]'
- '[[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]'
- '[[2026-09-25-marimo-the-reactive-python-notebook-for-reproducible-data-work]]'
- '[[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]'
- '[[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]'
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
status: unread
---

> **TL;DR:** I changed one cell in a Python grid, and all three rows changed. This bug shows up in games, matrices and dynamic-programming code all the time, and the line that causes it looks completely innocent. Every output below i…

## What’s new and why it matters
I changed one cell in a Python grid, and all three rows changed. This bug shows up in games, matrices and dynamic-programming code all the time, and the line that causes it looks completely innocent. Every output below is from Python 3.15. Video version: The bug >>> grid = [ [ 0 ] * 3 ] * 3 >>> grid [ 0 ] [ 0 ] = 1 >>> grid [ [ 1 , 0 , 0 ] , [ 1 , 0 , 0 ] , [ 1 , 0 , 0 ] ] One assignment, three changed rows. Here's the same thing in a tic-tac-toe board: board = [ [ "." ] * 3 ] * 3 board [ 1 ] [ 1 ] = "X" for row in board : print ( " " . join ( row ) ) . X . . X . . X . One move, a whole column…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/refactorly/i-changed-one-cell-and-three-rows-changed-the-0-3-3-bug-in-python-i0g

## Related notes
- [[2026-10-24-joining-datasets-that-never-shared-a-key-validate-cin-lei-and-wikidata-ids-then-resolve-them-in-python]]
- [[2026-09-21-how-to-build-a-creator-emails-pipeline-in-one-python-call]]
- [[2026-09-25-marimo-the-reactive-python-notebook-for-reproducible-data-work]]
- [[2026-09-27-how-to-optimize-a-database-one-step-at-a-time]]
- [[2026-10-27-find-low-stock-products-in-a-shopify-csv-with-60-lines-of-python]]
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
