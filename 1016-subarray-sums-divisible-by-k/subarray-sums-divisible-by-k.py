class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        summ = res = 0
        preSum = {0 : 1}
        for i in nums:
            summ += i
            d = summ % k
            if d in preSum:
                res += preSum[d]
                preSum[d] += 1
            else:
                preSum[d] = 1
        return res