---
title: A Python TLS probe that keeps certificate verification enabled
date: '2026-11-12'
source: https://dev.to/pki-channnel/a-python-tls-probe-that-keeps-certificate-verification-enabled-18fl
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
- '[[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]'
- '[[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]'
- '[[2026-09-14-test-the-next-effect-not-just-the-first-tool-call]]'
- '[[2026-08-14-recent-checkout-errors-polling-an-api-for-unresolved-slack-and-email-alerts]]'
- '[[2026-10-12-how-to-build-an-ai-tool-a-7-step-checklist-from-problem-definition-to-monitoring]]'
status: unread
---

> **TL;DR:** A script that works only after setting verify=False has lost an important part of its connection check. Before changing trust settings, make the failure observable: which host did the program contact, which name did it v…

## What’s new and why it matters
A script that works only after setting verify=False has lost an important part of its connection check. Before changing trust settings, make the failure observable: which host did the program contact, which name did it verify, and did it reach the TLS handshake? This example uses Python's standard library. It opens one connection to a service you are authorized to test, performs a TLS handshake, prints a few certificate fields, and exits. It does not send an HTTP request or change the operating system's trust store. The complete probe Save this as tls_probe.py . Pass a hostname, without https:…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/pki-channnel/a-python-tls-probe-that-keeps-certificate-verification-enabled-18fl

## Related notes
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
- [[2026-11-11-five-security-tests-for-mcp-servers-and-agents-in-173-lines-of-python]]
- [[2026-07-30-trace-ai-coding-changes-to-requirements-with-python-and-sarif]]
- [[2026-09-14-test-the-next-effect-not-just-the-first-tool-call]]
- [[2026-08-14-recent-checkout-errors-polling-an-api-for-unresolved-slack-and-email-alerts]]
- [[2026-10-12-how-to-build-an-ai-tool-a-7-step-checklist-from-problem-definition-to-monitoring]]
