from itertools import groupby
class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            tmp = ''
            for key, group in groupby(res):
                tmp += f"{len(list(group))}{key}"
            res = tmp
        return res