class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        res = []
        for i in zip(*matrix):
            res.append(i)
        return res