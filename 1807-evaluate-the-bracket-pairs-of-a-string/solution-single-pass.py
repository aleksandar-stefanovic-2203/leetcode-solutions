class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hash_table = dict(knowledge)

        result, start = [], -1
        for i, c in enumerate(s):
            if c == "(":
                start = i
            elif c == ")":
                key = s[start + 1 : i]
                value = hash_table.get(key, "?")
                result.append(value)
                start = -1
            elif start == -1:
                result.append(c)

        return "".join(result)