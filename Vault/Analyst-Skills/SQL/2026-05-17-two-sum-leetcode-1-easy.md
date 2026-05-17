---
title: 'Two Sum — LeetCode #1 (Easy)'
date: '2026-05-17'
source: https://dev.to/logixydev/two-sum-leetcode-1-easy-4fop
domain: SQL
relevance: 🟡
tags:
- '#ai'
- '#best-practice'
- '#career'
- '#python'
- '#sql'
- '#tool'
- '#zendesk'
related:
- '[[2026-03-20-search-in-rotated-sorted-array-using-binary-search]]'
- '[[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]'
- '[[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]'
- '[[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]'
- '[[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]'
- '[[2026-03-15-count-commas-in-range---leetcode-3870-solution]]'
status: unread
---

> **TL;DR:** TL;DR Single-pass hash map lookup: store each number's index as you go, check for the complement before storing. O(n) time, O(n) space. The Problem Given an array of integers nums and an integer target , return the indic…

## What’s new and why it matters
TL;DR Single-pass hash map lookup: store each number's index as you go, check for the complement before storing. O(n) time, O(n) space. The Problem Given an array of integers nums and an integer target , return the indices of the two numbers that add up to target . Input: nums = [2,7,11,15], target = 9 Output: [0,1] The answer is indices 0 and 1 because nums[0] + nums[1] == 9 . Note: return indices, not values. Constraints 2 <= nums.length <= 10^4 -10^9 <= nums[i] <= 10^9 -10^9 <= target <= 10^9 Exactly one valid answer exists. Naive Approach Fix one number, scan every number after it for the…

## How to apply
- Extract 1 actionable tactic from this post and try it on a real dataset this week.
- Write the query in a scratchpad and run EXPLAIN/QUERY PLAN to verify performance.
- Add a short note: what changed in your workflow?

## Relevance
🟡

## Source
https://dev.to/logixydev/two-sum-leetcode-1-easy-4fop

## Related notes
- [[2026-03-20-search-in-rotated-sorted-array-using-binary-search]]
- [[2026-03-30-database-indexing-explained-whats-actually-happening-under-the-hood]]
- [[2026-03-02-your-ai-forgot-everything-you-told-it-yesterday-mine-didnt]]
- [[2026-03-24-two-hospitals-matched-patient-records-without-sharing-a-single-name]]
- [[2026-04-22-i-priced-18-million-spy-put-spreads-across-8-years-every-bucket-was--ev-every-year-made-money]]
- [[2026-03-15-count-commas-in-range---leetcode-3870-solution]]
