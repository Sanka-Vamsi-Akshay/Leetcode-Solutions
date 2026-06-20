class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        preSum = {0 : 0}
        x = sum(nums) - x
        l = 0
        tot = 0
        maxx = 0
        for idx, i in enumerate(nums):
            tot += i
            if tot == x:
                maxx = idx + 1
            elif (tot - x) in preSum:
                if maxx < idx - preSum[tot - x]:
                    maxx = idx - preSum[tot - x]
            if tot not in preSum:
                preSum[tot] = idx
            l += 1
        if maxx == 0:
            if x == 0:
                return l
            return -1
        return l - maxx