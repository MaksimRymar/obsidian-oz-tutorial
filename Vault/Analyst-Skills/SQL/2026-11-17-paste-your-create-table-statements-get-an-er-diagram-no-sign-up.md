---
title: Paste your CREATE TABLE statements, get an ER diagram (no sign-up)
date: '2026-11-17'
source: https://dev.to/deekeej/paste-your-create-table-statements-get-an-er-diagram-no-sign-up-2gcj
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tool'
related:
- '[[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]'
- '[[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]'
- '[[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]'
- '[[2026-11-04-reading-medium-articles-by-tag-author-and-publication-with-rss-and-where-it-stops]]'
- '[[2026-07-25-rest-style-graphql-one-line-of-java-handles-filtering-sorting-pagination-stats-csv-export]]'
- '[[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]'
status: unread
---

> **TL;DR:** You already have your schema as SQL. Drawing it again by hand, box by box, is the part nobody enjoys. Here is a way to skip it: paste the CREATE TABLE statements and let the diagram draw itself. I'm the maker of Systemap…

## What’s new and why it matters
You already have your schema as SQL. Drawing it again by hand, box by box, is the part nobody enjoys. Here is a way to skip it: paste the CREATE TABLE statements and let the diagram draw itself. I'm the maker of Systemap, a diagram editor that runs in the browser. This post walks through its SQL import. You can follow along without an account. The schema A small issue tracker: users, projects, issues and comments. CREATE TABLE users ( id uuid PRIMARY KEY , name text NOT NULL , email text NOT NULL UNIQUE ) ; CREATE TABLE projects ( id uuid PRIMARY KEY , name text NOT NULL ) ; CREATE TABLE issue…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/deekeej/paste-your-create-table-statements-get-an-er-diagram-no-sign-up-2gcj

## Related notes
- [[2026-10-05-how-to-get-a-transcript-of-any-spotify-podcast-episode-3-ways-with-and-without-code]]
- [[2026-06-28-how-to-generate-a-sql-schema-from-a-csv-file-without-hand-writing-every-column-type]]
- [[2026-05-08-prisma-relationships-finally-explained-with-mysql-side-by-side]]
- [[2026-11-04-reading-medium-articles-by-tag-author-and-publication-with-rss-and-where-it-stops]]
- [[2026-07-25-rest-style-graphql-one-line-of-java-handles-filtering-sorting-pagination-stats-csv-export]]
- [[2026-11-11-setting-up-postgresql-with-docker-psql-and-pgadmin]]
