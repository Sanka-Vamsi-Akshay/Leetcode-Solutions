class Solution:
    def GCD(self, n1, n2):
        if n1 < n2:
            return GCD(n2, n1)
        if n1 % n2 == 0:
            return n2
        return self.GCD(n2, n1 % n2)
    def maxPairStrength(self, nums: list[int]) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                val = nums[i] * nums[j]
                if val < res:
                    continue
                res = max(res, val // (self.GCD(nums[i], nums[j]) ** 2))
        return res