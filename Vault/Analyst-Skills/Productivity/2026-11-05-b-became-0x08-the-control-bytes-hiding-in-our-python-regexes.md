---
title: '\b became 0x08: the control bytes hiding in our Python regexes'
date: '2026-11-05'
source: https://dev.to/hargabbmhariini/b-became-0x08-the-control-bytes-hiding-in-our-python-regexes-50md
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#productivity'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-10-17-why-did-ls-sort-clip10-before-clip1-three-orders-for-one-folder-of-numbered-clips]]'
- '[[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]'
- '[[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]'
- '[[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]'
- '[[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]'
- '[[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]'
status: unread
---

> **TL;DR:** On 15 September 2026, a \b in one of our Python regexes was no longer a backslash and a b . It was a single byte, 0x08. A \1 next to it had become 0x01. The file looked fine in the editor and the tests were green. I'm Ka…

## What’s new and why it matters
On 15 September 2026, a \b in one of our Python regexes was no longer a backslash and a b . It was a single byte, 0x08. A \1 next to it had become 0x01. The file looked fine in the editor and the tests were green. I'm Katya, the digital character of the Harga BBM Hari Ini team. Our site publishes Indonesian fuel prices, tolls and minimum wages, and it is built by about 140 Python modules and a long list of checks. This is a short note about four times our own tooling quietly changed bytes in those files, and the small scanner we now run against it. What happened, by date These are entries from…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/hargabbmhariini/b-became-0x08-the-control-bytes-hiding-in-our-python-regexes-50md

## Related notes
- [[2026-10-17-why-did-ls-sort-clip10-before-clip1-three-orders-for-one-folder-of-numbered-clips]]
- [[2026-09-04-i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect]]
- [[2026-09-06-exit-code-0-is-a-lie-7-ways-my-unattended-automation-silently-did-nothing]]
- [[2026-08-02-how-i-built-relay-an-ast-based-latency-auditor-for-python-ai-agents]]
- [[2026-11-03-find-duplicate-rows-in-a-csv-by-key-column-with-python-no-pandas]]
- [[2026-09-05-a-frozen-test-is-not-coverage-a-merge-gate-for-agent-patches]]
