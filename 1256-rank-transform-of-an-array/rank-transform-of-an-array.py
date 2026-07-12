import heapq
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dup = arr[:]
        heapq.heapify(dup)
        rank = {}
        r = 1
        while dup:
            v = heapq.heappop(dup)
            if v not in rank:
                rank[v] = r
                r += 1
        for i, j in enumerate(arr):
            arr[i] = rank.get(j)
        return arr