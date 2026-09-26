class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kvPairs = {}
        for i, j in knowledge:
            kvPairs[i] = j
        s = s.split("(")
        for i in range(1, len(s)):
            tmp = s[i].split(")")
            s[i] = kvPairs.get(tmp[0], "?") + tmp[1]
        return ''.join(s)