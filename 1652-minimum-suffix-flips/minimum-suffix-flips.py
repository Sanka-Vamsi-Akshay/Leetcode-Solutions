class Solution:
    def minFlips(self, target: str) -> int:
        val1 = '1'
        val2 = '0'
        res = 0
        for i in target:
            if i == val1:
                res += 1
                val1, val2 = val2, val1
        return res