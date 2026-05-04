---
title: certifi has 350M weekly downloads and one publisher. It handles your SSL certificates.
date: '2026-05-04'
source: https://dev.to/piiiico/certifi-has-350m-weekly-downloads-and-one-publisher-it-handles-your-ssl-certificates-1k40
domain: AI-Tools
relevance: 🔴
tags:
- '#ai'
- '#best-practice'
- '#feature'
- '#library'
- '#python'
- '#tool'
related:
- '[[2026-03-25-litellm-pypi-compromise-is-just-the-beginning-how-to-audit-your-python-dependencies-right-now]]'
- '[[2026-03-25-the-litellm-supply-chain-attack-how-mcp-servers-got-compromised-and-how-to-check-if-youre-affected]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]'
- '[[2026-03-17-i-wrapped-my-free-npm-package-as-a-paid-rest-api-heres-the-architecture]]'
- '[[2026-04-05-python-supply-chain-risk-i-scored-the-top-ai-packages-litellm-has-1-maintainer-and-12k-versions]]'
status: unread
---

> **TL;DR:** I spent last week writing about npm supply chain risk . Then I ran the same analysis on Python. The findings are different. In some ways worse. The setup I built a tool called Proof of Commitment that scores packages on…

## What’s new and why it matters
I spent last week writing about npm supply chain risk . Then I ran the same analysis on Python. The findings are different. In some ways worse. The setup I built a tool called Proof of Commitment that scores packages on behavioral signals: publisher depth, download momentum, release consistency, age. "Publisher depth" is the critical one — how many people have PyPI publish access? A package with one publisher and 300M weekly downloads is structurally fragile in a specific way: one compromised account enables a malicious publish to that entire install base. For npm, the notable CRITICALs are th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Reproduce the example in a notebook; then refactor into a reusable function.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/piiiico/certifi-has-350m-weekly-downloads-and-one-publisher-it-handles-your-ssl-certificates-1k40

## Related notes
- [[2026-03-25-litellm-pypi-compromise-is-just-the-beginning-how-to-audit-your-python-dependencies-right-now]]
- [[2026-03-25-the-litellm-supply-chain-attack-how-mcp-servers-got-compromised-and-how-to-check-if-youre-affected]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-17-maybe-this-is-how-open-source-apps-are-born]]
- [[2026-03-17-i-wrapped-my-free-npm-package-as-a-paid-rest-api-heres-the-architecture]]
- [[2026-04-05-python-supply-chain-risk-i-scored-the-top-ai-packages-litellm-has-1-maintainer-and-12k-versions]]
