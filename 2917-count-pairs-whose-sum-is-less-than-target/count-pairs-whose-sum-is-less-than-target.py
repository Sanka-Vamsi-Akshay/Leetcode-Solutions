class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        cnt = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    cnt += 1
                else:
                    break
            if nums[i] >= target and nums[i] >= 0:
                break
        return cnt