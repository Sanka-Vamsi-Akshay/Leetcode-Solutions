class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = [[0] * n for _ in range(m)]
        res[0][0] = [1, 1]
        tmp = 1
        for i in range(1, m):
            if grid[i - 1][0] == 1:
                tmp = 0
            res[i][0] = [0, tmp]
        tmp = 1
        for i in range(1, n):
            if grid[0][i - 1] == 1:
                tmp = 0
            res[0][i] = [tmp, 0]
        for i in range(1, m):
            for j in range(1, n):
                res[i][j] = [0, res[i - 1][j][0]]
                if grid[i - 1][j] == 0:
                    res[i][j][1] += res[i - 1][j][1]
                res[i][j][0] += res[i][j - 1][1]
                if grid[i][j - 1] == 0:
                    res[i][j][0] += res[i][j - 1][0]
        return (res[m - 1][n - 1][0] + res[m - 1][n - 1][1]) % 1000000007