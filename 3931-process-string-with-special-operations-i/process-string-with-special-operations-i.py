class Solution:
    def processStr(self, s: str) -> str:
        res = []
        n = 0
        for i in s:
            if i == '*': 
                if res:
                    res.pop()
                    n -= 1
            elif i == '#':
                res.extend(res)
                n *= 2
            elif i == '%':
                l, r = 0, n - 1
                while l < r:
                    res[l], res[r] = res[r], res[l]
                    l += 1
                    r -= 1
            else:
                res.append(i)
                n += 1
        return ''.join(res)