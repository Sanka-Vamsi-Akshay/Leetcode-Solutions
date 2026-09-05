class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = len(nums)
        minVals = [0] * l
        minn = float("inf")
        for i in range(l - 1, -1, -1):
            minn = min(minn, nums[i])
            minVals[i] = minn
        maxx = 0
        for i, j in enumerate(nums):
            maxx = max(maxx, j)
            if maxx - minVals[i] <= k:
                return i
        return -1