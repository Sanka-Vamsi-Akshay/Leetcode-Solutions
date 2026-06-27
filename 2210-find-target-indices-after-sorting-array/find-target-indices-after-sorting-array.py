class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = ((r - l) // 2) + l
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                if m != 0 and nums[m - 1] == target:
                    r = m - 1
                else:
                    while m < n and nums[m] == target:
                        res.append(m)
                        m += 1
                    break
        return res