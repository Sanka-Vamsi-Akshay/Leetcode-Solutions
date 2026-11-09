class Solution:
    def numSquares(self, n: int) -> int:
        squares = {1}
        minWays = [float("inf")] * n
        minWays[0] = 1
        for i in range(2, n + 1):
            tmp = i ** 0.5
            if int(tmp) == tmp:
                squares.add(i)
                minWays[i - 1] = 1
            else:
                for j in squares:
                    minWays[i - 1] = min(minWays[i - 1], 1 + minWays[i - j - 1])
        return minWays[n - 1]