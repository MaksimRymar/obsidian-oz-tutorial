---
title: I Needed Collapsible App Groups in Django Admin, So I Built a Package
date: '2026-07-10'
source: https://dev.to/kroxiksut/i-needed-collapsible-app-groups-in-django-admin-so-i-built-a-package-45nm
domain: SQL
relevance: 🔴
tags:
- '#ai'
- '#feature'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-09-untyped-python-let-antigravity-goal-do-the-cleanup]]'
- '[[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]'
- '[[2026-04-27-managing-background-tasks-in-fastapi-from-basic-to-production-ready-beyond-fire-and-forget]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-07-10-build-a-location-aware-serp-check-for-local-seo-experiments]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
status: unread
---

> **TL;DR:** The built-in Django Admin works well, especially while a project is still small. But as a project grows, the sidebar gradually fills up with more applications and models: users, permissions, products, orders, reports, in…

## What’s new and why it matters
The built-in Django Admin works well, especially while a project is still small. But as a project grows, the sidebar gradually fills up with more applications and models: users, permissions, products, orders, reports, integrations, internal reference data, and many other sections. Most of these sections are not used all the time. In one project, an administrator may spend most of the day working with orders and customers, while dozens of rarely used models remain visible in the sidebar. At some point, I wanted to add a very simple feature to the standard Django Admin sidebar: click an arrow ne…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/kroxiksut/i-needed-collapsible-app-groups-in-django-admin-so-i-built-a-package-45nm

## Related notes
- [[2026-07-09-untyped-python-let-antigravity-goal-do-the-cleanup]]
- [[2026-06-24-semantic-search-with-postgresql-pragmatism-beats-hype---most-of-the-time]]
- [[2026-04-27-managing-background-tasks-in-fastapi-from-basic-to-production-ready-beyond-fire-and-forget]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-07-10-build-a-location-aware-serp-check-for-local-seo-experiments]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
