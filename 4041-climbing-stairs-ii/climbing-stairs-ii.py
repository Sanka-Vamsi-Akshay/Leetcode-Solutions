class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        minCost = [0] * (n + 1)
        minCost[1] = costs[0] + 1
        if n > 1:
            minCost[2] = costs[1] + min(4, 1 + minCost[1])
        for i in range(3, n + 1):
            minCost[i] = costs[i - 1] + min(minCost[i - 3] + 9, minCost[i - 2] + 4, minCost[i - 1] + 1)
        return minCost[n]