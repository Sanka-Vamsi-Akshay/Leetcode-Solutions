class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        m = nums[len(nums) // 2]
        res = 0
        for i in nums:
            res += abs(i - m)
        return res