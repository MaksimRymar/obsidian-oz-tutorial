---
title: 'I built rboto: async-only, fully typed Python clients for 34 AWS services,
  powered by Rust'
date: '2026-11-02'
source: https://dev.to/leandrodamascena/i-built-rboto-async-only-fully-typed-python-clients-for-34-aws-services-powered-by-rust-625
domain: Python
relevance: 🔴
tags:
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-09-14-coming-from-java-functions-are-values-in-python]]'
- '[[2026-08-19-a-practical-guide-to-the-ace-data-cloud-python-sdk]]'
- '[[2026-10-31-opendsec-self-hosted-sandboxes-for-rl-rollouts-and-code-running-agents]]'
- '[[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]'
- '[[2026-03-13-using-marshmallow-method-fields-for-complex-nested-schemas-in-flask]]'
- '[[2026-10-07-building-a-secure-django-rest-api-for-task-management]]'
status: unread
---

> **TL;DR:** About a year ago, I had an idea for a Python ORM for DynamoDB. I wanted a good developer experience, async support, and strong typing, but I also wanted to move expensive work out of the Python layer. That became pydynox…

## What’s new and why it matters
About a year ago, I had an idea for a Python ORM for DynamoDB. I wanted a good developer experience, async support, and strong typing, but I also wanted to move expensive work out of the Python layer. That became pydynox , with a Rust core handling serialization and other CPU-heavy work. More recently, I started thinking about the SDK underneath applications that use several AWS services. Especially with agents, a workflow might combine model calls with documents in S3, state in DynamoDB, and messages in SQS. Async calls and clear input and output types matter there too. Whether a developer or…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/leandrodamascena/i-built-rboto-async-only-fully-typed-python-clients-for-34-aws-services-powered-by-rust-625

## Related notes
- [[2026-09-14-coming-from-java-functions-are-values-in-python]]
- [[2026-08-19-a-practical-guide-to-the-ace-data-cloud-python-sdk]]
- [[2026-10-31-opendsec-self-hosted-sandboxes-for-rl-rollouts-and-code-running-agents]]
- [[2026-10-17-check-that-a-package-exists-before-your-ai-agent-installs-it]]
- [[2026-03-13-using-marshmallow-method-fields-for-complex-nested-schemas-in-flask]]
- [[2026-10-07-building-a-secure-django-rest-api-for-task-management]]
