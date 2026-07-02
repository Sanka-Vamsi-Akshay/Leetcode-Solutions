class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        for i in range(k):
            res += nums[i]
        summ = res
        for i in range(k, len(nums)):
            summ -= nums[i - k]
            summ += nums[i]
            if res < summ:
                res = summ
        return res / k