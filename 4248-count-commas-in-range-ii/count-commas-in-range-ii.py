class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        tmp = 1000
        val = 1
        res = 0
        while n > (tmp * 1000) - 1:
            res += val * (tmp * 999)
            tmp *= 1000
            val += 1
        res += val * (n - tmp + 1)
        return res