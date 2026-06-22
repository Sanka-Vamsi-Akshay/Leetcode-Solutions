from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = a = l = o = n = 0
        for i in text:
            match i:
                case 'b': b += 1
                case 'a': a += 1
                case 'l': l += 1
                case 'o': o += 1
                case 'n': n += 1
                case _: pass
        if not(b or a or l or o or n):
            return 0
        return min(b, a, l // 2, o // 2, n)