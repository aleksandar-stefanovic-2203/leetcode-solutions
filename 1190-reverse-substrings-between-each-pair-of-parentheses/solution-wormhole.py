from collections import deque

class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses = deque()
        pair = [0] * n

        for i, c in enumerate(s):
            if c == "(":
                open_parentheses.append(i)
            elif c == ")":
                j = open_parentheses.pop()
                pair[i] = j
                pair[j] = i

        result = []
        curr_index = 0
        direction = 1

        while curr_index < n:
            if s[curr_index] == "(" or s[curr_index] == ")":
                curr_index = pair[curr_index]
                direction = -direction
            else:
                result.append(s[curr_index])
            
            curr_index += direction

        return "".join(result)

print(Solution().reverseParentheses("(ed(et(oc))el)"))