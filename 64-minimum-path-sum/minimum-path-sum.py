import heapq
class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return grid[0][0]
        v = set((0, 0))
        q = [[grid[0][0], (0, 0)]]
        heapq.heapify(q)
        while True:
            val, idx = heapq.heappop(q)
            if (idx[0] + 1 == m - 1 and idx[1] == n - 1) or (idx[0] == m - 1 and idx[1] + 1 == n - 1):
                return val + grid[m - 1][n - 1]
            if idx[0] + 1 != m and (idx[0] + 1, idx[1]) not in v:
                heapq.heappush(q, [val + grid[idx[0] + 1][idx[1]], (idx[0] + 1, idx[1])])
                v.add((idx[0] + 1, idx[1]))
            if idx[1] + 1 != n and (idx[0], idx[1] + 1) not in v:
                heapq.heappush(q, [val + grid[idx[0]][idx[1] + 1], (idx[0], idx[1] + 1)])
                v.add((idx[0], idx[1] + 1))