class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        m = p = g = 0
        res = 0
        for idx, i in enumerate(garbage):
            for j in i:
                res += 1
                match j:
                    case "M": m = idx
                    case "P": p = idx
                    case "G": g = idx
                    case _: pass
        for i in range(1, len(travel)):
            travel[i] += travel[i - 1]
        if m:
            res += travel[m - 1]
        if p:
            res += travel[p - 1]
        if g:
            res += travel[g - 1]
        return res