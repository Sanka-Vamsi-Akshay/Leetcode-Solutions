class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxx = 1
        idx = 0
        n = len(nums)
        while maxx < n and idx < maxx:
            maxx = max(maxx, nums[idx] + idx + 1)
            idx += 1
        return maxx >= n