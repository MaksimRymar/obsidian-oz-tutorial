---
title: How to Add SMS Fallback to B2B Password Reset Emails
date: '2026-09-20'
source: https://dev.to/rhettmurray8263/how-to-add-sms-fallback-to-b2b-password-reset-emails-904
domain: AI-Tools
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]'
- '[[2026-09-09-media-sms-alerts-api-in-2026-polling-transactional-notification-status-without-webhooks]]'
- '[[2026-08-11-a-simple-openai-compatible-python-backend-api-for-prompt-to-image-marketing-assets]]'
- '[[2026-09-09-how-to-implement-a-saas-sms-otp-api-for-useu-login-2026-retry-rules]]'
- '[[2026-09-14-python-email-recovery-transactional-templates-custom-domains-dkim-and-api-sends]]'
- '[[2026-08-05-decision-record-an-in-app-saas-chatbot-api-with-one-key-and-durable-transcripts]]'
status: unread
---

> **TL;DR:** Use an email reset link as the primary recovery path. Add SMS OTP as a separate fallback only for an account whose phone number was already verified; do not make recovery depend on SMS. For a B2B SaaS product that routes…

## What’s new and why it matters
Use an email reset link as the primary recovery path. Add SMS OTP as a separate fallback only for an account whose phone number was already verified; do not make recovery depend on SMS. For a B2B SaaS product that routes contact forms into support queues, this keeps an administrator able to recover access even when the product team decides that phone verification adds too much enrollment friction. TL;DR: evaluate email-first and email-plus-SMS as two explicit designs. Pass a design only when email recovery remains independent, SMS is limited to previously verified numbers, and the business lay…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/rhettmurray8263/how-to-add-sms-fallback-to-b2b-password-reset-emails-904

## Related notes
- [[2026-08-14-structured-json-app-logs-that-survive-a-vendor-switch-what-a-small-saas-should-check]]
- [[2026-09-09-media-sms-alerts-api-in-2026-polling-transactional-notification-status-without-webhooks]]
- [[2026-08-11-a-simple-openai-compatible-python-backend-api-for-prompt-to-image-marketing-assets]]
- [[2026-09-09-how-to-implement-a-saas-sms-otp-api-for-useu-login-2026-retry-rules]]
- [[2026-09-14-python-email-recovery-transactional-templates-custom-domains-dkim-and-api-sends]]
- [[2026-08-05-decision-record-an-in-app-saas-chatbot-api-with-one-key-and-durable-transcripts]]
