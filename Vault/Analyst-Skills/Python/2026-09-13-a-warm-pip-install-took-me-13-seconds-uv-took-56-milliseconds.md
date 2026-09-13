---
title: A warm pip install took me 13 seconds. uv took 56 milliseconds.
date: '2026-09-13'
source: https://dev.to/remdore/a-warm-pip-install-took-me-13-seconds-uv-took-56-milliseconds-3ehp
domain: Python
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]'
status: unread
---

> **TL;DR:** A warm pip install of a normal web backend took 13 seconds on my machine. The same install with uv took 56 milliseconds. Not 56 milliseconds faster. 56 milliseconds total, for 63 packages, including numpy and pandas and…

## What’s new and why it matters
A warm pip install of a normal web backend took 13 seconds on my machine. The same install with uv took 56 milliseconds. Not 56 milliseconds faster. 56 milliseconds total, for 63 packages, including numpy and pandas and pillow. I did not believe it either, so I ran it enough times to be sure the number was real and not a no-op. It is real, and the reason it is real is the interesting part. What I measured uv is the Python package installer from Astral, the company behind the Ruff linter, written in Rust and aimed squarely at pip. The pitch is "10 to 100 times faster". I wanted to know where in…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/remdore/a-warm-pip-install-took-me-13-seconds-uv-took-56-milliseconds-3ehp

## Related notes
- [[2026-07-18-im-not-a-real-developer-so-i-built-my-app-the-simplest-way-possible]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-03-14-176-trades-on-polymarket-what-my-bot-actually-made-its-not-what-you-think]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-08-12-sql-ctes-how-to-build-a-query-in-steps-you-can-check]]
