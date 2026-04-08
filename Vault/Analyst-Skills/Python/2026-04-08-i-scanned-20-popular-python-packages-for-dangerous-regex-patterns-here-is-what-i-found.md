---
title: I scanned 20 popular Python packages for dangerous regex patterns. Here is
  what I found.
date: '2026-04-08'
source: https://dev.to/harshithreddy01/i-scanned-20-popular-python-packages-for-dangerous-regex-patterns-here-is-what-i-found-dg6
domain: Python
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]'
- '[[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** At 13:42 UTC on July 2, 2019, an engineer working for Cloudflare made changes to the regular ruleset that was being used by their Web Application Firewall. In under three minutes, there was an 80% drop in the amount of t…

## What’s new and why it matters
At 13:42 UTC on July 2, 2019, an engineer working for Cloudflare made changes to the regular ruleset that was being used by their Web Application Firewall. In under three minutes, there was an 80% drop in the amount of traffic globally. The load on all HTTP serving CPUs in their network hit 100%. It was caused by one regular expression intended to detect XSS attacks, which contained the regular expression pattern .*(?:.*=.*) . This pattern included two quantifiers using .* on the same character class. That was the result of a production ReDoS. I was interested to know how frequent such pattern…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/harshithreddy01/i-scanned-20-popular-python-packages-for-dangerous-regex-patterns-here-is-what-i-found-dg6

## Related notes
- [[2026-04-03-i-built-a-pii-detection-api-with-zero-ai-cost-pure-regex]]
- [[2026-03-16-build-your-first-multi-agent-system-in-python-3-patterns-that-scale]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-14-the-ai-engineering-stack-in-2026-what-to-learn-first]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
