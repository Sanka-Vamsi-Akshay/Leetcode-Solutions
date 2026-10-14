class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        n = []
        for _ in range(num):
            if sum > 9:
                n.append("9")
                sum -= 9
            else:
                n.append(f"{sum}")
                sum = 0
        return ''.join(n)
