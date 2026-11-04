---
title: Deadlocks γιατί εμφανίζονται και πώς τα μειώνουμε
date: '2026-11-04'
source: https://dev.to/__b63657/deadlocks-giati-emphanizontai-kai-pos-ta-meionoume-1om7
domain: SQL
relevance: 🟡
tags:
- '#sql'
- '#tutorial'
related:
- '[[2026-10-31-how-to-fix-sql-server-deadlocks-causes-detection-and-real-fixes]]'
- '[[2026-03-20-sql-triggers-for-blocking]]'
- '[[2026-08-29-postgresql-25p01-error-causes-and-solutions-complete-guide]]'
- '[[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]'
- '[[2026-04-07-database-transactions-acid-properties-in-plain-english]]'
- '[[2026-08-08-postgresql-22012-error-causes-and-solutions-complete-guide]]'
status: unread
---

> **TL;DR:** Μια συναλλαγή μπορεί να προστατεύει προσωρινά δεδομένα από ασύμβατες ενέργειες άλλων συναλλαγών. Αυτή η προστασία ονομάζεται κλείδωμα — lock . Αν μια άλλη εργασία χρειάζεται τα ίδια δεδομένα, μπορεί να περιμένει. Αναμονή…

## What’s new and why it matters
Μια συναλλαγή μπορεί να προστατεύει προσωρινά δεδομένα από ασύμβατες ενέργειες άλλων συναλλαγών. Αυτή η προστασία ονομάζεται κλείδωμα — lock . Αν μια άλλη εργασία χρειάζεται τα ίδια δεδομένα, μπορεί να περιμένει. Αναμονή και deadlock Η απλή αναμονή μπορεί να εξελιχθεί φυσιολογικά: Η A κρατά μια γραμμή. Η B περιμένει. Η A ολοκληρώνεται. Η B συνεχίζει. Αυτό λέγεται blocking . Σε ένα deadlock , η αναμονή γίνεται κύκλος: Η A κρατά τη γραμμή 1 και περιμένει τη γραμμή 2. Η B κρατά τη γραμμή 2 και περιμένει τη γραμμή 1. Καμία δεν μπορεί να συνεχίσει χωρίς παρέμβαση. Ο SQL Server επιλέγει μια συναλλαγ…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/__b63657/deadlocks-giati-emphanizontai-kai-pos-ta-meionoume-1om7

## Related notes
- [[2026-10-31-how-to-fix-sql-server-deadlocks-causes-detection-and-real-fixes]]
- [[2026-03-20-sql-triggers-for-blocking]]
- [[2026-08-29-postgresql-25p01-error-causes-and-solutions-complete-guide]]
- [[2026-05-03-claudemd-for-postgresql-13-rules-that-make-ai-write-safe-production-ready-sql]]
- [[2026-04-07-database-transactions-acid-properties-in-plain-english]]
- [[2026-08-08-postgresql-22012-error-causes-and-solutions-complete-guide]]
