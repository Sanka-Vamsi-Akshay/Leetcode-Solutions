class Solution:
    def GCD(self, n1, n2):
        if n1 < n2:
            return self.GCD(n2, n1)
        if n1 % n2 == 0:
            return n2
        return self.GCD(n2, n1 % n2)
    def maxPairStrength(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                val = nums[i] * nums[j]
                if val > res:
                    res = max(res, val // (self.GCD(nums[i], nums[j]) ** 2))
        return res