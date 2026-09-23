# 1658. Minimum Operations to Reduce X to Zero

## Problem

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

## 1. Recursive approach

### Approach

My first idea was to try to solve the problem recursively by trying to remove elements from both ends of the current array and compare their number of operations, always taking the minimum of the two.

### Algorithm

At each step, there are two possible choices: remove the leftmost or the rightmost element. I recursively explore both possibilities and keep the one requiring fewer operations.

The recursion stops when:

* `x == 0` — a valid solution has been found.
* `x < 0` — the removed elements have exceeded `x`, so this branch is invalid.
* The array is empty while `x != 0` — this branch cannot reach the target.

If one branch is invalid (`-1`), I use the other branch. If both are valid, I take the minimum:

```python
if minLeft == -1 or minRight == -1:
    return max(minLeft, minRight)
else:
    return min(minLeft, minRight)
```

### Complexity
**Time complexity:** $O(2^n)$<br>
At each step we recursively explore **2** choices, and the maximum recursion depth is **n**, where **n** is the length of the array.

**Note:** Slicing lists in python takes O(k) time, where k is the length of an array being sliced. In this approach we slice the array on every recursive call, which contributes to the time complexity, though it seems it doesn't affect the growth rate.

**Space complexity:** $O(n^2)$<br>
Even though the maximum recursion depth is **n**, in each recursive call we store the copy of the array on the stack. In the first call the size of the array is **n-1**, in the second **n-2**, and so on until **0**. This sums up to $\frac{(n-1)n}{2}$, which is $O(n^2)$ space complexity.

### Solution
[View solution](./solution-recursive-approach.py)

## 2. Index-based recursive approach

### Approach

I wanted to optimize the first approach by using indexes to mark the leftmost and rightmost elements in the current array instead of slicing it on every recursion call.

### Algorithm

Increment `left` when removing the leftmost element and decrement `right` when removing the rightmost one. The base cases are `x == 0`, `x < 0`, and `left > right`.

### Complexity
**Time complexity:** $O(2^n)$<br>
There are still two recursive choices at each level, so the time complexity remains exponential.

**Space complexity:** $O(n)$<br>
Only the recursion stack and primitive values are stored; no array copies are created.

### Solution
[View solution](./solution-index-based-recursive-approach.py)

## 3. Sliding-window approach

### Approach

Instead of selecting the elements to remove from the left and right, I look for the longest contiguous subarray that can remain in the array.

If the sum of all elements is `totalSum`, the elements that remain must have a sum of:

```text
targetSum = totalSum - x
```

The minimum number of operations is:

```text
minimum operations = len(nums) - longest subarray length
```

Because all values are positive, a sliding window can maintain the sum in linear time.

### Algorithm

1. Calculate `targetSum = sum(nums) - x`.
2. Return `-1` if `targetSum < 0`, because the removed elements cannot sum to `x`.
3. Return `len(nums)` if `targetSum == 0`, because every element must be removed.
4. Use two pointers to maintain a sliding window whose sum is at most `targetSum`.
5. Expand the window by moving the right pointer through the array.
6. While the window sum is greater than `targetSum`, move the left pointer forward and subtract the removed values from the sum.
7. Track the longest window whose sum equals `targetSum`.
8. Return `len(nums) - maxLength`, or `-1` if no such window exists.

### Complexity
**Time complexity:** $O(n)$<br>
Each element enters and leaves the sliding window at most once, so both pointers move through the array at most **n** times.

**Space complexity:** $O(1)$<br>
The solution uses only a few variables in addition to the input array.

### Solution
[View solution](./solution-sliding-window.py)

## Complexity comparison

| Approach | Time complexity | Space complexity |
| --- | --- | --- |
| Recursive approach | $O(2^n)$, plus list-slicing overhead | $O(n^2)$ |
| Index-based recursive approach | $O(2^n)$ | $O(n)$ |
| Sliding-window approach | $O(n)$ | $O(1)$ |