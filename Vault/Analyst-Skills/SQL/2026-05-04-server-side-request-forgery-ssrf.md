---
title: Server-Side Request Forgery (SSRF)
date: '2026-05-04'
source: https://dev.to/safron/server-side-request-forgery-ssrf-ede
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-03-09-how-to-audit-production-code-a-5-layer-bug-hunting-methodology]]'
- '[[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]'
- '[[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
status: unread
---

> **TL;DR:** Your application fetches a URL. The user supplied it. Your server makes the request, follows the redirect, and returns the content. The URL pointed to http://169.254.169.254/latest/metadata/iam/security-credentials/produ…

## What’s new and why it matters
Your application fetches a URL. The user supplied it. Your server makes the request, follows the redirect, and returns the content. The URL pointed to http://169.254.169.254/latest/metadata/iam/security-credentials/production-role . Your application just handed the attacker your cloud credentials. TL;DR SSRF lets an attacker trick your server into making requests on their behalf — to internal services, cloud metadata endpoints, or infrastructure never meant to be reachable from the outside. CVE-2024-29415 in the npm ip package allowed attackers to bypass SSRF protections using non-standard IP…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/safron/server-side-request-forgery-ssrf-ede

## Related notes
- [[2026-03-09-how-to-audit-production-code-a-5-layer-bug-hunting-methodology]]
- [[2026-04-22-your-pytest-retries-are-lying-to-you-the-hidden-cost-of---reruns-and-the-plugin-i-wrote-so-i-could-actually-see-what-my-]]
- [[2026-03-13-test-your-ai-agent-like-a-senior-engineer-4-patterns-that-work]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
