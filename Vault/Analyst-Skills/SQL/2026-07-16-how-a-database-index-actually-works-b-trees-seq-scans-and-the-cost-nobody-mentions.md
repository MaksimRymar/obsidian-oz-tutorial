---
title: 'How a Database Index Actually Works: B-Trees, Seq Scans, and the Cost Nobody
  Mentions'
date: '2026-07-16'
source: https://dev.to/vahid_aghajani_60ce9dbec9/how-a-database-index-actually-works-b-trees-seq-scans-and-the-cost-nobody-mentions-528j
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]'
status: unread
---

> **TL;DR:** 📺 Prefer to watch? 90-second YouTube Short · 💬 Telegram Originally published on software-engineer-blog.com . The same query. 4.2 seconds , then 3 milliseconds . Same data, same machine, same SQL. The only thing that chan…

## What’s new and why it matters
📺 Prefer to watch? 90-second YouTube Short · 💬 Telegram Originally published on software-engineer-blog.com . The same query. 4.2 seconds , then 3 milliseconds . Same data, same machine, same SQL. The only thing that changed was one line: CREATE INDEX idx_customers_email ON customers ( email ); Most explanations of indexing start at "it's like the index in a book" — and then stop. That analogy is fine as far as it goes, but it skips the part that actually matters: why the database is slow without one, and what it costs you to add one. So let's start a level below the index. Throughout, one runn…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/vahid_aghajani_60ce9dbec9/how-a-database-index-actually-works-b-trees-seq-scans-and-the-cost-nobody-mentions-528j

## Related notes
- [[2026-06-29-how-database-indexes-actually-work-and-when-they-backfire]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-07-06-your-postgres-already-knows-why-its-slow-you-just-have-to-ask-it]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-04-15-how-to-build-a-strong-foundation-in-sql-and-databases-step-by-step]]
