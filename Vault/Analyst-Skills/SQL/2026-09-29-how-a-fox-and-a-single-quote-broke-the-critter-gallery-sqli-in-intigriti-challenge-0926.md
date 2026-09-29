---
title: How a Fox and a Single Quote Broke the Critter Gallery — SQLi in Intigriti
  Challenge 0926
date: '2026-09-29'
source: https://dev.to/duchuaz/how-a-fox-and-a-single-quote-broke-the-critter-gallery-sqli-in-intigriti-challenge-0926-4fhm
domain: SQL
relevance: 🔴
tags:
- '#sql'
- '#support-analytics'
- '#tool'
related:
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-09-16-sql-joins-with-examples-of-each]]'
- '[[2026-08-04-sqlazymerge-multiple-tables-into-single-rows-by-common-id]]'
- '[[2026-07-28-why-schema-drift-goes-undetected]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-08-10-why-senior-data-engineers-write-sql-differently]]'
status: unread
---

> **TL;DR:** How a Fox and a Single Quote Broke the Critter Gallery — SQLi in Intigriti Challenge 0926 My write-up for Intigriti Challenge 0926 : a cute animal gallery hiding a textbook SQL injection behind a base64 ?pic= parameter.…

## What’s new and why it matters
How a Fox and a Single Quote Broke the Critter Gallery — SQLi in Intigriti Challenge 0926 My write-up for Intigriti Challenge 0926 : a cute animal gallery hiding a textbook SQL injection behind a base64 ?pic= parameter. Solved 27/09/2026, submission INTIGRITI-TAPV7AA2 accepted. The challenge The Critter Gallery shows one animal per page. The animal is picked via a base64-encoded ?pic= query parameter that decodes to the critter's name, e.g. ?pic=Rk9Y → FOX . Beneath each picture sits a short description pulled from a database. Somewhere on the server, a second table — secret_vault — holds the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/duchuaz/how-a-fox-and-a-single-quote-broke-the-critter-gallery-sqli-in-intigriti-challenge-0926-4fhm

## Related notes
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-09-16-sql-joins-with-examples-of-each]]
- [[2026-08-04-sqlazymerge-multiple-tables-into-single-rows-by-common-id]]
- [[2026-07-28-why-schema-drift-goes-undetected]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-08-10-why-senior-data-engineers-write-sql-differently]]
