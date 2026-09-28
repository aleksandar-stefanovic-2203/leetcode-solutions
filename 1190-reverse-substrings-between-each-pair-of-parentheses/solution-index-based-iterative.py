class Solution:
    def reverseParentheses(self, s: str) -> str:
        parentheses_indicies = []
        result = []

        for c in s:
            if c == "(":
                parentheses_indicies.append(len(result))
            elif c == ")":
                start = parentheses_indicies.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(c)

        return "".join(result)

print(Solution().reverseParentheses("(ed(et(oc))el)"))