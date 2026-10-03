class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open = close = max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                open += 1
            else:
                close += 1

            if open == close:
                max_len = max(max_len, 2 * open)
            elif close > open:
                open = close = 0

        open = close = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                open += 1
            else:
                close += 1

            if open == close:
                max_len = max(max_len, 2 * open)
            elif open > close:
                open = close = 0

        return max_len