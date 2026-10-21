class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]
        tmp = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                tmp = 0
            dp[i][0] = tmp
        tmp = 1
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                tmp = 0
            dp[0][i] = tmp
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]