---
title: My Stripe delivery script silently skipped a paid customer for 7 days
date: '2026-04-25'
source: https://dev.to/whoffagents/my-stripe-delivery-script-silently-skipped-a-paid-customer-for-7-days-j37
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-04-02-your-otp-flow-is-only-as-reliable-as-the-route-behind-it-build-otp-delivery-with-programmable-routing-in-python]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
status: unread
---

> **TL;DR:** The bug was one line of code. It cost a customer 7 days of waiting. I run a small shop that sells Claude Code skill packs. When someone buys, a Python script polls Stripe for new charges and sends the product zip via Res…

## What’s new and why it matters
The bug was one line of code. It cost a customer 7 days of waiting. I run a small shop that sells Claude Code skill packs. When someone buys, a Python script polls Stripe for new charges and sends the product zip via Resend. Simple enough. Here's what the original delivery loop looked like: for charge in charges : if charge . id in processed : continue try : send_delivery_email ( to_email , zip_filename , charge . id ) except Exception as e : log . error ( " Delivery error: %s " , e ) processed . add ( charge . id ) # BUG: runs even if delivery failed save_state ( state ) Can you see it? proce…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/whoffagents/my-stripe-delivery-script-silently-skipped-a-paid-customer-for-7-days-j37

## Related notes
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-04-02-your-otp-flow-is-only-as-reliable-as-the-route-behind-it-build-otp-delivery-with-programmable-routing-in-python]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
