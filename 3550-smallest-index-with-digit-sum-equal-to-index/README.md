# 3550. Smallest Index With Digit Sum Equal to Index

## Problem

You are given an integer array `nums`.

Return the smallest index `i` such that the sum of the digits of `nums[i]` is equal to `i`.

If no such index exists, return `-1`.

## Approach

For each index, calculate the digit sum of `nums[i]` and compare it with the index. Return the index if they match, or `-1` if no such index is found.

Sum of digits is calculated by extracting digits from the rightmost to the leftmost.

Because iteration is done **from left to right**, if we find an index that satisfies the condition it is guaranteed to be the **smallest one**.

## Complexity Analysis
Let `n` be the number of elements in an array, and `m` the largest number in an array.

**Time complexity:** $O(n \log_{10}(m))$<br>
There are n iterations of the algorithm at most, and in every iteration we calculate the digit sum which takes $O(log_{10}(m))$ time.

**Space complexity:** $O(1)$<br>
Allocated space is not dependent on the size of the array.

## Solution
[View solution](./solution.py)