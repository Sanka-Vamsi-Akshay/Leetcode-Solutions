class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0
        for i in words:
            if not (set(i) - allowed):
                cnt += 1
        return cnt