class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        curr = []

        def generate(o: int, c: int):
            if o == 0 and c == 0:
                result.append("".join(curr))
                return

            if o > 0:
                curr.append("(")
                generate(o - 1, c)
                curr.pop()
            if c > o:
                curr.append(")")
                generate(o, c - 1)
                curr.pop()

        generate(n, n)
        return result