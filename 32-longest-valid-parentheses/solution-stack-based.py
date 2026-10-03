class Solution:
    def longestValidParentheses(self, s: str) -> int:
        result = 0
        stack = [-1]

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            else:
                stack.pop()

                if stack:
                    result = max(result, i - stack[-1])
                else:
                    stack.append(i)

        return result