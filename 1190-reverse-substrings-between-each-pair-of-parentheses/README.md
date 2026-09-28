# 1190. Reverse Substrings Between Each Pair of Parentheses

## Problem

You are given a string `s` that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should **not** contain any brackets.

## 1. Recursive approach

### Approach

Recursively evaluate each parenthesized group. A scan tracks the current nesting depth to find a group's matching closing parenthesis. The recursive call evaluates that group's contents, then reverses them before returning to the enclosing expression.

### Algorithm

1. Call a helper on the full string with reversal disabled.
2. Scan the helper's range, tracking the start and nesting depth of each parenthesized group.
3. When a matching closing parenthesis is reached, recursively evaluate the group's contents with reversal enabled and append the returned characters.
4. Append characters that are outside any group directly to the current result.
5. Reverse the current result when the helper was called with reversal enabled.
6. Join the outer call's result and return it.

### Complexity

Let **n** be the length of `s`.

**Time complexity:** $O(n^2)$ in the worst case.<br>
Deeply nested groups cause repeated scans of nested ranges, and each recursive level may reverse its result.

**Space complexity:** $O(n)$<br>
The recursion stack and intermediate result lists require linear space in total.

### Solution
[View solution](./solution-recursive.py)

## 2. Index-based iterative approach

### Approach

Build the result from left to right. When an opening parenthesis is found, save the current result length. When its closing parenthesis is found, reverse the portion of the result added since that saved position. A stack handles nested pairs in last-in, first-out order.

### Algorithm

1. Initialize an empty result list and a stack of result positions.
2. For each character in `s`:
	- On `(`, push the current result length onto the stack.
	- On `)`, pop the saved position and reverse the result suffix starting there.
	- Otherwise, append the character to the result.
3. Join the result list into a string and return it.

### Complexity

Let **n** be the length of `s`.

**Time complexity:** $O(n^2)$ in the worst case.<br>
Each character is processed once, but reversing result suffixes can repeatedly touch the same characters for nested parentheses.

**Space complexity:** $O(n)$<br>
The result and the stack of opening-parenthesis positions each use at most linear space.

### Solution
[View solution](./solution-index-based-iterative.py)

## 3. Wormhole-jump approach

### Approach

First pair each opening and closing parenthesis by index. Then walk the string with a direction that can be forward or backward. Whenever a parenthesis is encountered, jump to its matching partner and flip direction. This simulates reversing each enclosed substring without explicitly reversing it.

### Algorithm

1. Scan `s` with a stack of opening-parenthesis indices.
2. On `(`, push its index. On `)`, pop its matching opening index and record both directions in a pair array.
3. Start at the beginning of the string, moving forward.
4. When a parenthesis is encountered, jump to its matching index and reverse the direction of travel.
5. Otherwise, append the current character, then advance by the current direction.
6. Join the collected characters and return them.

### Complexity

Let **n** be the length of `s`.

**Time complexity:** $O(n)$<br>
Pairing parentheses and traversing the string each take linear time.

**Space complexity:** $O(n)$<br>
The matching-index array, stack, and output use linear space.

### Solution
[View solution](./solution-wormhole.py)

## Complexity comparison

| Approach | Time complexity | Space complexity |
| --- | --- | --- |
| Recursive | $O(n^2)$ | $O(n)$ |
| Index-based iterative | $O(n^2)$ | $O(n)$ |
| Wormhole-jump | $O(n)$ | $O(n)$ |
