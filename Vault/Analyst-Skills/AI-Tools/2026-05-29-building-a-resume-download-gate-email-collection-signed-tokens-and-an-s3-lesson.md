---
title: 'Building a Resume Download Gate: Email Collection, Signed Tokens, and an S3
  Lesson'
date: '2026-05-29'
source: https://dev.to/highcenburg/building-a-resume-download-gate-email-collection-signed-tokens-and-an-s3-lesson-32f2
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#feature'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]'
- '[[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]'
- '[[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]'
- '[[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]'
- '[[2026-04-02-your-otp-flow-is-only-as-reliable-as-the-route-behind-it-build-otp-delivery-with-programmable-routing-in-python]]'
- '[[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]'
status: unread
---

> **TL;DR:** I wanted a soft gate on my resume download. Not a paywall. Just an email field — enough friction to filter bots, enough signal to know who's interested. What started as a straightforward feature turned into a three-part…

## What’s new and why it matters
I wanted a soft gate on my resume download. Not a paywall. Just an email field — enough friction to filter bots, enough signal to know who's interested. What started as a straightforward feature turned into a three-part lesson: stateless token signing, S3 public access, and email delivery mechanics. Here's the full story. The Feature The flow I wanted: Visitor clicks "Download Resume" on the About page or Hero A modal asks for their email Backend validates the email (format + disposable domain check) A signed, time-limited link is emailed to them They click the link, the PDF opens No database…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/highcenburg/building-a-resume-download-gate-email-collection-signed-tokens-and-an-s3-lesson-32f2

## Related notes
- [[2026-05-25-i-added-mcp-support-to-my-saas-in-an-afternoon-heres-the-whole-thing]]
- [[2026-04-03-i-got-tired-of-watching-my-terminal-so-i-built-guga]]
- [[2026-05-02-uncovering-8-indexeddb-data-loss-after-browser-crashes-with-playwright]]
- [[2026-04-02-how-to-stop-your-ai-agent-from-burning-400month-on-api-calls]]
- [[2026-04-02-your-otp-flow-is-only-as-reliable-as-the-route-behind-it-build-otp-delivery-with-programmable-routing-in-python]]
- [[2026-03-08-building-autonomous-ai-agents-that-actually-do-work]]
