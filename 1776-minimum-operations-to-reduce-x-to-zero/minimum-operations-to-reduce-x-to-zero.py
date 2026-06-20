class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        x = sum(nums) - x
        n = len(nums)
        if x == 0:
            return n
        if x < 0:
            return -1
        tot = 0
        l = 0
        maxx = 0
        for idx, i in enumerate(nums):
            tot += i
            while tot > x:
                tot -= nums[l]
                l += 1
            if tot == x:
                val = idx - l + 1
                if val > maxx:
                    maxx = val
        if maxx == 0:
            return -1
        return n - maxx