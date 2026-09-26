class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        hash_table = {}
        
        for row in knowledge:
            hash_table[row[0]] = row[1]

        start = s.find("(")
        end = s.find(")")

        while start != -1:
            key = s[start + 1 : end]            

            if key in hash_table:
                s = s.replace("(" + key + ")", hash_table[key])
            else:
                s = s.replace("(" + key + ")", "?")

            start = s.find("(")
            end = s.find(")")

        return s