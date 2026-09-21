---
title: I ran a contract check against the Swagger Petstore. Here is what came back.
date: '2026-09-21'
source: https://dev.to/b6bs62fhysjpg/i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back-24me
domain: Productivity
relevance: 🟡
tags:
- '#best-practice'
- '#productivity'
- '#tool'
related:
- '[[2026-09-06-checking-if-a-businesss-google-profile-actually-matches-its-own-website]]'
- '[[2026-09-05-a-domain-that-doesnt-exist-returns-http-200-ok]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]'
- '[[2026-09-09-six-tables-out-of-260]]'
- '[[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]'
status: unread
---

> **TL;DR:** Most API bugs I care about are not crashes. They are small lies between the spec and the live API. A field that went missing. A status code nobody documented. A body that is not what the spec says it is. I built SpecSent…

## What’s new and why it matters
Most API bugs I care about are not crashes. They are small lies between the spec and the live API. A field that went missing. A status code nobody documented. A body that is not what the spec says it is. I built SpecSentinel to catch those. It is a small command line tool. You give it an OpenAPI spec and the address of a running API. It sends GET requests, compares every answer with the spec and ends with an exit code: 0 for a match, 1 for drift, 2 if the check could not be done. That makes it easy to use as a step in CI. To see what it does on something real, I pointed it at the public Swagge…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/b6bs62fhysjpg/i-ran-a-contract-check-against-the-swagger-petstore-here-is-what-came-back-24me

## Related notes
- [[2026-09-06-checking-if-a-businesss-google-profile-actually-matches-its-own-website]]
- [[2026-09-05-a-domain-that-doesnt-exist-returns-http-200-ok]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-19-python-quickstart-nutrition-data-in-10-lines]]
- [[2026-09-09-six-tables-out-of-260]]
- [[2026-08-17-before-you-trust-minimax-h3-run-this-free-baseline-harness]]
