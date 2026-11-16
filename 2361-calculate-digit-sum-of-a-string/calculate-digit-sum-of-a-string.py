class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            res = ''
            tot = 0
            for i, j in enumerate(s):
                tot += int(j)
                if (i + 1) % k == 0:
                    res += str(tot)
                    tot = 0
            if len(s) % k != 0:
                res += str(tot)
            s = res
        return s