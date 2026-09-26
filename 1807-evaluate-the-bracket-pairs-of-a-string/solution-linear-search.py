class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        start = s.find("(")
        end = s.find(")")

        while start != -1:
            key = s[start + 1 : end]

            found = False
            for row in knowledge:
                if key == row[0]:
                    s = s.replace("(" + key + ")", row[1])
                    found = True
                    break
            if not found:
                s = s.replace("(" + key + ")", "?")

            start = s.find("(")
            end = s.find(")")

        return s