---
title: 'One tar Command, Eight Extractions: The 512 Bytes POSIX Left Unspecified'
date: '2026-11-10'
source: https://dev.to/chenyuan20509/one-tar-command-eight-extractions-the-512-bytes-posix-left-unspecified-4nl7
domain: Productivity
relevance: 🔴
tags:
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]'
- '[[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-08-12-sql-foundations-start-to-finish]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
status: unread
---

> **TL;DR:** How many files should come out of an archive that was built from three? Every tool you have ever used will answer three, and for any normal archive they would be right. On November 7, Harmen Stoppels published a ten-kilo…

## What’s new and why it matters
How many files should come out of an archive that was built from three? Every tool you have ever used will answer three, and for any normal archive they would be right. On November 7, Harmen Stoppels published a ten-kilobyte tar file, built with a single GNU tar invocation and no hand-assembled bytes, for which the honest answer depends entirely on which program you ask. GNU tar returns three files. The tar that ships with macOS returns two, one of them silently corrupted. 7-Zip returns two and never mentions the third. R returns three, one padded with 512 zero bytes it pulled from the archive…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/chenyuan20509/one-tar-command-eight-extractions-the-512-bytes-posix-left-unspecified-4nl7

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-11-05-your-ai-says-fixed-would-a-test-notice-if-it-wasnt]]
- [[2026-09-22-we-have-no-marketing-state-table-only-five-sql-windows-over-timestamps-we-already-had]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-08-12-sql-foundations-start-to-finish]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
