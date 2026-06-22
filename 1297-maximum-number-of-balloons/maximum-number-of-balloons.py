from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text = Counter(text)
        b = text.get('b', 0)
        a = text.get('a', 0)
        l = text.get('l', 0) // 2
        o = text.get('o', 0) // 2
        n = text.get('n', 0)
        return min(b, a, l, o, n)