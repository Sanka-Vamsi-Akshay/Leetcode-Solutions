class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        def find(comb, tot):
            for i in candidates:
                if comb and comb[-1] > i:
                    continue
                elif tot > target:
                    break
                elif tot + i > target:
                    continue
                elif tot + i == target:
                    res.append(comb + [i])
                    continue
                else:
                    find(comb + [i], tot + i)
        find([], 0)
        return res