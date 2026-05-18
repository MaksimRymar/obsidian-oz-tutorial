---
title: 'Day 84: Merging Cognito Identities & Surviving a 502 Gateway Error'
date: '2026-05-18'
source: https://dev.to/ericrodriguez10/day-84-merging-cognito-identities-surviving-a-502-gateway-error-3hb5
domain: Productivity
relevance: 🟡
tags:
- '#feature'
- '#library'
- '#productivity'
- '#python'
- '#tool'
related:
- '[[2026-04-15-beginners-sql-machinelearning-100daysofcode]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-13-from-data-to-decisions-designing-an-ai-seo-agent-with-azure-openai-python]]'
- '[[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]'
- '[[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]'
- '[[2026-04-24-started-giving-my-agents-my-credit-card]]'
status: unread
---

> **TL;DR:** Today I almost broke my serverless production environment, but AWS disaster recovery features saved the day. I was deploying a major update to my Financial Agent to fix a split identity issue. Users logging in with Email…

## What’s new and why it matters
Today I almost broke my serverless production environment, but AWS disaster recovery features saved the day. I was deploying a major update to my Financial Agent to fix a split identity issue. Users logging in with Email/Password and Google OAuth were getting separate DynamoDB partitions. I rewrote the backend to unify the identity resolution around the verified email address. At the same time, I was updating the transaction classification logic. The system needed to strictly separate refunds/credits from actual income so the AI wouldn't hallucinate false financial praise. The Deployment Incid…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/ericrodriguez10/day-84-merging-cognito-identities-surviving-a-502-gateway-error-3hb5

## Related notes
- [[2026-04-15-beginners-sql-machinelearning-100daysofcode]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-13-from-data-to-decisions-designing-an-ai-seo-agent-with-azure-openai-python]]
- [[2026-04-23-i-built-a-browser-only-sql-practice-tool-because-installing-dbeaver-is-a-productivity-tax]]
- [[2026-03-09-i-got-frustrated-my-ai-kept-forgetting-me-so-i-spent-6-months-building-a-fix]]
- [[2026-04-24-started-giving-my-agents-my-credit-card]]
