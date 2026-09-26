# 1807. Evaluate the Bracket Pairs of a String

## Problem

You are given a string `s` that contains some bracket pairs, with each pair containing a **non-empty** key.

* For example, in the string `"(name)is(age)yearsold"`, there are **two** bracket pairs that contain the keys `"name"` and `"age"`.

You know the values of a wide range of keys. This is represented by a 2D string array `knowledge` where each knowledge[i] = [key<sub>i</sub>, value<sub>i</sub>] indicates that key key<sub>i</sub> has a value of value<sub>i</sub>.

You are tasked to evaluate **all** of the bracket pairs. When you evaluate a bracket pair that contains some key key<sub>i</sub>, you will:

Replace key<sub>i</sub> and the bracket pair with the key's corresponding value<sub>i</sub>.
If you do not know the value of the key, you will replace key<sub>i</sub> and the bracket pair with a question mark `"?"` (without the quotation marks).

Each key will appear at most once in your `knowledge`. There will not be any nested brackets in `s`.

Return *the resulting string after evaluating **all** of the bracket pairs*.

## 1. Linear knowledge search

For each key, scan the knowledge pairs until its value is found. Replace all occurrences of that parenthesized key, or use `?` if it is missing.

### Complexity

Let **n** be the length of the input string and **k** the number of knowledge pairs.

**Time complexity:** $O(n^2 + nk)$ in the worst case, due to rescanning and replacing across the string for each distinct key.

**Space complexity:** $O(n)$ for the updated string.

### Solution

[View solution](./solution-linear-search.py)

## 2. Hash map with string replacement

Build a dictionary from the knowledge pairs, then look up each parenthesized key in constant expected time. The string is rescanned and updated after each replacement.

### Complexity

**Time complexity:** $O(n^2 + k)$ in the worst case, due to repeated scans and replacements of the string.

**Space complexity:** $O(n + k)$ for the updated string and dictionary.

### Solution

[View solution](./solution-hash-map-replace.py)

## 3. Single-pass construction

Build a dictionary once, then scan the input from left to right. Append ordinary characters directly to the result; when a closing parenthesis is reached, look up the enclosed key and append its value or `?`.

### Complexity

**Time complexity:** $O(n + k)$, including dictionary construction and the scan.

**Space complexity:** $O(n + k)$ for the dictionary and result.

### Solution

[View solution](./solution-single-pass.py)

## Complexity comparison

| Approach | Time complexity | Space complexity |
| --- | --- | --- |
| Linear knowledge search | $O(n^2 + nk)$ | $O(n)$ |
| Hash map with string replacement | $O(n^2 + k)$ | $O(n + k)$ |
| Single-pass construction | $O(n + k)$ | $O(n + k)$ |
