# 1111. Maximum Nesting Depth of Two Valid Parentheses Strings

## Problem

A string is a *valid parentheses string* (denoted VPS) if and only if it consists of `"("` and `")"` characters only, and:

- It is the empty string, or
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are VPSs, or
- It can be written as `(A)`, where `A` is a VPS.

We can similarly define the *nesting depth* `depth(S)` of any VPS `S` as follows:

- `depth("") = 0`
- `depth(A + B) = max(depth(A), depth(B))`, where `A` and `B` are VPSs
- `depth("(" + A + ")") = 1 + depth(A)`, where `A` is a VPS

For example, `""`, `"()()"`, and `"()(())"` are VPSs (with nesting depths 0, 1, and 2), and `")("` and `"(()"` are not VPSs.

Given a VPS seq, split it into two disjoint subsequences `A` and `B`, such that `A` and `B` are VPSs (and `A.length + B.length = seq.length`). The subsequences may not necessarily be contiguous.

For example, for the sequence `123456789`, one possible split is:

- `A = {1, 3, 5, 7, 9}`
- `B = {2, 4, 6, 8}`

This corresponds to the output `[0, 1, 0, 1, 0, 1, 0, 1, 0]`, where 0 indicates membership in `A` and 1 indicates membership in `B`.

Now choose **any** such `A` and `B` such that `max(depth(A), depth(B))` is the minimum possible value.

Return an `answer` array (of length `seq.length`) that encodes such a choice of `A` and `B`: `answer[i] = 0` if `seq[i]` is part of `A`, else `answer[i] = 1`. Note that even though multiple answers may exist, you may return any of them.

## 1. Depth parity approach

### Approach

Track the current nesting depth. Assign each opening parenthesis according to its depth after opening, and each closing parenthesis according to its depth before closing. This alternates nested pairs between the two subsequences.

### Algorithm

1. Initialize the current depth to `0`.
2. For each character, if it is `(`, increase the depth and append `depth % 2` to the result.
3. If it is `)`, append `depth % 2` and then decrease the depth.
4. Return the result.

### Complexity

Let **n** be the length of the input string.

**Time complexity:** $O(n)$<br>
Each character is processed once.

**Space complexity:** $O(1)$<br>
Space allocated for variables is constant and isn't dependant on the length of the array.

### Solution

[View solution](./solution-depth-parity.py)

## 2. Index parity approach

### Approach

Assign each character based on its index: opening parentheses use the opposite parity, while closing parentheses use the index parity. In a valid parentheses string, the nesting-depth parity at each position is determined by the character-index parity, so this produces the same assignments as the depth-based approach.

### Algorithm

1. Enumerate the characters in `seq`.
2. For `)`, append `i % 2`; for `(`, append `1 - i % 2`.
3. Return the result.

### Complexity

Let **n** be the length of the input string.

**Time complexity:** $O(n)$<br>
Each character is processed once.

**Space complexity:** $O(1)$<br>
Space allocated for variables is constant and isn't dependant on the length of the array.

### Solution

[View solution](./solution-index-parity.py)