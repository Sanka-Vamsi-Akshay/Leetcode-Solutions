class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        path = [('#' * (n - 1)) + '.' for _ in range(m)]
        path[0] = '.' * n
        return path