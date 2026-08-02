---
title: Workday's job API tells you there are 2,000 jobs, then says 0 on page two
date: '2026-08-02'
source: https://dev.to/glitchbound/workdays-job-api-tells-you-there-are-2000-jobs-then-says-0-on-page-two-2c8e
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]'
- '[[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]'
- '[[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]'
- '[[2026-07-24-alpha-to-beta-bringing-in-qa]]'
- '[[2026-07-25-rest-style-graphql-one-line-of-java-handles-filtering-sorting-pagination-stats-csv-export]]'
status: unread
---

> **TL;DR:** Workday is where large enterprises actually post. NVIDIA has 2,000 open roles there, Salesforce 1,477, Adobe 832. It answers an anonymous POST with no key. It also has two behaviours that are not in any documentation you…

## What’s new and why it matters
Workday is where large enterprises actually post. NVIDIA has 2,000 open roles there, Salesforce 1,477, Adobe 832. It answers an anonymous POST with no key. It also has two behaviours that are not in any documentation you can read without an account, and both of them fail silently. One of them costs you 98% of the board without raising anything. The number that changes after page one Ask for the first twenty postings and the response carries a total : POST /wday/cxs/nvidia/NVIDIAExternalCareerSite/jobs {"appliedFacets":{}, "limit":20, "offset":0, "searchText":""} 20 jobPostings, total: 2000 Ask…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/glitchbound/workdays-job-api-tells-you-there-are-2000-jobs-then-says-0-on-page-two-2c8e

## Related notes
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-06-15-day-01-of-learning-data-engineering-step1-sql-joins-and-set-operators]]
- [[2026-07-27-i-tested-42-large-employers-to-see-which-ones-you-can-actually-scrape-only-7-worked]]
- [[2026-08-01-my-mcp-servers-two-api-helpers-had-zero-except-blocks-every-bad-call-crashed-with-a-raw-urllib-traceback]]
- [[2026-07-24-alpha-to-beta-bringing-in-qa]]
- [[2026-07-25-rest-style-graphql-one-line-of-java-handles-filtering-sorting-pagination-stats-csv-export]]
