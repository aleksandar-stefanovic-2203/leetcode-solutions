# 32. Longest Valid Parentheses

## Problem

Given a string containing just the characters `'('` and `')'`, return *the length of the longest valid (well-formed) parentheses substring*.

## 1. Stack-based solution

### Approach

Store indices of unmatched opening parentheses. The initial `-1` acts as a boundary before the string. When a closing parenthesis matches an opening one, the current valid substring length is the distance from the latest unmatched boundary. If no opening index remains, the current closing index becomes the new boundary.

### Algorithm

1. Initialize the stack with `-1` and the maximum length with zero.
2. Push the index of each opening parenthesis.
3. For each closing parenthesis, pop the stack. If it is empty, push the current index as the new boundary; otherwise, update the maximum length using the distance to the top index.
4. Return the maximum length.

### Complexity

**Time complexity:** $O(n)$<br>
Each character is processed once.

**Space complexity:** $O(n)$<br>
The stack can contain indices for all opening parentheses.

### Solution

[View solution](./solution-stack-based.py)

## 2. Two-pass counter solution

### Approach

Count opening and closing parentheses from left to right, resetting when closing parentheses outnumber opening ones. This finds valid substrings that are not short of closing parentheses. A right-to-left pass resets when opening parentheses outnumber closing ones, covering the complementary case.

### Algorithm

1. Scan left to right, incrementing the relevant counter.
2. When the counters are equal, update the maximum length. When closing parentheses outnumber opening ones, reset both counters.
3. Reset both counters and scan right to left.
4. When the counters are equal, update the maximum length. When opening parentheses outnumber closing ones, reset both counters.
5. Return the maximum length.

### Complexity

**Time complexity:** $O(n)$<br>
The string is scanned twice.

**Space complexity:** $O(1)$<br>
Only a fixed number of counters are used.

### Solution

[View solution](./solution-two-pass-counters.py)

## Comparison

Both approaches run in $O(n)$ time. The stack approach is a direct way to track unmatched boundaries, while the two-pass counter approach uses constant extra space. The two-pass approach is preferable when minimizing auxiliary space matters.