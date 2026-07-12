import heapq
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        for r, num in enumerate(sorted(set(arr)), 1):
            rank[num] = r
        return [rank[num] for num in arr]