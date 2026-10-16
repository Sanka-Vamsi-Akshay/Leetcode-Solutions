class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for _ in range(n - 1):
            tmp = ''
            ch = res[0]
            cnt = 0
            for i in res:
                if i == ch:
                    cnt += 1
                else:
                    tmp += f"{cnt}{ch}"
                    ch = i
                    cnt = 1
            res = tmp + f"{cnt}{ch}"
        return res