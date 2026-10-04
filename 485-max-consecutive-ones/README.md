# 485. Max Consecutive Ones

## Problem

Given a binary array `nums`, return *the maximum number of consecutive `1`'s in the array*.

## Approach

Scan the array while tracking the length of the current run of `1`s. Reset the count to `0` whenever a `0` is encountered, and update the maximum after each element.

## Complexity

Let **n** be the length of `nums`.

**Time complexity:** $O(n)$<br>
Each element is processed once.

**Space complexity:** $O(1)$<br>
Only the current and maximum run lengths are stored.

## Solution
[View solution](./solution.py)
