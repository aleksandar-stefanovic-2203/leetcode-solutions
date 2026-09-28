# 1614. Maximum Nesting Depth of the Parentheses

## Problem

Given a **valid parentheses string** `s`, return the **nesting depth** of `s`. The nesting depth is the **maximum** number of nested parentheses.

## Approach

Scan the string once while tracking the current nesting depth. Whenever an opening parenthesis increases the depth, update the maximum depth if the current value is larger. Closing parentheses decrease the current depth.

## Algorithm

1. Initialize the current depth and maximum depth to `0`.
2. Iterate through each character in `s`.
3. If the character is `(`, increment the current depth and update the maximum depth.
4. If the character is `)`, decrement the current depth.
5. Return the maximum depth.

## Complexity

Let **n** be the length of `s`.

**Time complexity:** $O(n)$<br>
Each character is processed once.

**Space complexity:** $O(1)$<br>
Only the current and maximum depths are stored.

## Solution
[View solution](./solution.py)
