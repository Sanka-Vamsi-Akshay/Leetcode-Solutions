class Solution:
    def convertToBase7(self, num: int) -> str:
        s = -1 if num < 0 else 1
        num = abs(num)
        res = 0
        p = 0
        while num > 0:
            res = ((10 ** p) * (num % 7)) + res
            num //= 7
            p += 1
        return f"{s * res}"