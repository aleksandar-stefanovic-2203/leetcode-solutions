# 1. Two Sum

## Problem

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

## 1. Brute-force approach

### Approach

The simplest way is to check every pair of indices `(i, j)` and test whether their sum is equal to the target.

### Algorithm

1. Loop over all indices `i` from `0` to `n - 2`.
2. For every `i`, loop over all indices `j` from `i + 1` to `n - 1`.
3. If `nums[i] + nums[j] == target`, return `[i, j]`.

### Complexity
**Time complexity:** $O(n^2)$<br>
We compare each pair of elements once, so the number of checks grows quadratically with the array size.

**Space complexity:** $O(1)$<br>
The algorithm uses only a few variables and does not allocate additional data structures.

### Solution
[View solution](./solution-brute-force.py)

## 2. Hash-map approach

### Approach

Instead of checking every pair, we store numbers that we have already seen. While iterating through the array, we calculate the complement:

```python
complement = target - nums[i]
```

If the complement has already been seen, then we found the pair.

### Algorithm

1. Create an empty dictionary `map`.
2. Iterate through the array with index `i`.
3. Calculate `complement = target - nums[i]`.
4. If `complement` exists in `map`, return `[map[complement], i]`.
5. Otherwise, store `nums[i]` with its index in `map`.

### Complexity
**Time complexity:** $O(n)$<br>
Each element is processed once, and dictionary lookups are constant on average.

**Space complexity:** $O(n)$<br>
In the worst case, we store all numbers in the dictionary.

### Solution
[View solution](./solution-hash-map.py)

## Complexity comparison

| Approach | Time complexity | Space complexity |
| --- | --- | --- |
| Brute-force | $O(n^2)$ | $O(1)$ |
| Hash-map | $O(n)$ | $O(n)$ |

## Final note

The hash-map solution is the preferred one for this problem because it is both faster and more scalable for larger inputs.
