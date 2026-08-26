class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        i = j = 0
        tmp = k
        res = ['a'] * 100
        while True:
            while j < n and tmp > 0:
                if s[j] == "1":
                    tmp -= 1
                j += 1
            if tmp != 0:
                break
            while s[i] == "0":
                i += 1
            if len(res) > (j - i):
                res = s[i : j]
            elif len(res) == (j - i):
                res = min(res, s[i : j])
            while s[i] != "1":
                i += 1
            i += 1
            tmp += 1
        if res[0] == "a":
            return ""
        return ''.join(res)