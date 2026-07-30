class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for i in word:
            freq[i] = freq.get(i, 0) + 1
        freq = sorted(freq.values(), key = lambda x : x, reverse = True)
        idx = 0
        res = 0
        for i in freq:
            res += (i * ((idx // 8) + 1))
            idx += 1
        return res