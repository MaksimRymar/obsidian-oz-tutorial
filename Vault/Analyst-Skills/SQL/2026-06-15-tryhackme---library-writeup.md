---
title: TryHackme - Library Writeup
date: '2026-06-15'
source: https://dev.to/exploitnotes/tryhackme-library-writeup-5alb
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#library'
- '#python'
- '#sql'
- '#tool'
related:
- '[[2026-05-30-mp3---sqli-xss-and-csrf-writeup]]'
- '[[2026-05-18-top-orm-tools-practical-comparison]]'
- '[[2026-05-28-how-i-added-dbt-cloud-to-coral-my-open-source-hackathon-journey]]'
- '[[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]'
- '[[2026-04-17-postgresql-vs-mysql-which-is-better-for-your-application]]'
- '[[2026-03-28-from-pixels-to-payload-lsb-steganography-and-in-memory-execution]]'
status: unread
---

> **TL;DR:** Platform: TryHackMe Difficulty: Easy OS: Linux Reconnaissance Nmap nmap -sC -sV -A MACHINE_IP -oA nmap Open ports: 22/tcp — OpenSSH 7.2p2 (Ubuntu) 80/tcp — Apache 2.4.18, title: Welcome to Blog - Library Machine Web Enum…

## What’s new and why it matters
Platform: TryHackMe Difficulty: Easy OS: Linux Reconnaissance Nmap nmap -sC -sV -A MACHINE_IP -oA nmap Open ports: 22/tcp — OpenSSH 7.2p2 (Ubuntu) 80/tcp — Apache 2.4.18, title: Welcome to Blog - Library Machine Web Enumeration Visiting port 80 revealed a blog page. The blog post was authored by meliodas — a valid username. The comments section also leaked root and www-data as system usernames. robots.txt contained an unusual entry: User - agent : rockyou Disallow : / This is a hint to use the rockyou.txt wordlist for brute-forcing. Directory brute-forcing with feroxbuster and dirsearch found…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/exploitnotes/tryhackme-library-writeup-5alb

## Related notes
- [[2026-05-30-mp3---sqli-xss-and-csrf-writeup]]
- [[2026-05-18-top-orm-tools-practical-comparison]]
- [[2026-05-28-how-i-added-dbt-cloud-to-coral-my-open-source-hackathon-journey]]
- [[2026-02-26-i-gave-an-open-source-ai-full-access-to-my-linux-terminal-and-lived-to-tell-the-tale]]
- [[2026-04-17-postgresql-vs-mysql-which-is-better-for-your-application]]
- [[2026-03-28-from-pixels-to-payload-lsb-steganography-and-in-memory-execution]]
