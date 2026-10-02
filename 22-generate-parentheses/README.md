# 22. Generate Parentheses

## Problem

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

## Solution: Backtracking

### Approach

Build each string one character at a time. Add an opening parenthesis while any remain. Add a closing parenthesis only when there are more closing parentheses remaining than opening parentheses, ensuring every prefix remains valid.

### Algorithm

1. Start with `n` opening and `n` closing parentheses remaining, and an empty current string.
2. If both counts are zero, add the current string to the result.
3. If openings remain, append `(`, recurse with one fewer opening, then backtrack.
4. If `c > o`, append `)`, recurse with one fewer closing, then backtrack.
5. Return all generated strings.

### Complexity

Let $C_n = \frac{1}{n+1}\binom{2n}{n}$ be the n-th Catalan number, the number of valid strings.

**Time complexity:** $O(nC_n) = \Theta(4^n / \sqrt{n})$, approximately $O(4^n)$<br>
There are $C_n$ output strings, each containing $2n$ characters.

**Space complexity:** $O(n)$ auxiliary space<br>
The recursion stack and current string each use $O(n)$ space, not counting the returned output, which uses $O(nC_n)$ space.

### Solution
[View solution](./solution-backtracking.py)