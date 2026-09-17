---
title: 'Oracle ORA-12728 Error: Causes and Solutions Complete Guide'
date: '2026-09-17'
source: https://dev.to/dbmserror/oracle-ora-12728-error-causes-and-solutions-complete-guide-b6l
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#sql'
- '#tool'
- '#tutorial'
related:
- '[[2026-09-16-oracle-ora-12722-error-causes-and-solutions-complete-guide]]'
- '[[2026-09-17-oracle-ora-12723-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-16-oracle-ora-00909-error-causes-and-solutions-complete-guide]]'
- '[[2026-07-11-postgresql-42710-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-25-oracle-ora-01001-error-causes-and-solutions-complete-guide]]'
- '[[2026-06-23-oracle-ora-00964-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** ORA-12728: Invalid Range in Regular Expression ORA-12728 is thrown by Oracle when a regular expression contains an invalid character range inside square brackets, such as [z-a] or [9-0] , where the start of the range has…

## What’s new and why it matters
ORA-12728: Invalid Range in Regular Expression ORA-12728 is thrown by Oracle when a regular expression contains an invalid character range inside square brackets, such as [z-a] or [9-0] , where the start of the range has a higher code point than the end. This error can appear in any Oracle SQL or PL/SQL context that uses regex functions: REGEXP_LIKE , REGEXP_REPLACE , REGEXP_SUBSTR , REGEXP_INSTR , and REGEXP_COUNT . Top 3 Causes 1. Reversed Character Range The most common cause is simply specifying the range in descending order instead of ascending. -- ERROR: reversed range SELECT * FROM empl…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/dbmserror/oracle-ora-12728-error-causes-and-solutions-complete-guide-b6l

## Related notes
- [[2026-09-16-oracle-ora-12722-error-causes-and-solutions-complete-guide]]
- [[2026-09-17-oracle-ora-12723-error-causes-and-solutions-complete-guide]]
- [[2026-06-16-oracle-ora-00909-error-causes-and-solutions-complete-guide]]
- [[2026-07-11-postgresql-42710-error-causes-and-solutions-complete-guide]]
- [[2026-06-25-oracle-ora-01001-error-causes-and-solutions-complete-guide]]
- [[2026-06-23-oracle-ora-00964-error-causes-and-solutions-complete-guide]]
