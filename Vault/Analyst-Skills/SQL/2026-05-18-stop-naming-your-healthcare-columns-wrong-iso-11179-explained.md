---
title: Stop Naming Your Healthcare Columns Wrong — ISO-11179 Explained
date: '2026-05-18'
source: https://dev.to/season_mudbhary_7856e4083/stop-naming-your-healthcare-columns-wrong-iso-11179-explained-2hnb
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
- '#tutorial'
- '#zendesk'
related:
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-09-sql-window-functions-dont-have-to-be-scary]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
- '[[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]'
status: unread
---

> **TL;DR:** If you've ever inherited a healthcare database with columns named DOB , PatientID , or CLAIM_NUMBER — this guide is for you. Healthcare data engineering has a naming problem. Every team, every vendor, every health plan n…

## What’s new and why it matters
If you've ever inherited a healthcare database with columns named DOB , PatientID , or CLAIM_NUMBER — this guide is for you. Healthcare data engineering has a naming problem. Every team, every vendor, every health plan names their columns differently. A "member ID" becomes MemberID in one system, mem_id in another, PATIENT_KEY in a third, and mbr_identifier in a fourth. When you try to join these systems — and you always have to join them — you spend more time figuring out what columns mean than actually building the pipeline. There's a standard that solves this. Most healthcare data engineers…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/season_mudbhary_7856e4083/stop-naming-your-healthcare-columns-wrong-iso-11179-explained-2hnb

## Related notes
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-09-sql-window-functions-dont-have-to-be-scary]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-05-07-how-databricks-genie-turns-plain-english-into-sql-code]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
- [[2026-05-06-four-ways-to-use-ai-with-your-database-in-vs-code]]
