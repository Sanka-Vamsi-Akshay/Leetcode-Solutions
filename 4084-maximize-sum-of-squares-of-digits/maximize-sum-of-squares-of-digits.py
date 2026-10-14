class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        l = sum // 9
        res = "9" * l
        r = sum % 9
        if r > 0:
            res += str(r)
            l += 1
        res += "0" * (num - l)
        return res