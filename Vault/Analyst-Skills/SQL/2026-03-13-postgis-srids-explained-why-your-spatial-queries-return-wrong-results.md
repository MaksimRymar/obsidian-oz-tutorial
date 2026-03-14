---
title: 'PostGIS SRIDs Explained: Why Your Spatial Queries Return Wrong Results'
date: '2026-03-13'
source: https://dev.to/philip_mcclarence_2ef9475/postgis-srids-explained-why-your-spatial-queries-return-wrong-results-3lcc
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#sql'
- '#tool'
related:
- '[[2026-03-09-postgis-geometry-quality-invalid-geometries-mixed-srids-and-complexity]]'
- '[[2026-03-12-postgis-spatial-indexing-why-your-queries-are-doing-sequential-scans]]'
- '[[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]'
- '[[2026-03-01-joins-and-windows-functions-in-sql]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-03-01-pgvector-distance-functions-cosine-vs-l2-vs-inner-product]]'
status: unread
---

> **TL;DR:** PostGIS SRIDs Explained: Why Your Spatial Queries Return Wrong Results Every geometry in PostGIS carries an SRID -- a Spatial Reference Identifier that defines its coordinate system. SRID 4326 is WGS 84 (GPS coordinates…

## What’s new and why it matters
PostGIS SRIDs Explained: Why Your Spatial Queries Return Wrong Results Every geometry in PostGIS carries an SRID -- a Spatial Reference Identifier that defines its coordinate system. SRID 4326 is WGS 84 (GPS coordinates in degrees). SRID 3857 is Web Mercator (the projection behind Google Maps tiles). SRID 326xx is a UTM zone (meters, accurate within a narrow longitude band). Get the SRID wrong and every spatial function -- distance, area, intersection, containment -- returns a number that looks plausible but is incorrect. The insidious part is that PostGIS never raises an error. It computes wh…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/philip_mcclarence_2ef9475/postgis-srids-explained-why-your-spatial-queries-return-wrong-results-3lcc

## Related notes
- [[2026-03-09-postgis-geometry-quality-invalid-geometries-mixed-srids-and-complexity]]
- [[2026-03-12-postgis-spatial-indexing-why-your-queries-are-doing-sequential-scans]]
- [[2026-03-03-sql-joins-window-functions-the-skills-that-separate-analysts-from-beginners]]
- [[2026-03-01-joins-and-windows-functions-in-sql]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-03-01-pgvector-distance-functions-cosine-vs-l2-vs-inner-product]]
