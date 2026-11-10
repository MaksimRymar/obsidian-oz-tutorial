---
title: Extract Email Domains Using INSTR() and SUBSTR() in Oracle SQL
date: '2026-11-10'
source: https://dev.to/kailas_warade_d2a15d1ef8a/extract-email-domains-using-instr-and-substr-in-oracle-sql-e0o
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]'
- '[[2026-09-11-sql-subqueries-ctes-write-smarter-cleaner-queries]]'
- '[[2026-11-02-sql-challenge-can-you-find-employees-earning-more-than-their-departments-average-salary]]'
- '[[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]'
- '[[2026-11-02-sql-join-example-how-to-get-employee-names-along-with-department-names]]'
- '[[2026-05-20-learning-sql-as-if-you-built-it-yourself]]'
status: unread
---

> **TL;DR:** SQL Challenge #98: How to Extract an Email Domain Using INSTR() and SUBSTR() in Oracle SQL Sometimes, while working with employee or customer records, you may need to get the domain name separately from an email address.…

## What’s new and why it matters
SQL Challenge #98: How to Extract an Email Domain Using INSTR() and SUBSTR() in Oracle SQL Sometimes, while working with employee or customer records, you may need to get the domain name separately from an email address. For example: kailas@gmail.com → gmail.com rahul@yahoo.com → yahoo.com Let's see how to do this using two simple Oracle SQL functions. The Problem You have an "employees" table containing email addresses. You need to write a query that extracts everything after the "@" symbol and displays it in a separate column. Input: employees emp_id email 101 kailas@gmail.com 102 rahul@yaho…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/kailas_warade_d2a15d1ef8a/extract-email-domains-using-instr-and-substr-in-oracle-sql-e0o

## Related notes
- [[2026-10-28-sql-select-statement-practical-examples-for-interview-preparation]]
- [[2026-09-11-sql-subqueries-ctes-write-smarter-cleaner-queries]]
- [[2026-11-02-sql-challenge-can-you-find-employees-earning-more-than-their-departments-average-salary]]
- [[2026-10-29-5-common-sql-mistakes-where-order-by-andor-and-top-3-queries]]
- [[2026-11-02-sql-join-example-how-to-get-employee-names-along-with-department-names]]
- [[2026-05-20-learning-sql-as-if-you-built-it-yourself]]
