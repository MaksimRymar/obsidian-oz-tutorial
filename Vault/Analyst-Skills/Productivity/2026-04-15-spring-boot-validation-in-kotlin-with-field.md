---
title: Spring Boot Validation in Kotlin with @field
date: '2026-04-15'
source: https://dev.to/focused_dot_io/spring-boot-validation-in-kotlin-with-field-4gon
domain: Productivity
relevance: 🟡
tags:
- '#productivity'
- '#python'
- '#tool'
- '#tutorial'
related:
- '[[2026-03-02-python-asyncio-for-web-scraping-speed-up-10x]]'
- '[[2026-03-13-building-a-music-practice-app-with-ai-stem-separation-python-react]]'
- '[[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]'
- '[[2026-04-11-why-vibe-coding-your-data-warehouse-is-a-terrible-idea]]'
- '[[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]'
- '[[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]'
status: unread
---

> **TL;DR:** Recently I found myself needing to validate fields in a Spring Boot controller written in Kotlin. Here's the code I ended up with: @Controller @RequestMapping ( " api/sample " ) class SampleController { @PostMapping fun…

## What’s new and why it matters
Recently I found myself needing to validate fields in a Spring Boot controller written in Kotlin. Here's the code I ended up with: @Controller @RequestMapping ( " api/sample " ) class SampleController { @PostMapping fun post ( @Valid @RequestBody request : SampleType ){ return ResponseEntity . ok (). build () } } data class SampleType ( @field : NotBlank info : String ) The key is the @field in the data class. Without that, Kotlin will apply validation to the constructor parameters by default. This makes sense when you see it, but is less obvious when you're wading through your 10th Java based…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/focused_dot_io/spring-boot-validation-in-kotlin-with-field-4gon

## Related notes
- [[2026-03-02-python-asyncio-for-web-scraping-speed-up-10x]]
- [[2026-03-13-building-a-music-practice-app-with-ai-stem-separation-python-react]]
- [[2026-04-13-python-314-free-threading-real-benchmarks-real-breakage-real-code]]
- [[2026-04-11-why-vibe-coding-your-data-warehouse-is-a-terrible-idea]]
- [[2026-02-22-a-beginners-guide-to-making-data-web-applications-using-python-with-streamlit]]
- [[2026-04-11-i-trusted-the-code-ai-wrote-for-me-my-data-was-silently-broken-the-whole-time]]
