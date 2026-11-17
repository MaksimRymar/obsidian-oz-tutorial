---
title: New attack with fake delivery documents infects Windows computers
date: '2026-11-17'
source: https://dev.to/hacksgr/new-attack-with-fake-delivery-documents-infects-windows-computers-4mg1
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#zendesk'
related:
- '[[2026-03-28-from-pixels-to-payload-lsb-steganography-and-in-memory-execution]]'
- '[[2026-04-27-managing-background-tasks-in-fastapi-from-basic-to-production-ready-beyond-fire-and-forget]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-10-30-your-model-archive-can-carry-a-program-check-members-by-their-bytes]]'
- '[[2026-09-15-how-to-extract-tables-from-word-documents-with-python]]'
- '[[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]'
status: unread
---

> **TL;DR:** Researchers have detailed a multi-stage malware campaign utilizing a shipment-themed ZIP archive to execute a complex delivery chain. The attack leverages DLL side-loading via a signed Kingsoft PDF executable, a disguise…

## What’s new and why it matters
Researchers have detailed a multi-stage malware campaign utilizing a shipment-themed ZIP archive to execute a complex delivery chain. The attack leverages DLL side-loading via a signed Kingsoft PDF executable, a disguised WinRAR utility, and a renamed Python runtime to decode and execute a payload communicating with PureRAT infrastructure. According to research by Unit 42 published on November 16, 2026, this activity was recorded after an infection incident on October 21. The attackers are distributing a file with a mission-related name, which contains a genuine and legally signed document rea…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hacksgr/new-attack-with-fake-delivery-documents-infects-windows-computers-4mg1

## Related notes
- [[2026-03-28-from-pixels-to-payload-lsb-steganography-and-in-memory-execution]]
- [[2026-04-27-managing-background-tasks-in-fastapi-from-basic-to-production-ready-beyond-fire-and-forget]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-10-30-your-model-archive-can-carry-a-program-check-members-by-their-bytes]]
- [[2026-09-15-how-to-extract-tables-from-word-documents-with-python]]
- [[2026-08-18-the-duplicate-rows-query-you-re-google-every-six-weeks]]
