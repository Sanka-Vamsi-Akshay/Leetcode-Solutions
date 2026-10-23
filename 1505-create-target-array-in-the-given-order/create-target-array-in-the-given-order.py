class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        res = []
        for i, j in zip(nums, index):
            res.insert(j, i)
        return res