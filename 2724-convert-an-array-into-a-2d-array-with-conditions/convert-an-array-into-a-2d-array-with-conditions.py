class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        res = []
        for i in nums:
            for j in res:
                if i not in j:
                    j.add(i)
                    break
            else:
                res.append({i})
        for i, j in enumerate(res):
            res[i] = list(j)
        return res