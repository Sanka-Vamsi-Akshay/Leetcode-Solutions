class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        garbageIdx = {"M" : 0, "P" : 0, "G" : 0}
        res = 0
        for idx, i in enumerate(garbage):
            for j in i:
                res += 1
                garbageIdx[j] = idx
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        for i in garbageIdx:
            if garbageIdx[i] != 0:
                res += travel[garbageIdx[i] - 1]
        return res