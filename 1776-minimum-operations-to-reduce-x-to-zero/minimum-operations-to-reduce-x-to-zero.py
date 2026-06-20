class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        preSum = {0 : 0}
        idx = tot = 0
        res = float("inf")
        l = len(nums)
        for i in range(l - 1, -1, -1):
            tot += nums[i]
            idx += 1
            if tot not in preSum:
                preSum[tot] = idx
            if tot == x and res > l - i:
                res = l - i
        tot = 0
        for idx, i in enumerate(nums):
            tot += i
            if (x - tot) in preSum and (l - preSum[x - tot]) > idx:
                val = idx + 1 + preSum[x - tot]
                if val < res:
                    res = val
        return res if res != float("inf") else -1