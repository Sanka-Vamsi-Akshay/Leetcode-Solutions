class Solution:
    def jump(self, nums: list[int]) -> int:
        l = len(nums)
        ans = [0] * l
        idx = 1
        for i, j in enumerate(nums):
            while idx < l and idx <= (i + j):
                ans[idx] = ans[i] + 1
                idx += 1
            if idx >= l:
                break
        return ans[-1]