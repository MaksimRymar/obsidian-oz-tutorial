---
title: Comment supprimer les silences d'un enregistrement en Python sans couper les
  mots
date: '2026-11-07'
source: https://dev.to/bestaitools-fr/comment-supprimer-les-silences-dun-enregistrement-en-python-sans-couper-les-mots-2lid
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#feature'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-10-31-sql-dbutant-le-cours-pas-pas-et-12-exercices-corrigs]]'
- '[[2026-11-05-comment-rechercher-dans-google-patents-depuis-python-sans-cl-dapi]]'
- '[[2026-07-10-apprendre-sql-la-mthode-par-la-pratique-2026]]'
- '[[2026-08-21-on-ne-devrait-pas-avoir-croire-un-cv-sur-parole]]'
- '[[2026-06-22-du-tableau-html-aux-instructions-sql-insert-en-un-clic]]'
- '[[2026-07-20-du-navigateur-la-base-de-donnes-le-chemin-le-plus-court-pour-les-tableaux-web]]'
status: unread
---

> **TL;DR:** Retirer les pauses d'un enregistrement vocal se résume à quatre nombres : un niveau en dessous duquel l'audio est considéré comme silencieux, la durée minimale d'un passage calme avant qu'on le supprime, et la marge à ga…

## What’s new and why it matters
Retirer les pauses d'un enregistrement vocal se résume à quatre nombres : un niveau en dessous duquel l'audio est considéré comme silencieux, la durée minimale d'un passage calme avant qu'on le supprime, et la marge à garder de chaque côté des morceaux conservés. Le Sound Editor de l'application de bureau osFoundry expose exactement ces quatre réglages dans sa boîte de dialogue Strip Silence, avec comme valeurs par défaut −48 dB, 50 ms, 5 ms et 20 ms. Ci-dessous, la même opération est reconstruite en une quarantaine de lignes de numpy, vérifiée échantillon par échantillon contre un fichier exp…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/bestaitools-fr/comment-supprimer-les-silences-dun-enregistrement-en-python-sans-couper-les-mots-2lid

## Related notes
- [[2026-10-31-sql-dbutant-le-cours-pas-pas-et-12-exercices-corrigs]]
- [[2026-11-05-comment-rechercher-dans-google-patents-depuis-python-sans-cl-dapi]]
- [[2026-07-10-apprendre-sql-la-mthode-par-la-pratique-2026]]
- [[2026-08-21-on-ne-devrait-pas-avoir-croire-un-cv-sur-parole]]
- [[2026-06-22-du-tableau-html-aux-instructions-sql-insert-en-un-clic]]
- [[2026-07-20-du-navigateur-la-base-de-donnes-le-chemin-le-plus-court-pour-les-tableaux-web]]
