# 2267. Check if There Is a Valid Parentheses String Path

## Problem

A parentheses string is a **non-empty** string consisting only of `(` and `)`. It is **valid** if any of the following conditions is true:

* It is `()`.
* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.
* It can be written as `(A)`, where `A` is a valid parentheses string.

You are given an $m \times n$ matrix of parentheses `grid`. A **valid parentheses string path** in the grid is a path satisfying all of the following conditions:

* The path starts from the upper left cell `(0, 0)`.
* The path ends at the bottom-right cell `(m - 1, n - 1)`.
* The path only ever moves **down or right**.
* The resulting parentheses string formed by the path is **valid**.

Return `true` if there exists a **valid parentheses string path** in `grid`. Otherwise, return `false`.

## 1. Recursive approach

### Approach

Explore every path from the top-left to the bottom-right. Track the current balance: an opening parenthesis increments it, and a closing parenthesis decrements it. A path is abandoned as soon as the balance becomes negative, and it is valid at the destination only when the balance is zero.

### Algorithm

1. Process the current cell and update the balance.
2. Return `False` if the balance becomes negative.
3. At the destination, return whether the balance is zero.
4. Otherwise, recursively try moving down or right.

### Complexity
**Time complexity:** $O(2^{m+n})$<br>
Each recursive call can branch into two moves, with a maximum path length of $m+n-1$.

**Space complexity:** $O(m+n)$<br>
The recursion stack can hold one call for each cell along a path.

### Solution
[View solution](./solution-recursive.py)

## 2. Set-based dynamic programming

### Approach

For each cell, store the set of all nonnegative balances that can reach it. A transition adds one for an opening parenthesis or subtracts one for a closing parenthesis, discarding negative balances. A valid path must have an even number of cells, start with `(`, and end with `)`.

### Algorithm

1. Reject grids whose path length is odd or whose endpoints cannot form a valid string.
2. Initialize the starting cell with balance `1`.
3. For each later cell, transfer reachable balances from the cell above and the cell to the left, applying the current parenthesis.
4. Return whether balance `0` is reachable at the destination.

### Complexity
**Time complexity:** $O(mn(m+n))$<br>
Each cell can have up to $O(m+n)$ distinct balances, and each is transferred from at most two neighboring cells.

**Space complexity:** $O(mn(m+n))$<br>
The grid stores up to $O(m+n)$ balances for each of its $mn$ cells.

### Solution
[View solution](./solution-set-dynamic-programming.py)

## 3. Bitmask dynamic programming

### Approach

Represent the reachable balances at each cell as bits in an integer. Bit `k` is set when balance `k` is reachable. Shifting left by one applies `(`, while shifting right by one applies `)`; bitwise OR merges the possibilities from above and from the left.

### Algorithm

1. Apply the same path-length and endpoint checks as the set-based approach.
2. Initialize the starting cell's bitmask with bit `1` set.
3. For each cell, shift the mask from each available predecessor according to the current parenthesis and OR the results together.
4. Return whether bit `0` is set at the destination.

### Complexity

Let $W$ be the number of bits in a machine word. A mask with $O(L)$ bits occupies $O(\lceil L/W\rceil)$ machine words, and shifting or combining it takes time proportional to that size.

**Time complexity:** $O(mn\lceil (m+n)/W\rceil)$<br>
Each cell performs a constant number of shifts and unions on its masks.

**Space complexity:** $O(mn(m+n))$<br>
There is one integer mask per cell, and each mask can occupy up to $O(m+n)$ space.

### Solution
[View solution](./solution-bitmask-dynamic-programming.py)

## Complexity comparison

| Approach | Time complexity | Space complexity |
| --- | --- | --- |
| Recursive approach | $O(2^{m+n})$ | $O(m+n)$ |
| Set-based dynamic programming | $O(mn(m+n))$ | $O(mn(m+n))$ |
| Bitmask dynamic programming | $O(mn\lceil (m+n)/W\rceil)$ | $O(mn(m+n))$ |
