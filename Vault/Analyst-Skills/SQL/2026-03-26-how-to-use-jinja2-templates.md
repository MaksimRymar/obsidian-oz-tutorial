---
title: How to use Jinja2 Templates
date: '2026-03-26'
source: https://dev.to/brandon_woondc/how-to-use-jinja2-templates-2io2
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#sql'
- '#support-analytics'
- '#tool'
- '#tutorial'
related:
- '[[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]'
- '[[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]'
- '[[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]'
- '[[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]'
- '[[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]'
- '[[2026-02-24-stop-using-any-the-wrong-way-in-rails]]'
status: unread
---

> **TL;DR:** The base template acts as the foundation of the entire website using Jinja2’s template inheritance system. Instead of repeating common elements like the navigation bar, footer, fonts, and global styles across every page,…

## What’s new and why it matters
The base template acts as the foundation of the entire website using Jinja2’s template inheritance system. Instead of repeating common elements like the navigation bar, footer, fonts, and global styles across every page, they are defined once in base.html. Other pages use extends <!DOCTYPE html> <html lang= "en" > <head> <meta charset= "UTF-8" /> <meta name= "viewport" content= "width=device-width, initial-scale=1.0" /> <title> {% block title %}Local Hub{% endblock %} </title> <link href= "https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=Nunito:wght@400;600;700&…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/brandon_woondc/how-to-use-jinja2-templates-2io2

## Related notes
- [[2026-02-28-clustered-vs-non-clustered-index-in-sqlcomplete-guide-with-examples]]
- [[2026-02-28-database-indexing-made-easy-sql-vs-mongodb]]
- [[2026-03-10-pdf-ocr-extract-text-from-scanned-pdfs-with-an-api]]
- [[2026-03-15-sql-joins-and-window-functions-the-tools-that-changed-how-i-query-data]]
- [[2026-03-13-you-dont-need-a-framework-building-reliable-ai-agents-from-first-principles]]
- [[2026-02-24-stop-using-any-the-wrong-way-in-rails]]
