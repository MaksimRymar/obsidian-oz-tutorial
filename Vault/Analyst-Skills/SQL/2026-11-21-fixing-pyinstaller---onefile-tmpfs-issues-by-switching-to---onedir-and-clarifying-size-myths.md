---
title: Fixing PyInstaller --onefile tmpfs Issues by Switching to --onedir and Clarifying
  Size Myths
date: '2026-11-21'
source: https://dev.to/romdevin/fixing-pyinstaller-onefile-tmpfs-issues-by-switching-to-onedir-and-clarifying-size-myths-3bpn
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
- '[[2026-09-02-why-serverless-engineers-already-understand-containers]]'
- '[[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]'
status: unread
---

> **TL;DR:** Anatomy of the --onefile vs. --onedir Bundle and the Size Myth When you pass --onefile to PyInstaller, the build tool does not strip dead code, prune unused shared libraries, or shrink your Python interpreter. Instead, t…

## What’s new and why it matters
Anatomy of the --onefile vs. --onedir Bundle and the Size Myth When you pass --onefile to PyInstaller, the build tool does not strip dead code, prune unused shared libraries, or shrink your Python interpreter. Instead, the bootloader appends a compressed archive (typically using zlib or LZMA) containing the exact same set of .pyc bytecode files, .so / .dll shared objects, and data assets that a --onedir build places into a directory tree. If your bundle contains a 600 MB scientific or machine learning stack, --onefile still carries all 600 MB of underlying payload inside that single executable…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/romdevin/fixing-pyinstaller-onefile-tmpfs-issues-by-switching-to-onedir-and-clarifying-size-myths-3bpn

## Related notes
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-08-26-the-postgres-insert-that-fails-right-after-a-successful-load]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
- [[2026-09-02-why-serverless-engineers-already-understand-containers]]
- [[2026-10-28-python-google-sheets-on-autopilot-why-your-script-dies-after-7-days-and-4-more-errors]]
