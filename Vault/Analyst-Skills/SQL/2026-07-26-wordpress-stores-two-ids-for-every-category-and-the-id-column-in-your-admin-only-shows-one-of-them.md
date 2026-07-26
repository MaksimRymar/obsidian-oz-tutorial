---
title: WordPress stores two IDs for every category, and the ID column in your admin
  only shows one of them
date: '2026-07-26'
source: https://dev.to/lucasfenw/wordpress-stores-two-ids-for-every-category-and-the-id-column-in-your-admin-only-shows-one-of-them-42pg
domain: SQL
relevance: 🔴
tags:
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-07-23-btree-height-after-delete-postgresql-fast-root]]'
- '[[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]'
- '[[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]'
- '[[2026-05-01-joins-combining-tables-without-losing-your-mind]]'
status: unread
---

> **TL;DR:** Add an ID column to the WordPress taxonomy list tables by enabling Custom Admin Columns in WP Adminify: go to WP Adminify > Settings > Productivity, scroll to Custom Admin Columns, tick Show "Taxonomy ID" Column for all…

## What’s new and why it matters
Add an ID column to the WordPress taxonomy list tables by enabling Custom Admin Columns in WP Adminify: go to WP Adminify > Settings > Productivity, scroll to Custom Admin Columns, tick Show "Taxonomy ID" Column for all possible types of taxonomies , and save, and an ID column appears after Count on Categories, Tags and every custom taxonomy screen, and the number it prints is the term_id , the same value that sits in each row edit link as term.php?taxonomy=category&tag_ID=3 , which is not the term_taxonomy_id that wp_term_relationships uses to join posts to terms. That is the whole answer. Th…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🔴

## Source
https://dev.to/lucasfenw/wordpress-stores-two-ids-for-every-category-and-the-id-column-in-your-admin-only-shows-one-of-them-42pg

## Related notes
- [[2026-04-22-sql-set-operators-union-intersect-and-except-explained-simply]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-07-23-btree-height-after-delete-postgresql-fast-root]]
- [[2026-07-22-the-backfill-pattern-adding-required-columns-without-downtime]]
- [[2026-04-22-sql-database-architecture-use-cases-and-monitoring-a-practitioners-guide]]
- [[2026-05-01-joins-combining-tables-without-losing-your-mind]]
