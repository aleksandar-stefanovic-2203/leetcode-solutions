class Solution:
    def reverseParentheses(self, s: str) -> str:
        def reverseExpression(s: str, start: int, end: int, reverse: bool) -> list[str]:
            result = []
            p_start = -1
            parentheses_count = 0
            for i in range(start, end):
                c = s[i]
                if c == "(":
                    if p_start == -1:
                        p_start = i
                    parentheses_count += 1
                elif c == ")":
                    parentheses_count -= 1
                    if parentheses_count == 0:
                        reversed_expression = reverseExpression(s, p_start + 1, i, True)
                        result.extend(reversed_expression)
                        p_start = -1
                elif p_start < 0:
                    result.append(c)

            return result if not reverse else result[::-1]

        result = reverseExpression(s, 0, len(s), False)
        return "".join(result)

print(Solution().reverseParentheses("(ed(et(oc))el)"))