# 20. Valid Parentheses

## Problem

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Stack approach

### Approach

Use a stack to remember opening brackets. For every closing bracket, compare it with the most recent unmatched opening bracket. If the stack is empty or they do not match, the string is invalid; otherwise remove the opening bracket. Any opening brackets remaining at the end are unmatched.

### Algorithm

1. Create an empty stack and a mapping from each closing bracket to its corresponding opening bracket.
2. Iterate through the characters in `s`.
3. Push opening brackets onto the stack.
4. For a closing bracket, return `False` if the stack is empty or its top does not match. Otherwise, pop the matching opening bracket.
5. Return `True` only if the stack is empty after processing the string.

### Complexity

**Time complexity:** $O(n)$<br>
Each character is processed once, with constant-time stack and dictionary operations.

**Space complexity:** $O(n)$<br>
In the worst case, the stack holds all opening brackets.

### Solution

[View solution](./solution-stack.py)
