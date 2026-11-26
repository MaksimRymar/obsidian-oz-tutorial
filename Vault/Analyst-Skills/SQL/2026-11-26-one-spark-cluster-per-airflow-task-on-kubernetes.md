---
title: One Spark cluster per Airflow task on Kubernetes
date: '2026-11-26'
source: https://itnext.io/one-spark-cluster-per-airflow-task-on-kubernetes-afdc7acf4fb7?source=rss------python-5
domain: SQL
relevance: 🟡
tags:
- '#python'
- '#sql'
related:
- '[[2026-09-27-spark-partitioning-rdd-groupby-vs-window-partitioning-subset-and-coalesce-in-spark-cte-with]]'
- '[[2026-08-30-celery-had-40-idle-workers-one-long-task-still-delayed-every-payment]]'
- '[[2026-11-25-in-rag-context-engineering-starts-with-the-question]]'
- '[[2026-06-06-duckdb-loutil-le-plus-sous-estim-pour-les-data-analysts-en-2026]]'
- '[[2026-10-16-pandas-is-the-python-skill-that-makes-messy-data-useful]]'
- '[[2026-08-19-streamlit-option-menu-the-navigation-bar-that-makes-people-ask-what-frontend-framework-you-used]]'
status: unread
---

> **TL;DR:** pysparkonk8s makes the KubernetesExecutor worker pod a client-mode Spark driver and starts the task’s executors next to it, sized from… Continue reading on ITNEXT »

## What’s new and why it matters
pysparkonk8s makes the KubernetesExecutor worker pod a client-mode Spark driver and starts the task’s executors next to it, sized from… Continue reading on ITNEXT »

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://itnext.io/one-spark-cluster-per-airflow-task-on-kubernetes-afdc7acf4fb7?source=rss------python-5

## Related notes
- [[2026-09-27-spark-partitioning-rdd-groupby-vs-window-partitioning-subset-and-coalesce-in-spark-cte-with]]
- [[2026-08-30-celery-had-40-idle-workers-one-long-task-still-delayed-every-payment]]
- [[2026-11-25-in-rag-context-engineering-starts-with-the-question]]
- [[2026-06-06-duckdb-loutil-le-plus-sous-estim-pour-les-data-analysts-en-2026]]
- [[2026-10-16-pandas-is-the-python-skill-that-makes-messy-data-useful]]
- [[2026-08-19-streamlit-option-menu-the-navigation-bar-that-makes-people-ask-what-frontend-framework-you-used]]
