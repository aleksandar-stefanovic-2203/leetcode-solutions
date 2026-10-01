class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for c in s:
            if c in "({[":
                stack.append(c)
            elif stack and pairs[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack
