class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        allEven = allOdd = True
        minn = float("inf")
        for i in nums1:
            if i % 2 == 0:
                allOdd = False
            else:
                allEven = False
            minn = min(minn, i)
        if allOdd or allEven:
            return True
        if minn % 2 == 0:
            return False
        return True